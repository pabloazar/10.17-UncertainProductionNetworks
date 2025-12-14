---
description: Send paper to LLM reviewers and parse feedback
---

# Math Review Workflow

Automated review cycle: compile → send to reviewers → parse feedback → apply fixes.

## Usage
```
/math-review
```

## Steps

// turbo-all

1. Compile LaTeX to ensure it builds:
```bash
pdflatex -interaction=nonstopmode new_draft_2.tex
```

2. Generate latexdiff against original (for context):
```bash
git show 1c3a315:new_draft_2.tex > /tmp/original_draft.tex && latexdiff /tmp/original_draft.tex new_draft_2.tex > new_draft_2_diff.tex
```

3. Send to LLM reviewers (Claude Opus 4.5 + Grok):
```bash
python3 scripts/send_followup_review.py
```

4. Wait for reviews to complete and read feedback:
- Read `followup_review_claude_opus_deepthink.md`
- Read `followup_review_super_grok.md`

5. Summarize feedback with priority ranking:
- **Fatal errors**: Must fix before next round
- **Moderate issues**: Should fix
- **Minor issues**: Can defer

6. For each fatal error:
- Apply fix to `new_draft_2.tex`
- Verify compilation

7. Commit fixes:
```bash
git add new_draft_2.tex && git commit -m "Address reviewer feedback: [summary]"
```

8. If fatal errors were fixed, loop back to step 1 for another round.

## Output
- Updated `followup_review_claude_opus_deepthink.md`
- Updated `followup_review_super_grok.md`
- Fixed `new_draft_2.tex` (committed)
- Updated `new_draft_2_diff.pdf` (redline)

## Notes
- Prioritize Claude feedback over Grok when in conflict
- Maximum 5 rounds before asking user for direction
