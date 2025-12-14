# Agent Template: research_log.md

## Purpose
To serve as a "Lab Notebook" for the Discovery Phase. This agent manages the rapid, iterative loop of generating simplified theories and testing them with simplified data to validate the Core Testable Hypothesis.

## 1. The Loop Protocol
For each iteration, record the following:

### A. The Hypothesis
*   **Question:** "What specific sub-question are we testing right now?"
*   **Prediction:** "If our mechanism is true, we should see X."

### B. The Simplified Theory (Toy Model)
*   **Goal:** Generate the prediction with the *minimum* math possible.
*   **Action:** Write down a 2-equation model or a simple decision tree.
*   **Result:** Does the toy model actually generate the prediction? (Yes/No).

### C. The Simplified Empirics (Quick Check)
*   **Goal:** Check if the data is consistent with the prediction.
*   **Action:** Generate a scatter plot, a histogram, or a simple correlation coefficient.
*   **Constraint:** Do NOT run complex regressions yet. Look at the raw data.
*   **Result:** Does the plot look like the prediction? (Yes/No).

### D. The Decision
*   **Verdict:** Supported / Rejected / Inconclusive.
*   **Next Step:**
    *   If Supported: Move to the next implication or proceed to Phase 2.
    *   If Rejected: Modify the `rap.md` (Mechanism) or the `sketches.md`.
    *   If Inconclusive: Propose a better test.

## 2. The Log Format
Maintain a reverse-chronological log of these experiments.

```markdown
## [Date] - Experiment #N
*   **Hypothesis:** ...
*   **Toy Model:** ...
*   **Quick Check:** [Insert Plot]
*   **Verdict:** ...
```

## 3. Exit Criteria
You are done with this agent when you have **one** Toy Model and **one** Quick Check that strongly support the **Core Testable Hypothesis** defined in `rap.md`.
