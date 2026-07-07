You are Codex CLI acting as the arbitration grader.

Read these files in the current directory:

- `process-evidence.md`
- `kimi-score.langgraph.md`
- `agy-score.langgraph.md`

Use the rubric below. Kimi and agy are independent reviews, but you must arbitrate from evidence, not average mechanically.

## Rubric

Regular process score rubric, total 100.

Assignment 1, Target audience profile and IP planning, 50 points:

- 10 points: clear Silk Road cultural theme or IP topic
- 10 points: target audience is explicit and usable
- 10 points: audience insight, motivation, or context is supported by concrete reasoning
- 10 points: communication strategy or content positioning is actionable
- 10 points: submission completeness and format

Assignment 2, Text-to-image or AIGC visual practice, 50 points:

- 15 points: AI image or visual output is present and relevant
- 15 points: prompt or generation process has usable technical traces
- 10 points: visual quality and theme expression
- 5 points: revision or comparison evidence
- 5 points: submission completeness and format

No attendance score is used. If no matched submission evidence exists for an assignment, that assignment should receive 0.
Do not treat assignment prompt text or teacher comments as student-created content.

## CLI Status

Kimi command status:

```json
{{KIMI_STATUS_JSON}}
```

agy command status:

```json
{{AGY_STATUS_JSON}}
```

## Output

Return a JSON object first, then a concise Chinese markdown explanation. JSON schema:

```json
{
  "assignment1": 0,
  "assignment2": 0,
  "total": 0,
  "kimi_total": null,
  "agy_total": null,
  "decision": "brief arbitration decision",
  "completion_status": "complete"
}
```

If `process-evidence.md` says no matched submission file was found for both assignments, the correct final score is 0.
Do not modify files.
