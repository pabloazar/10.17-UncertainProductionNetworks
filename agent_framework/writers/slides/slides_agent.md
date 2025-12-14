# Agent Template: slides.tex

## Purpose
To translate the static research paper into a dynamic 60-minute seminar presentation. This agent manages the `.tex` Beamer code, ensuring the "Takeaway Headings" from the paper become the headlines of the slides.

## 1. Slide Deck Architecture
* **Structure:** Enforce the standard "Job Market Paper" flow:
    1. **The Hook (3 slides):** Motivation + The Puzzle.
    2. **The RAP (1 slide):** Question, Answer, Contribution (This slide must be memorizable).
    3. **Preview of Results (2 slides):** One graph + One simplified table.
    4. **The Model (variable length):** Setup $\to$ Mechanism $\to$ Key Proposition. (Skip proofs).
    5. **Empirics (variable length):** Data $\to$ ID Strategy $\to$ Results $\to$ Robustness.
    6. **Conclusion (1 slide):** Summary + Policy Implication.
* **Formatting Rule:** Use the `\usetheme{Metropolis}` or similar clean, modern Beamer theme. Avoid "walls of text."

## 2. Visual Translation Strategy
* **Text-to-Bullet:** Convert paragraph arguments from `paper.md` into 3-bullet hierarchies.
* **Math reduction:**
    * *Paper:* Full derivation of FOCs.
    * *Slides:* Show the Problem Maximization $\to$ Show the First Order Condition $\to$ Show the Intuition (arrow logic). Use `\underbrace{}` tags to explain terms in equations.
* **Figures:** Import figures directly from `illustrations.md` using `\includegraphics`. Ensure font sizes in TikZ figures match slide text size.

## 3. Table "Beautification" Protocol
* **Source:** Extract raw data/structure from `empirics.md` tables.
* **Transformation:** Do NOT copy-paste the full paper table.
    * **Focus:** Keep only the Main Regressor and Dependent Variable.
    * **Hide:** Group all controls into "Yes/No" rows (e.g., "Fixed Effects: Yes").
    * **Highlight:** Use `\alert{}` or `\textbf{}` to color the specific coefficient of interest that matches the slide's claim.
    * **Sizing:** Use `\resizebox{0.9\textwidth}{!}{...}` to ensure fit.
    * **Style:** Use `booktabs` (no vertical lines, distinct `\toprule`, `\midrule`, `\bottomrule`).

## 4. The "Slide 1" Check
* **Title Slide:** Must include the Title, Author, and a "Bottom Line Up Front" (BLUF) subtitle that summarizes the main result in plain English.
