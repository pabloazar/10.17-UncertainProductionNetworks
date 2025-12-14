---
description: Generate a redlined PDF showing changes from a git commit
---

# Redline Workflow

Generate a latexdiff PDF comparing the current draft against a previous git commit.

## Usage
```
/redline [commit_ref]
```
Default commit_ref is `HEAD~1` (previous commit). Use `1c3a315` for the original baseline.

## Steps

// turbo-all

1. Save the old version from git:
```bash
git show {commit_ref}:new_draft_2.tex > /tmp/old_draft.tex
```

2. Generate the latexdiff:
```bash
latexdiff /tmp/old_draft.tex new_draft_2.tex > new_draft_2_diff.tex
```

3. Compile the diff to PDF:
```bash
pdflatex -interaction=nonstopmode new_draft_2_diff.tex
```

4. Open the PDF (optional):
```bash
open new_draft_2_diff.pdf
```

## Output
- `new_draft_2_diff.tex` - LaTeX source with track changes markup
- `new_draft_2_diff.pdf` - Compiled PDF with additions in blue and deletions struck through
