# Agent Template: pitch.tex

## Purpose
To create an extremely concise (5-slide, 5-minute) presentation that communicates the core concept, its importance, and its "so-what." This deck contains **zero** mathematical notation and **at most one** key empirical chart.

## 1. Slide Deck Architecture
* **Rule:** A strict 5-slide structure. One minute, one core idea per slide.
* **Format:** Use `\usetheme{Metropolis}` or similar. Font size must be large. Each slide must have a clear "Takeaway Heading."

## 2. The 5-Slide Structure

### Slide 1: The Problem
* **Headline:** "The Puzzle: [State the puzzle in plain English]"
* **Content:** A real-world, relatable question (e.g., "Why are gas prices high?").
* **Visual:** A powerful, full-slide image (e.g., a photo of a gas station).

### Slide 2: The "Old" Answer
* **Headline:** "The Conventional Wisdom is [X]"
* **Content:** The common explanation for the puzzle (this is your "P" from `rap.md`).
* **Visual:** A simple text box or a "common knowledge" icon.

### Slide 3: Our Answer (The New Mechanism)
* **Headline:** "But the Real Story is [Y]"
* **Content:** Your "A" from `rap.md`, explained as a logical story.
* **Visual:** A *highly* simplified version of your `sketches.md` diagram (e.g., 3 boxes, 2 arrows).

### Slide 4: The "So-What" (The Killer Fact)
* **Headline:** "How We Know This is True"
* **Content:** The *one* piece of evidence that makes your case.
* **Visual:** The single most compelling chart from `empirics.md` (no table). The axes must be clearly labeled in plain English.

### Slide 5: The Takeaway
* **Headline:** "Why This Matters"
* **Content:** The one-sentence summary of your contribution and its implication for policy or the field.
* **Visual:** A simple text slide or a relevant icon (e.g., a "policy" icon).

## 3. Translation Strategy
* **Jargon:** Zero tolerance.
* **Math:** Zero tolerance.
* **Tables:** Zero tolerance.
* **Text:** Maximum 3 bullet points per slide.
* **Focus:** The Orchestrator will extract the "R," "A," and "P" from `rap.md` and the most compelling visual from `sketches.md` or `empirics.md` to build this deck. The primary goal is to make the audience *understand* and *remember* the idea.
