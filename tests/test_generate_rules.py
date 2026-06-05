import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = ROOT / "scripts" / "generate-rules.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("generate_rules", GENERATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GenerateRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.generator = load_generator()

    def test_manifest_contains_expected_outputs(self):
        agents = self.generator.load_manifest(ROOT)
        outputs = {agent["output"] for agent in agents}

        self.assertEqual(
            outputs,
            {
                "AGENTS.md",
                "CLAUDE.md",
                "GEMINI.md",
                "COPILOT.md",
                ".instructions.md",
                ".cursorrules",
                ".cursor/rules/karpathy-guidelines.mdc",
            },
        )

    def test_render_all_is_deterministic(self):
        first = self.generator.render_all(ROOT)
        second = self.generator.render_all(ROOT)

        self.assertEqual(first, second)

    def test_check_outputs_passes_for_matching_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "AGENTS.md"
            outputs = {path: "expected\n"}
            path.write_text("expected\n", encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                result = self.generator.check_outputs(outputs)
            self.assertEqual(result, 0)

    def test_check_outputs_fails_for_drift(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "AGENTS.md"
            outputs = {path: "expected\n"}
            path.write_text("drifted\n", encoding="utf-8")

            with redirect_stdout(io.StringIO()):
                result = self.generator.check_outputs(outputs)
            self.assertEqual(result, 1)

    def test_cursor_mdc_keeps_frontmatter(self):
        outputs = self.generator.render_all(ROOT, "cursor")
        content = next(iter(outputs.values()))

        self.assertTrue(content.startswith("---\n"))
        self.assertIn("alwaysApply: true", content)
        self.assertIn("---\n\n# Karpathy Behavioral Guidelines", content)

    def test_generated_instructions_keep_skill_references(self):
        outputs = self.generator.render_all(ROOT)

        for content in outputs.values():
            self.assertIn("SKILL-REFERENCE.md", content)
            self.assertIn("skills/", content)


if __name__ == "__main__":
    unittest.main()
