# Skeleton: Endogenous Production Networks under Uncertainty

---

# 1. Introduction
> **Takeaway:** We provide the first theory of endogenous production network formation under incomplete information, showing that extremal monotone equilibria exist and exhibit predictable comparative statics.

- **Para 1:** Firms choose their suppliers, but they do so under uncertainty about productivity—both their own and their partners'.
- **Para 2:** Existing theory addresses either network formation under complete information (Acemoglu-Azar) or abstract games under incomplete information (Van Zandt-Vives), but not their intersection.
- **Para 3:** We integrate these approaches by showing that CES production with complementary inputs generates the strategic complementarities that, combined with affiliated signals, guarantee extremal monotone equilibria.
- **Para 4:** Our main result establishes existence, uniqueness properties, and comparative statics: shocks to beliefs propagate through the network via complementarities.
- **Para 5:** The paper proceeds as follows: Section 2 sets up the environment, Section 3 derives strategic complementarities from CES production, Section 4 establishes the information structure, Section 5 proves the main existence result, Section 6 develops comparative statics, Section 7 extends to dynamics, and Section 8 concludes.

---

# 2. Environment
> **Takeaway:** We study a multi-firm production economy where each firm chooses its supplier set, quantities, and labor, while observing only a private signal about aggregate productivity.

## 2.1 Primitives
> **Takeaway:** Firms, states, and signals are the fundamental objects.

- **Para 1:** The economy consists of n firms, each producing a distinct good using labor and intermediate inputs from other firms.
- **Para 2:** An aggregate state μ governs productivity economy-wide; it follows a Markov process on a compact set.
- **Para 3:** Each firm observes a private signal about the state—the signal equals the state plus noise, where signals are affiliated across firms.

## 2.2 Technology
> **Takeaway:** Production follows a CES aggregator with an endogenous extensive margin: firms choose *which* inputs to use, not just *how much*.

- **Para 1:** Following Acemoglu and Azar (2020), each firm chooses a supplier set from a finite menu of options.
- **Para 2:** Output is a CES aggregate of labor and intermediate inputs, with productivity depending on the supplier set.
- **Para 3:** The elasticity of substitution σ parameterizes complementarity: when σ < 1, inputs are complements; when σ > 1, they are substitutes.

## 2.3 Payoffs and Strategies
> **Takeaway:** Firms maximize expected profits; strategies map private signals to supplier sets, input quantities, and labor.

- **Para 1:** Firm i's profit equals output revenue minus labor costs and input expenditures.
- **Para 2:** Output prices depend on the aggregate state; input prices are determined in equilibrium.
- **Para 3:** A strategy is a mapping from the firm's private signal (its type) to an action—a supplier set and input choice.

---

# 3. Strategic Complementarities from CES Production
> **Takeaway:** When inputs are complements (σ < 1), the CES technology generates strategic complementarities in supplier adoption: if others expand their networks, each firm's incentive to expand increases.

## 3.1 Supermodularity of the Production Function
> **Takeaway:** With σ < 1, the CES production function is supermodular in the joint choice of supplier set and input quantities.

- **Para 1:** Supermodularity requires non-negative cross-partial derivatives: raising one input should increase the marginal product of another.
- **Para 2:** We compute the cross-partial explicitly: for CES, it equals (1-σ)/σ times a positive term, which is positive precisely when σ < 1.
- **Para 3:** The discrete component—adding a supplier—also exhibits complementarity: adopting supplier j raises the marginal product of input k.
- **Para 4:** When σ > 1 (substitutes), the production function is submodular, strategic substitutes emerge, and our methods do not apply.

## 3.2 Single-Crossing in the Cost Function
> **Takeaway:** If expanding the supplier set is cost-reducing at high input prices, it remains cost-reducing at low prices—the technology-price single-crossing condition holds.

- **Para 1:** The unit cost function summarizes the technology's implications for optimal input choice.
- **Para 2:** Adding supplier k changes costs by α_k(P_k^{1-σ} - 1), which becomes more negative (more favorable) as P_k falls.
- **Para 3:** This single-crossing property—proved here, not cited—implies that lower input prices encourage network expansion.

## 3.3 Increasing Differences in Payoffs
> **Takeaway:** The profit function satisfies increasing differences in own action and others' actions, in own action and the state, and single-crossing in own action and type.

