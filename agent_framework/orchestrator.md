# Economist-in-the-Loop: A Two-Phase Research Workflow

## Purpose
This document outlines a two-phase workflow for economics research. The process is designed to validate a paper's core idea before committing to full production. The system is managed by an Orchestrator (Gemini) in collaboration with the Economist (User).

---

## The Two Phases

### 1. Phase 1: Discovery
* **Goal:** To validate a core research idea and its central mechanism.
* **Process:** Iterative. Theory, empirics, and writing are co-developed in a single `research-LOG.md` to rapidly test the central argument.
* **Output:** A validated `rap.md` (Question, Answer, Positioning) and a core result. A "Go/Kill" decision is made.

### 2. Phase 2: Production
* **Goal:** To build a complete, robust paper based on the validated idea from Phase 1.
* **Process:** Systematic and linear. The model is formalized, empirical tests are expanded, and the final paper is written.
* **Output:** A polished `paper.md` ready for submission.

---

## Interaction Modes
The Economist can direct the Orchestrator to use either mode.

### 1. Dialogue Mode (Default)
* **Description:** High-interaction. The Orchestrator performs one small task (e.g., drafts one paragraph, proposes one test) and waits for the Economist's input and approval before proceeding.
* **Use Case:** Initial idea generation, strategic planning, and interpretation of results.

### 2. RA Mode (On-Demand)
* **Description:** Low-interaction. The Economist provides a specific, time-boxed objective (e.g., "Run robustness checks for 8 hours" or "Formalize the model based on the log").
* **Use Case:** Executing well-defined tasks. The Orchestrator works autonomously and provides a summary report upon completion.

---

# Project Workflow
This section details the step-by-step research pipeline, managed by the Orchestrator.

## Phase 1: Discovery
**Goal:** Find and validate a "Minimal Viable Paper."

### Step 0: Literature Review (The "Space")
* **Files:** `writers/paper/literature_review.md` (optional output)
* **Data Source:** `enriched_papers` (Abstracts/Titles from Top 5 Econ / Top 3 Finance Editors).
* **Agent:** `writers/paper/literature_agent.md`
* **Process:** The Literature Agent scans the `enriched_papers` to identify the "Conventional Wisdom" and the "Missing Piece."
    *   **Output:** A draft "P" (Positioning) and key citations for the RAP Agent.

### Step 1: Define RAP
* **Files:** `writers/paper/rap.md`
* **Agent:** `writers/paper/rap_agent.md`
* **Process:** The Orchestrator and Economist define R, A, and P.
    *   **Constraint:** Must pass the "Three Logical Checks" (Space for R, A answers R, A answers Idle Question).

### Step 2: Create Conceptual Sketch
* **Files:** `economists/sketches.md`
* **Process:** Create a conceptual diagram (e.g., box-and-arrow, timeline) that illustrates the core mechanism ("A").

### Step 3: Draft Introduction (The Sales Pitch)
* **Files:** `writers/paper/paper-INTRO-DRAFT.md`
* **Agent:** `writers/paper/rap_agent.md`
* **Process:** Draft the intro using the RAP Agent's structure.

### Step 3.5: The "Getting Good Feedback" Checklist
*   **Goal:** Verify the Argument, Structure, and Paragraphs.

### Step 4: Iterative Testing (Loop)
* **Files:** `research-LOG.md`
* **Agent:** `economists/research_log_agent.md`
* **Process:** Rapidly iterate on simplified theory and empirics.

### Phase 1 Exit Criteria
A "Go/Kill" decision is made.

---

## Phase 2: Production
**Goal:** Build the complete, robust paper.

### Step 5: Formalize the Model
* **Files:** `economists/model.md`
* **Process:** Formal production-grade model.

### Step 6: Execute the Empirical Strategy
* **Files:** `economists/empirical.md`
* **Process:** Full empirical analysis (Data, Facts, OLS, IV).

### Step 7: Reconcile & Extend
* **Files:** `economists/model.md`, `economists/empirical.md`
* **Process:** Extensions and heterogeneity.

### Step 8: Create the Skeleton
* **Files:** `writers/paper/skeleton.md`
* **Agent:** `writers/paper/skeleton_agent.md`
* **Process:** Define Headings, Concise Answers (Takeaways), and Leading Text (Topic Sentences).
    *   **Constraint:** Headings ONLY must reveal the argument.

### Step 9: Polish & Integrate (The "Fill")
* **Files:** `writers/paper/paper.md`, `writers/paper/illustrations.md`
* **Agent:** `writers/paper/paper_agent.md`
* **Process:** Fill the paragraphs implied by the Leading Text.
    *   **Constraint:** Do NOT change the Leading Text.

### Step 9.5: The Pitfalls Check
*   **Goal:** Ensure the paper is logical, not rhetorical.
*   **Checklist:**
    1.  **Rhetoric:** Are there persuasive words ("obviously", "crucially")? Remove them.
    2.  **Pressure:** Does the paper feel warped to fit an advisor's view?
    3.  **Burying the Lede:** Is the main point of any paragraph buried at the bottom? Move it to the top.
    4.  **Inconsistency:** Are terms used consistently?

### Step 10: Slides & Pitch
*   **Files:** `writers/slides/slides.tex`, `writers/slides/pitch.tex`
*   **Agents:** `writers/slides/slides_agent.md`, `writers/slides/pitch_agent.md`
*   **Process:** Create the presentation materials.

### Step 11: Submission & Reflection
* **Files:** `writers/paper/submission.md`
* **Process:** Finalize abstract, cover letter, and reflection.
