# Agent Template: model.md

## Purpose
To provide the rigorous mathematical foundation of the paper. All variables must be defined, all assumptions explicit, and all results proven.

## 1. Model Setup (The Environment)
* **Market Structure:** Define preferences ($U$), technology ($F$), and endowments explicitly using LaTeX.
* **Timing:** Formal $t=0, 1, ..., T$ sequence of events.
* **Information Sets:** Define $\mathcal{I}_{i,t}$ for each agent $i$ at time $t$.
    *   **Bayesian Structure:** Explicitly define Priors, Signals/Evidence, and Posteriors.
    *   **Updates:** Specify how information evolves (e.g., Bayes' Rule).
* **Budget Constraints:** Write out the budget constraint for every agent.

## 2. Agent Optimization
* **Problem Statement:**
    $$\max_{\{c_t\}} \mathbb{E} \sum \beta^t u(c_t) \quad \text{s.t.} \quad \dots$$
* **First Order Conditions (FOCs):** Derive the Euler equations or optimality conditions.
* **Key Lemmas:** Simplify the optimization (e.g., "Optimal contracts take linear form").

## 3. Equilibrium Definition
* **Concept:** (e.g., Perfect Bayesian Equilibrium, Recursive Competitive Equilibrium).
* **Conditions:**
    1. Agents optimize given prices/beliefs.
    2. Beliefs are consistent (Bayes' rule).
    3. Markets clear: $\int x_i di = S$.
* **Fixed Point:** Express the equilibrium as a fixed point of a mapping (if applicable).

## 4. Solution & Characterization
* **Existence/Uniqueness:** (Brief statement or proof).
* **Closed Form (if possible):** $$P^* = \frac{\alpha}{\beta} ...$$
* **Proposition 1 (Main Result):** The core theoretical finding regarding the mechanism.
* **Proof:** [Link to Appendix or write inline if short]

## 5. Comparative Statics
* **Derivations:** Calculate signs of derivatives $\frac{\partial Y^*}{\partial \theta}$.
    * Effect of [Parameter 1] on [Outcome].
    * Effect of [Parameter 2] on [Outcome].
* **Proposition 2 (Testable Implications):** Formal statements of how observables co-move.

## 6. Mapping to Empirics (The Handshake)
* **Table: Theory vs. Data**
    | Model Parameter ($\theta$) | Empirical Proxy | Predicted Sign | Observed Sign (from `empirics.md`) |
    | :--- | :--- | :--- | :--- |
    | Risk Aversion | VIX | Positive | Positive |
    | Info Friction | Bid-Ask Spread | Negative | Negative |
* **Discussion:** Specific instructions on how to estimate structural parameters or reduce form equations based on the FOCs.
