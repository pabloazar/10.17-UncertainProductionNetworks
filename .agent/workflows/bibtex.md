---
description: Mine references from the paper and their references ("snowballing") to create a comprehensive BibTeX.
---

# BibTeX Mining Workflow

**Goal**: Create a rich `references.bib` by finding correct citations for papers mentioned in text and exploring their key influences.

## Steps

// turbo-all

1. **Extract References**:
   - Read the `paper.md` or `.tex` file.
   - Identify all citation keys or "Author (Year)" strings (e.g., "Acemoglu and Azar (2020)", "Van Zandt and Vives (2007)").

2. **Primary Search** (For each key reference):
   - Use `search_web` with query: `bibtex [Paper Title] [Author]`.
   - Extract the full BibTeX entry (Article, Journal, Year, Volume, Pages).

3. **Snowball Search** (References of References):
   - For the top 3 most central papers (e.g., the base model, the main theorem source):
     - Use `search_web` to find "References of [Paper Title]".
     - Identify 2-3 seminal papers cited by them that are relevant to the *current* paper's mechanism (e.g., specific lattice theory papers, supermodularity foundations).
     - Get their BibTeX.

4. **Compile Archive**:
   - Write all entries to `references.bib`.
   - Ensure no duplicates.

5. **Commit**:
    ```bash
    git add references.bib && git commit -m "Generated references.bib via recursive mining"
    ```
