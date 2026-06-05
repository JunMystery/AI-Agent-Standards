---
name: large-file-refactor
description: Workflow for refactoring large or monolithic files by responsibility, not by line-count alone. Use when splitting files over 300 LOC, extracting modules, reducing mixed responsibilities, or breaking React components into hooks/subcomponents.
origin: AI-Agent-Standards
---

# Large-File Refactor

Use this skill when a task asks to split a large file, reduce a monolithic module, extract services/controllers/helpers, or bring files closer to the 300 LOC guideline.

## Core Rule

Split by responsibility, not by line count alone.

Do not cut a file into arbitrary chunks just to satisfy a numeric target. A 320-line cohesive algorithm may be better left intact, while a 260-line file with unrelated validation, persistence, and notification logic may deserve extraction.

## Decision Thresholds

- `<300 LOC`: keep the file unless it clearly mixes unrelated responsibilities.
- `300-500 LOC`: recommend splitting only when the file has more than one durable responsibility.
- `>500 LOC`: perform an explicit split analysis before implementation.

Count meaningful code first. Ignore blank lines and comments when judging whether the file is truly large.

## Workflow

1. Analyze responsibilities.
   - List the functional blocks: classes, functions, handlers, JSX sections, data access, validation, transformation, side effects.
   - Name what each block owns and what can change independently.

2. Cluster cohesive code.
   - Keep code together when it is called together most of the time or shares one domain responsibility.
   - Prefer domain/package-local extraction over distant shared folders.

3. Map dependencies before extracting.
   - Identify imports, globals, shared types, callbacks, side effects, and public API callers.
   - Check for circular import risk before creating new files.
   - If splitting creates a cycle, choose a different boundary, introduce dependency inversion, or keep the code together.

4. Extract with compatibility.
   - Preserve behavior and public API unless the user explicitly approved an API change.
   - Keep orchestration in the original file when that makes migration safer.
   - Use existing project naming, file layout, test helpers, and module style.

5. Verify after refactor.
   - Run existing tests without changing their intent.
   - Check imports and circular dependency warnings when tooling exists.
   - Confirm new files remain focused and generally under 300 meaningful LOC.

## Common Boundaries

- Services/controllers: split validation, domain logic, persistence, notification, and logging only when they are separate responsibilities.
- React/UI: extract stateful hooks, repeated subcomponents, and dense table/chart sections; keep the parent as orchestration.
- Pipelines: split extract, transform, load, validation, retry, metrics, and notification when dependencies flow one way.
- Algorithms: extract helpers or preprocessing only if the core algorithm remains easier to understand.

## Exceptions

Do not split by default when:

- The file is generated, vendored, or externally synchronized.
- The file is mostly constants or configuration that changes together.
- A cohesive algorithm would become harder to reason about across files.
- Splitting would create circular imports or tighter coupling.
- The change would require broad public API migration outside the user's request.

## Output Expectation

When this skill is active, provide:

- Responsibility analysis for the large file.
- Split/keep decision with the threshold applied.
- Proposed module boundaries and dependency direction.
- Circular dependency risk and mitigation.
- Files to create/change and public API impact.
- Verification evidence: tests/checks run, import-cycle checks when available, and any residual risk.
