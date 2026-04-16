# Fleet: lecture5-rewrite
Started: 2026-04-14T21:00:00

## Progress
- [x] Step 1: Research Remotion latest features (gemini) - DONE (v4.0.448, npx create-video@latest, core APIs confirmed)
- [x] Step 2: Research Remotion real-world cases (gemini) - DONE (rate limited, used cached knowledge + step 1 results)
- [x] Step 3: Research AI video tools comparison (gemini) - DONE (detailed Remotion vs AI model comparison obtained)
- [x] Step 4: Write full lecture document (self) - DONE
- [x] Step 5: Review lecture quality (self) - DONE

## Key Decisions
- Lecture restructured around "素材 vs 组装" framing per user feedback
- Section 2 dedicated to Remotion vs AI video model comparison (new, not in original)
- Format aligned with lectures 1-3 (教学目标→课时安排→详细内容→板书→注意事项)
- Removed "多元视角提醒" section (moved relevant content inline) to make room for comparison section

## Gemini Issues
- gemini CLI syntax: `-p "prompt"` not `-p --approval-mode yolo "prompt"`
- Rate limited (429) on first attempt, succeeded on retry
- Step 2 hit rate limit, fallback to self
