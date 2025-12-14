# Skeleton: Endogenous Production Networks under Uncertainty

---

# 1. Introduction
> **Takeaway:** We provide a theory of production networks where opaque supply chains and private risk signals create an information multiplier, amplifying shocks through strategic complementarities.

- **Para 1:** Supply chains are opaque webs of trust. Firms invest in suppliers based not on perfect knowledge, but on private signals—news, rumors, local conditions.
- **Para 2:** As supply chains grow more complex (Acemoglu & Azar, 2020) and volatile (Taschereau-Dumouchel et al., 2024), this "inference problem" becomes central. One missing chip halts an assembly line; one rumor of insolvency freezes credit.
- **Para 3:** We model this by combining endogenous network formation with dispersed, affiliated information. Firms receive correlated private signals about aggregate productivity.
- **Para 4:** Our key mechanism: when inputs are complements ($\sigma < 1$), information is also a complement. "Good news" encourages expansion, which (due to correlated signals) coincides with others expanding, creating a "sentiment multiplier."
- **Para 5:** We prove the existence of extremal monotone equilibria—robust configurations where optimism breeds density—and show how opacity amplifies the network's response to shocks.

---

# 2. Environment and Information
> **Takeaway:** We study an economy where firms choose suppliers under CES technology while observing private, affiliated signals about aggregate productivity.

## 2.1 Technology and Payoffs
> **Takeaway:** Output is produced via an endogenous supplier set and complementary inputs; payoffs depend on the realized state.

- **Para 1:** Primitives: $n$ firms, aggregate state $\mu$, CES production with elasticity $\sigma < 1$ (complements).
- **Para 2:** Following A&A, firms choose a supplier set $S_i$ from a menu, then optimize continuous inputs.
- **Para 3:** Payoffs are profit-based; productivity $\theta_i(\mu)$ is state-dependent.

## 2.2 Information Structure
> **Takeaway:** Firms observe private signals that are "affiliated"—a natural statistical property implying good news is positively correlated across agents.

- **Para 1:** Information is dispersed: $s_i = h(\mu) + \varepsilon_i$. No firm sees the true state.
- **Para 2:** We assume signals are **affiliated** (log-supermodular density). This captures the idea that "my good news makes it likely you also got good news."
- **Para 3:** This implies two critical properties (proven in Appendix): signals induce FOSD-ordered beliefs about the state, and FOSD-ordered beliefs about *others'* signals.

---

# 3. Equilibrium with Strategic Complementarities
> **Takeaway:** The combination of technological complementarity and affiliated information guarantees the existence of extremal monotone equilibria, where "optimistic" firms build denser networks.

## 3.1 Lemmas: The Geometry of Payoffs
> **Takeaway:** (Auxiliary) The CES technology generates supermodular payoffs and single-crossing conditions that align incentives for expansion.

- **Para 1:** **Lemma 1 (Supermodularity):** With $\sigma < 1$, adding a supplier raises the marginal product of other inputs.
- **Para 2:** **Lemma 2 (Single-Crossing):** If a network is profitable at high prices, it is even more profitable at low prices (A&A result).
- **Para 3:** **Lemma 3 (Information Complementarity):** Higher signals make expansion more attractive (direct effect) and make it likely others expand (indirect effect).

## 3.2 Existence of Extremal Equilibria
> **Takeaway:** (Main Result) A greatest and least Bayesian Nash equilibrium exist, and they are monotone in type.

- **Para 1:** The game satisfies the conditions of Van Zandt and Vives (2007): compact lattice actions and supermodular payoffs.
- **Para 2:** **Theorem 1:** There exist extremal equilibria $\bar{\sigma}$ and $\underline{\sigma}$ where strategies are increasing in signal.
- **Para 3:** This resolves the "infinite regress" of beliefs: we don't need to track the hierarchy of beliefs, only the monotone ordering of strategies.

---

# 4. Comparative Statics
> **Takeaway:** Improvements in the "news" (FOSD shifts) or reductions in friction propagate through the network, expanding connectivity.

## 4.1 The Information Multiplier
> **Takeaway:** A positive shift in the signal distribution expands the network more than the direct effect alone would predict.

- **Para 1:** **Theorem 2:** If interim beliefs shift upward (FOSD), the equilibrium network expands.
- **Para 2:** Mechanism: Direct effect (I am more optimistic) + Strategic effect (I believe you are more optimistic and will expand, lowering my costs).
- **Para 3:** This creates an "information multiplier" where small shifts in sentiment can trigger large reorganizations.

## 4.2 Policy and Technology
> **Takeaway:** Reducing adoption costs or increasing TFP has similar multiplier effects.

- **Para 1:** **Theorem 3:** Lower fixed costs or higher productivity parameters shift extremal equilibria upward.
- **Para 2:** Applications: Subsidizing digital supply chain adoption or reducing trade barriers.

---

# 5. Dynamic Extension
> **Takeaway:** In a dynamic setting, these forces generate persistent "regimes" of high or low network density.

- **Para 1:** We extend the model to infinite horizon where network formation is sticky (state variable $A_{t-1}$).
- **Para 2:** **Theorem 4:** Bayesian Markov Perfect Equilibria exist and are monotone in the state.
- **Para 3:** Transition dynamics: A high initial network (or good shock) puts the economy on a higher trajectory, illustrating hysteresis.

---

# 6. Conclusion
> **Takeaway:** By treating information as a fundamental input with complementarity, we explain how opacity and sentiment drive supply chain fragility.

- **Para 1:** Real-world supply chains are driven by imperfect signals.
- **Para 2:** We provided the first tractible theory of this, showing how "affiliated opacity" + "technological complementarity" = "fragile monotone equilibria."
- **Para 3:** Implication: Policy should focus not just on physical capacity, but on information transparency to dampen the multiplier.

---

# Appendix: Proofs
> **Takeaway:** Detailed derivation of all Lemmas and Theorems.
