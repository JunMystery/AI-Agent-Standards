from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]

MOJIBAKE_MARKERS = tuple(
    bytes.fromhex(marker).decode("cp1252")
    for marker in (
        "f09f",
        "e29c",
        "e28094",
        "e286",
        "e294",
        "e2ad",
        "c2",
        "c3",
        "c4",
        "c6",
        "e1bb",
    )
)

TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json"}
SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}


class EncodingHygieneTests(unittest.TestCase):
    def test_active_text_files_do_not_contain_mojibake_markers(self):
        offenders = []

        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix not in TEXT_SUFFIXES:
                continue
            if any(part in SKIP_PARTS for part in path.parts):
                continue

            content = path.read_text(encoding="utf-8")
            markers = [marker for marker in MOJIBAKE_MARKERS if marker in content]
            if markers:
                offenders.append(f"{path.relative_to(ROOT)}: {', '.join(markers)}")

        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main()