- **Para 1:** Increasing differences in (a_i, a_{-i}): When others expand networks, input prices fall, raising the return to own expansion via single-crossing.
- **Para 2:** Increasing differences in (a_i, μ): Higher productivity raises revenue multipliers, increasing the marginal benefit of larger supplier sets.
- **Para 3:** Single-crossing in (a_i, τ_i): Higher types—those with more optimistic beliefs—find expansion more attractive because they place more weight on high-μ states.

---

# 4. Information Structure and Affiliation
> **Takeaway:** Affiliated signals—a natural property of Gaussian information structures—generate the FOSD ordering of beliefs required for Van Zandt-Vives methods.

## 4.1 Affiliation: Definition and Implications
> **Takeaway:** Affiliation (log-supermodularity of the joint density) implies that higher signals induce FOSD-higher beliefs about both the state and other agents' signals.

- **Para 1:** Random variables are affiliated if their joint density satisfies f(z∨z')f(z∧z') ≥ f(z)f(z') for all z, z'.
- **Para 2:** Taking logs, this is equivalent to supermodularity of the log-density—a tractable condition.
- **Para 3:** Affiliation implies monotone likelihood ratio ordering of conditional distributions, which implies FOSD.

## 4.2 Affiliation in Gaussian Settings
> **Takeaway:** Gaussian signals with non-negative correlations are affiliated, providing a natural foundation for our information structure.

- **Para 1:** The log-density of a Gaussian vector is quadratic; its cross-partials equal negative entries of the precision matrix.
- **Para 2:** Affiliation requires the precision matrix to have non-positive off-diagonals.
- **Para 3:** A common factor model—signals equal the state plus independent noise—satisfies this condition.

## 4.3 From Affiliation to FOSD-Ordered Beliefs
> **Takeaway:** Under affiliation, higher own signals FOSD-shift beliefs about others' signals, enabling the application of Van Zandt-Vives.

- **Para 1:** By affiliation, Pr(μ > x | s_i) is increasing in s_i for all x—this is FOSD.
- **Para 2:** Similarly, the conditional distribution of s_{-i} given s_i is FOSD-increasing in s_i.
- **Para 3:** These FOSD orderings are the primitives required for Van Zandt-Vives' monotone equilibrium results.

---

# 5. Main Result: Existence of Extremal Monotone Equilibria
> **Takeaway:** Combining strategic complementarities (from CES) with FOSD-ordered beliefs (from affiliation), we prove that extremal Bayesian Nash equilibria exist and are monotone in type.

## 5.1 Van Zandt-Vives Conditions
> **Takeaway:** Six conditions must be verified: compact lattice actions, FOSD-ordered types, quasisupermodularity, single-crossing, increasing differences, and ascending best-replies.

- **Para 1:** Condition 1 (Lattice): The action space—a product of a finite set (suppliers) and compact intervals (quantities)—is a compact metrizable complete lattice.
- **Para 2:** Condition 2 (Type Order): Types are ordered by the FOSD relation on interim beliefs, inherited from the signal order under affiliation.
- **Para 3:** Conditions 3-5 (Supermodularity and ID): These follow from the CES production structure proved in Section 3.
- **Para 4:** Condition 6 (Best-Reply Properties): Compactness and continuity ensure non-empty best-reply correspondences; supermodularity ensures they are ascending.

## 5.2 Existence Theorem
> **Takeaway:** There exist a greatest and a least pure-strategy Bayesian Nash equilibrium, each in strategies monotone in type.

- **Para 1:** By Tarski's fixed-point theorem, the set of fixed points of an isotone map on a complete lattice is non-empty and itself a complete lattice.
- **Para 2:** The best-reply operator, constructed using extremal selections, is isotone under our conditions.
- **Para 3:** Iterating from the top (bottom) of the strategy lattice converges to the greatest (least) fixed point—the extremal equilibria.
- **Para 4:** Monotonicity in type follows from single-crossing: if a strategy is optimal for type τ, higher types prefer higher actions by single-crossing, so the extremal selections are monotone.

## 5.3 Discussion: Why Extremal Equilibria Matter
> **Takeaway:** Focusing on extremal equilibria provides selection (uniqueness up to bounds), robustness (preserved under perturbations), and tractable comparative statics.

- **Para 1:** Extremal equilibria are the natural focal points: they bound all other equilibria and are stable under best-reply dynamics.
- **Para 2:** They are robust to small perturbations in primitives—a property not shared by arbitrary equilibrium selections.
- **Para 3:** Comparative statics for extremal equilibria extend to all equilibria via the lattice structure.

---

# 6. Comparative Statics
> **Takeaway:** Shifts in beliefs and policy parameters move equilibrium networks monotonically: improvements in information (FOSD shifts) and reductions in adoption costs expand the supplier network.

## 6.1 Comparative Statics in Beliefs
> **Takeaway:** An FOSD improvement in interim beliefs increases both extremal equilibria.

- **Para 1:** When beliefs improve, single-crossing implies higher best-replies.
- **Para 2:** The extremal equilibria, as fixed points of isotone maps, inherit this monotonicity.
- **Para 3:** Economically: better news about productivity leads firms to adopt more suppliers.

## 6.2 Comparative Statics in Parameters
> **Takeaway:** Lower adoption costs, higher TFP, or reduced distortions expand equilibrium networks.

- **Para 1:** Let τ parameterize the technology such that higher τ increases payoffs to expansion.
- **Para 2:** By Topkis' theorem, the best-reply is monotone in τ.
- **Para 3:** The equilibrium, as a fixed point, inherits this monotonicity: σ(τ') ≥ σ(τ) for τ' > τ.

---

# 7. Dynamic Extension
> **Takeaway:** The static results extend to a dynamic Markov game: Bayesian Markov perfect equilibria exist, and transition paths are ordered in initial conditions.

## 7.1 The Dynamic Game
> **Takeaway:** Firms solve a Bellman equation where the state includes the inherited network and the current productivity shock.

- **Para 1:** The network evolves according to a transition function that depends on the previous network and current choices.
- **Para 2:** The Bellman operator maps value functions to value functions; its argmax gives the optimal policy.
- **Para 3:** Payoffs retain increasing differences; the transition preserves FOSD when the law of motion is isotone.

## 7.2 Existence of Markovian Equilibria
> **Takeaway:** Extremal Bayesian Markov perfect equilibria exist and are monotone in both state and type.

- **Para 1:** The period-by-period analysis of Section 5 applies to each stage game.
- **Para 2:** Backward induction preserves the lattice structure: extremal value functions are well-defined.
- **Para 3:** The limiting stationary equilibrium inherits monotonicity and extremality.

## 7.3 Monotone Transitional Dynamics
> **Takeaway:** Starting from a higher initial state, the economy follows a uniformly higher transition path to steady state.

- **Para 1:** By induction: higher initial state implies higher actions by comparative statics.
- **Para 2:** Higher actions imply a higher successor state via the isotone law of motion.
- **Para 3:** The induction propagates: the entire path is ordered.

---

# 8. Conclusion
> **Takeaway:** We have established theoretical foundations for production network formation under uncertainty, with applications to supply chain policy and resilience.

- **Para 1:** This paper introduced private, heterogeneous information into the analysis of endogenous production networks.
- **Para 2:** By establishing that CES production with complementary inputs satisfies Van Zandt-Vives conditions, we proved existence of extremal monotone equilibria.
- **Para 3:** Our comparative statics show how information shocks and policy interventions propagate through the network.
- **Para 4:** Extensions to dynamics provide a framework for analyzing supply chain formation over time.
- **Para 5:** Several extensions merit further study: heterogeneous information structures, flexible CES nesting, and empirical applications to supply chain data.

---

# Appendix A: Proofs
> **Takeaway:** All proofs are provided in full, deriving conditions from primitives rather than citing results as black boxes.

## A.1 Proof of Proposition 1 (CES Supermodularity)
## A.2 Proof of Proposition 2 (Single-Crossing)
## A.3 Proof of Proposition 3 (Increasing Differences)
## A.4 Proof of Proposition 4 (Affiliation → FOSD)
## A.5 Proof of Proposition 5 (Gaussian Affiliation)
## A.6 Proof of Theorem 1 (Existence)
## A.7 Proof of Theorem 2 (Comparative Statics)
## A.8 Proof of Theorem 3 (Dynamic Extension)

---
*Skeleton created: 2025-12-14*
