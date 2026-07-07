# Tasks: LangGraph Process Score Grading

**Input**: Design documents from `specs/001-langgraph-process-score/`

## Phase 1: Setup

- [x] T001 Create Spec Kit feature directory `specs/001-langgraph-process-score`
- [x] T002 Confirm `kimi`, `agy`, and `codex` CLI availability from project root
- [x] T003 Confirm `langgraph` is available under Python 3.12

## Phase 2: Foundation

- [x] T004 Define one-student grading contract in `specs/001-langgraph-process-score/spec.md`
- [x] T005 Define implementation plan in `specs/001-langgraph-process-score/plan.md`
- [x] T006 Implement CLI path resolution and UTF-8 subprocess wrapper in `tools/process_score_langgraph.py`
- [x] T007 Implement LangGraph nodes for evidence loading, Kimi review, agy review, Codex arbitration, and final persistence in `tools/process_score_langgraph.py`

## Phase 3: User Story 1 - Grade One Student Reliably

- [x] T008 [US1] Generate local reviewer prompts in the selected student directory
- [x] T009 [US1] Persist raw CLI outputs and command status for the selected student
- [x] T010 [US1] Persist final Markdown and JSON arbitration files for the selected student

## Phase 4: User Story 2 - Avoid Broken CLI Context

- [x] T011 [US2] Launch Kimi with explicit `--work-dir`
- [x] T012 [US2] Launch agy with subprocess `cwd` set to the student directory
- [x] T013 [US2] Launch Codex with `codex exec -C <student_dir> --skip-git-repo-check`
- [x] T014 [US2] Add timeout and failure persistence for all three CLI nodes

## Phase 5: Smoke Validation

- [x] T015 Run `py -3 -m py_compile tools/process_score_langgraph.py`
- [x] T016 Run one-student smoke test for an ungraded student directory
- [x] T017 Inspect output files and confirm final JSON contains a score and completion status

## Follow-up

- [x] T018 Extend workflow to batch scheduling after smoke test passes
- [x] T019 Add Excel `pscj` write-back after batch scoring is stable
