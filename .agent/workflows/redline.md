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
git show {commit_ref}:AAVZ_Bayesian_SupplyChains.tex > /tmp/old_draft.tex
```

2. Generate the latexdiff:
```bash
latexdiff /tmp/old_draft.tex AAVZ_Bayesian_SupplyChains.tex > AAVZ_Bayesian_SupplyChains_diff.tex
```

3. Compile the diff to PDF:
```bash
pdflatex -interaction=nonstopmode AAVZ_Bayesian_SupplyChains_diff.tex
```

4. Open the PDF (optional):
```bash
open AAVZ_Bayesian_SupplyChains_diff.pdf
```

## Output
- `AAVZ_Bayesian_SupplyChains_diff.tex` - LaTeX source with track changes markup
- `AAVZ_Bayesian_SupplyChains_diff.pdf` - Compiled PDF with additions in blue and deletions struck through
