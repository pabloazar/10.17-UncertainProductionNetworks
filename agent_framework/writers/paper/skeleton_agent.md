# Agent Template: skeleton.md

## Purpose
To bridge the gap between the high-level RAP and the final prose. This agent creates the "Skeleton" of the paper—a structural outline that ensures logical coherence and narrative flow *before* any paragraphs are written.

## 1. The Three-Layer Approach
The writing process follows a strict hierarchy:
1.  **RAP:** The core identity (Question, Answer, Contribution).
2.  **Skeleton:** The logical structure (Titles, Takeaways, Topic Sentences).
3.  **Prose:** The content filling the paragraphs (executed by `paper.md`).

## 2. Skeleton Components
For every section and subsection, the Skeleton must define:

### A. Headings and Subheadings ONLY
*   **Rule:** The skeleton is *just* the hierarchy of titles.
*   **Test:** If a reader sees ONLY these headings, can they infer the entire argument?

### B. The Concise Answer (The Takeaway)
*   **Definition:** The single most important message the reader must retain from this section.
*   **Criteria:** Must be a complete sentence. No "fluff."
*   **Location:** This answers the "Logical Question" raised by the section title.

### C. Leading Text (Topic Sentences)
*   **Definition:** The first sentence of each paragraph.
*   **Criteria:**
    *   **No Burying the Lede:** The sentence must state the paragraph's conclusion or main point immediately.
    *   **Flow:** Reading the topic sentences in order must yield a smooth, grammatical, and persuasive narrative.
    *   **Rhyming:** Use consistent "Key Concepts" (defined in `rap.md`) throughout.

## 3. The "Skim Test"
The Skeleton is successful ONLY if a reader can understand the entire paper's argument solely by reading the **Concise Answers** and **Leading Text**.

## 4. Output Format
```markdown
# [Section Title]
> **Takeaway:** [The one-sentence takeaway for this section.]

## [Subsection Title]
> **Takeaway:** [The one-sentence takeaway for this subsection.]

*   **Para 1:** [Topic Sentence]
*   **Para 2:** [Topic Sentence]
*   **Para 3:** [Topic Sentence]
```
