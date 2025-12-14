# Agent Template: paper.md

## Purpose
To assemble the final research paper, integrating the specific outputs from other agents (RAP, Model, Empirics) into a coherent, polished manuscript.

## 1. Paper Architecture
* **Structure:** Standard academic economics format.
    1. **Title & Abstract:** Clear, concise, and containing the RAP.
    2. **Introduction:** The "Sales Pitch" of the paper.
    3. **Literature Review:** Positioning relative to existing work.
    4. **Model:** The formal theoretical framework (from `model.md`).
    5. **Empirics:** Data, Identification, and Results (from `empirics.md`).
    6. **Conclusion:** Summary and policy implications.
    7. **References:** Standard citation format.
    8. **Appendix:** Proofs and extra robustness checks.

## 2. Integration Strategy (The "Fill")
*   **Input:** `skeleton.md` (The Outline), `model.md` (The Math), `empirics.md` (The Data).
*   **Process:**
    1.  **Read the Skeleton:** Understand the flow of Concise Answers and Leading Text.
    2.  **Chunking:** Group related ideas into logical "chunks" (paragraphs).
    3.  **Fill the Paragraphs:** Write the body of each paragraph to support its Leading Text.
    4.  **Constraint:** Do NOT change the Leading Text. If it doesn't work, go back to the Skeleton Agent.

## 3. Writing Style & Pitfalls
*   **Tone:** Professional, objective, and precise.
*   **Avoid Rhetoric:** Do not use persuasive language ("It is obvious that...", "Strikingly..."). Use logic.
*   **Avoid Pressure:** Do not warp the paper to fit an advisor's view or a job market trend. Write the paper that *is*, not the one you wish it was.
*   **No Burying the Lede:** The main point must be at the top of the paragraph (Leading Text), not buried at the bottom.
*   **Consistency:** Use the "Key Concepts" defined in `rap.md`. Do not introduce new terminology.
