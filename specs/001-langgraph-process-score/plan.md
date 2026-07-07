# Implementation Plan: LangGraph Process Score Grading

**Branch**: `001-langgraph-process-score` | **Date**: 2026-07-07 | **Spec**: `specs/001-langgraph-process-score/spec.md`

## Summary

Implement a Python LangGraph workflow that grades one prepared student evidence directory with three external CLI reviewers: Kimi CLI, agy CLI, and Codex CLI. The workflow fixes the prior failure mode by controlling working directories, UTF-8 environment, timeouts, and durable per-node outputs.

## Technical Context

**Language/Version**: Python 3.12 via `py -3`

**Primary Dependencies**: `langgraph`, standard library `subprocess`, `pathlib`, `json`

**Storage**: Local markdown and JSON files inside each student process-score directory

**Testing**: `py -3 -m py_compile` plus one-student smoke run

**Target Platform**: Windows PowerShell environment

**Project Type**: Internal CLI automation script

**Performance Goals**: One missing-submission or short-evidence student completes within bounded CLI timeouts

**Constraints**: No roster Excel write-back in this feature. No destructive cleanup. Preserve existing grading files unless `--force` is passed.

**Scale/Scope**: One-student smoke test now. Batch parallel grading later.

## Constitution Check

- Read existing files before writing: satisfied by inspecting evidence, CLI help, and Spec Kit templates.
- Keep changes scoped: only add Spec Kit artifacts and one LangGraph script.
- Test before declaring done: run syntax check and one-student smoke test.
- Do not overwrite user data: existing grading files are preserved unless `--force` is explicit.

## Project Structure

### Documentation

```text
specs/001-langgraph-process-score/
|-- spec.md
|-- plan.md
|-- tasks.md
```

### Source Code

```text
tools/
|-- process_score_langgraph.py
```

### Output Files Per Student

```text
langgraph-kimi-prompt.md
langgraph-agy-prompt.md
langgraph-codex-prompt.md
kimi-score.langgraph.md
agy-score.langgraph.md
codex-score.langgraph.md
codex-cli.langgraph.log
final-arbitration.langgraph.md
final-arbitration.langgraph.json
```

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Three CLI reviewers | User explicitly requires Kimi CLI, agy CLI, and Codex CLI | Single-model grading repeats the earlier credibility problem |
| LangGraph state machine | User explicitly requires LangGraph and resumable workflow | Ad hoc loops already failed with hidden blocking and wrong cwd |
