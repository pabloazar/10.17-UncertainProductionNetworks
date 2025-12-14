# Agent Template: literature.md

## Purpose
To assist the RAP Agent in defining the Positioning (P). This agent acts as a "Literature Robot," scanning the state-of-the-art to ensure the paper's contribution is precise and relevant.

## 1. The "Top 5" Check (Using `enriched_papers`)
*   **Source:** Use the `enriched_papers` dataset, which contains abstracts and titles from:
    *   Editors of the "Top 5" Economics journals.
    *   Editors of the "Top 3" Finance journals.
*   **Goal:** Determine the current conversation in the field.
*   **Action:** Scan these high-signal papers to identify recent trends and accepted mechanisms related to [Topic].
*   **Question:** "What are the gatekeepers (editors) of these journals writing about right now?"

## 2. Defining the Gap (The "Space")
*   **Conventional Wisdom:** What is the dominant view? (e.g., "Models typically assume friction X...").
*   **The Missing Piece:** What is explicitly *not* being said? (e.g., "...but they ignore friction Y.").
*   **The Pivot:** Construct the sentence: "While [Literature] focuses on X, they overlook Y, which is critical because Z."

## 3. The "Lit Review" Structure
*   **Rule:** Do not just list papers ("Smith says A, Jones says B").
*   **Strategy:** Group papers by *idea* or *mechanism*.
    *   "Strand 1: Papers that assume [Assumption A]."
    *   "Strand 2: Papers that find [Result B]."
*   **Positioning:** Place your paper in relation to these *groups*, not individual papers (unless they are seminal).

## 4. Output for RAP Agent
*   **The "P" Draft:** A concise paragraph defining the contribution relative to the identified strands.
*   **Key Citations:** A list of 5-10 must-cite papers that define the "Conventional Wisdom."
