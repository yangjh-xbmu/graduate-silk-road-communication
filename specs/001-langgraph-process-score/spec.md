# Feature Specification: LangGraph Process Score Grading

**Feature Branch**: `001-langgraph-process-score`

**Created**: 2026-07-07

**Status**: Draft

**Input**: User description: "Build a LangGraph workflow for regular process-score grading using kimi cli, agy cli, and codex cli. Run one student as a smoke test."

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Grade One Student Reliably (Priority: P1)

A grader can run one command against one prepared student evidence directory and receive durable Kimi, agy, and Codex CLI outputs plus a final arbitration record.

**Why this priority**: One-student validation proves the corrected execution model before batch grading.

**Independent Test**: Run the workflow for one ungraded student directory and verify that all prompt, raw review, and arbitration files are created.

**Acceptance Scenarios**:

1. **Given** a student directory containing `process-evidence.md`, **When** the workflow runs, **Then** it creates `kimi-score.langgraph.md`, `agy-score.langgraph.md`, `codex-score.langgraph.md`, `final-arbitration.langgraph.md`, and `final-arbitration.langgraph.json`.
2. **Given** one CLI fails or times out, **When** the workflow continues, **Then** the failure is recorded in that CLI output and passed to Codex arbitration instead of silently blocking.

---

### User Story 2 - Avoid Broken CLI Context (Priority: P2)

The workflow launches each CLI with explicit working directory, workspace scope, UTF-8 environment, timeout, and output path so it does not repeat the earlier prompt-location and GBK failures.

**Why this priority**: The previous multi-agent run failed because CLI subprocesses used the wrong working directory and had no fast failure boundary.

**Independent Test**: Inspect command logs and confirm each CLI received the intended student directory and bounded timeout.

**Acceptance Scenarios**:

1. **Given** agy is invoked, **When** the workflow starts it, **Then** the process current directory is the student directory and the prompt file is local to that directory.
2. **Given** Kimi emits non-GBK characters, **When** the workflow captures output, **Then** output is decoded with UTF-8 replacement instead of crashing.

---

### User Story 3 - Prepare for Batch Extension (Priority: P3)

The one-student workflow stores machine-readable state so later batch grading can skip already completed students and retry only failed nodes.

**Why this priority**: Batch grading should be resumable and auditable before writing scores to the roster workbook.

**Independent Test**: Run the workflow twice with and without `--force` and confirm completed outputs are not accidentally overwritten unless requested.

**Acceptance Scenarios**:

1. **Given** final arbitration already exists, **When** the workflow runs without `--force`, **Then** it exits without re-grading.
2. **Given** final arbitration already exists, **When** the workflow runs with `--force`, **Then** it regenerates the CLI outputs and arbitration record.

---

[Add more user stories as needed, each with an assigned priority]

### Edge Cases

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right edge cases.
-->

- Evidence files may contain mojibake from earlier extraction. The workflow records what it read and does not fabricate missing content.
- A student may have no matched submissions. The workflow must allow a 0 score with evidence-based explanation.
- A CLI may return nonzero, time out, or produce very short output. The workflow must persist that failure.
- Codex CLI may fail. Without Codex arbitration, the workflow must mark the run incomplete.

## Requirements *(mandatory)*

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right functional requirements.
-->

### Functional Requirements

- **FR-001**: System MUST run Kimi CLI, agy CLI, and Codex CLI as distinct workflow nodes.
- **FR-002**: System MUST read `process-evidence.md` and `process-evidence.json` from the selected student directory when present.
- **FR-003**: System MUST write each CLI prompt to a local markdown file in the selected student directory.
- **FR-004**: System MUST launch each CLI with explicit working directory and UTF-8 environment variables.
- **FR-005**: System MUST enforce per-node timeouts and persist timeout or nonzero exit details.
- **FR-006**: System MUST write final arbitration as both Markdown and JSON.
- **FR-007**: System MUST skip a completed student unless the operator passes `--force`.
- **FR-008**: System MUST avoid writing to the student roster Excel during the one-student smoke test.

### Key Entities *(include if feature involves data)*

- **StudentEvidence**: Student directory, basic identity, process evidence markdown, optional evidence JSON, related images.
- **CliReview**: Reviewer name, prompt path, output path, exit code, timeout flag, raw text, parsed score if available.
- **ArbitrationResult**: Final process score, assignment scores, decision notes, source reviewer scores, completion status.

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable success criteria.
  These must be technology-agnostic and measurable.
-->

### Measurable Outcomes

- **SC-001**: One selected student can be processed end to end with five durable output files.
- **SC-002**: A missing-submission student produces a valid arbitration record instead of blocking.
- **SC-003**: Each CLI node has a bounded timeout visible in the output record.
- **SC-004**: Re-running without `--force` does not overwrite an existing final arbitration record.

## Assumptions

<!--
  ACTION REQUIRED: The content in this section represents placeholders.
  Fill them out with the right assumptions based on reasonable defaults
  chosen when the feature description did not specify certain details.
-->

- Existing evidence directories were created by the earlier extraction script.
- The smoke test uses one student and does not update the roster workbook.
- Full batch parallelism and Excel write-back are follow-up work after the smoke test.
- Kimi, agy, and Codex CLI authentication already exists on this machine.
