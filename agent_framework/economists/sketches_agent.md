# Agent Template: sketches.md

## Purpose
To visualize the core economic mechanism and define the logical flow of the argument without the burden of formal notation. This file is the blueprint for the formal model.

## 1. Conceptual Market Structure
* **Environment:** (e.g., Search market, Auction, OLG, Production network)
* **Agents:** List the key players. (e.g., "Risk-averse firms," "Naive consumers").
* **Goods/Assets:** What is being traded or produced?
* **Frictions:** What prevents the First Best outcome? (e.g., Asymmetric info, search costs, limited commitment).

## 2. Timing & Sequence (The "Game")
* **Timeline:** [t=0] -> [t=1] -> [t=2]
    * *Draft a visual timeline or numbered list of who moves when.*
* **Action Space:** What choices does each agent make at each node?

## 3. Information Structure (Bayesian)
*   **Prior Beliefs:** What each agent believes about relevant unknown states of the world *ex ante*.
    *   Agent A's prior: $P(\theta)$
    *   Agent B's prior: $P(\theta)$
*   **Signals:** What information agents observe that might influence their beliefs.
    *   Agent A observes: $s_A \sim F(s_A | \theta)$
    *   Agent B observes: $s_B \sim F(s_B | \theta)$
*   **Belief Updating:** How agents update their beliefs after observing signals, using Bayes' Rule.
    *   Agent A's posterior: $P(\theta | s_A)$
    *   Agent B's posterior: $P(\theta | s_B)$
*   **Who knows what?**
    *   Agent A knows: { ... }
    *   Agent B knows: { ... }
*   **When is uncertainty resolved?**
    *   Agent A resolves uncertainty: $t_A$
    *   Agent B resolves uncertainty: $t_B$

## 4. Intuitive Equilibrium
* **Incentives:** What is the primary trade-off for the key agent? (e.g., "The firm balances the marginal benefit of cheating against the marginal cost of reputation loss.")
* **The Mechanism:** Draw a "Box-and-Arrow" diagram:
    * [Exogenous Shock] -> [Changes Incentives] -> [Agent Action] -> [Equilibrium Outcome]
* **Market Clearing Logic:** How do supply and demand meet conceptually?

## 5. Key Prediction (The Hypothesis)
* **Comparative Static (Intuition):** If we increase Parameter X (e.g., interest rate), what happens to Outcome Y?
* **Stylized Fact Match:** Does this intuition match the primary observed fact in `rap.md`?
    * *Check:* If X goes up, does Y go up?
