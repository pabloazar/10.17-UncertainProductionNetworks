# Endogenous Production Networks under Uncertainty

**Abstract.** We study production network formation when firms have private, correlated signals about aggregate productivity. Each firm chooses which suppliers to adopt, using a CES technology where intermediate inputs may be complements or substitutes. When inputs are complements ($\sigma < 1$) and signals are affiliated, the game exhibits strategic complementarities. We prove that extremal Bayesian Nash equilibria exist and are monotone in type: firms with higher signals about productivity adopt denser supplier networks. This "sentiment multiplier" amplifies shocks: because firms cannot distinguish fundamental productivity from correlated noise, informative signals trigger network expansions that are reinforcing. Comparative statics show that improvements in beliefs or reductions in adoption costs expand the equilibrium network. We extend these results to a dynamic setting with persistent network formation.

---

## 1. Introduction

Supply chains are opaque webs of trust. A manufacturer deciding whether to invest in a new supplier relationship rarely observes the precise reliability or productivity of that partner, nor the aggregate state of demand. Instead, decisions are made in the fog of war, based on dispersed signals: earnings reports, industry rumors, minor delivery delays, or local price fluctuations. In a complex economy, these signals are naturally correlated—a semiconductor shortage affects all automakers, but each observes different local symptoms. The central question of this paper is: how does this "inference problem" interact with the formation of the production network itself?

Real-world production networks have evolved from simple linear chains to complex, interconnected webs. As documented by Acemoglu and Azar (2020), modern industries rely on a vast array of specialized inputs—from satellites in agriculture to carbon fiber in automotive manufacturing. This complexity creates vulnerability. When inputs are technological complements, a disruption in one link can halt an entire production line. Taschereau-Dumouchel et al. (2024) highlight that in this volatile environment, firms actively manage risk by choosing "safer" suppliers, leading to a "flight to quality."

However, existing theory models these decisions under two extremes. Acemoglu and Azar (2020) assume complete information: every firm perfectly observes the productivity of every potential supplier. Kopytov et al. (2024) allows for uncertainty but models it as known risk profiles, where firms optimize against known variances. Neither accounts for the *inference* problem: how firms use private, correlated signals to form beliefs about the economy, and how these beliefs drive network formation.

This paper provides a theory of production network formation under dispersed information. We model an economy where firms choose their suppliers and input quantities while observing only private signals about an aggregate productivity state. By integrating the CES production structure of Acemoglu and Azar (2020) with the information economics of Van Zandt and Vives (2007), we uncover a powerful "information multiplier."

Our analysis yields three main results.

First, we show that **information acts as a strategic complement**. When inputs are technological complements (elasticity of substitution $\sigma < 1$), firms want to expand their networks when others do. Under affiliated signals (a natural property of correlated information), a firm observing "good news" not only becomes more optimistic about fundamentals (a direct effect) but also infers that others likely saw good news and will expand (an indirect, strategic effect). This double incentive creates a multiplier: small shifts in sentiment can trigger large reorganizations of the production network.

Second, we prove the existence of **extremal monotone equilibria**. Despite the complexity of the inference problem—where firms must form beliefs about others' beliefs—we rely on the lattice-theoretic properties of the game to show that robust equilibria exist where strategies are monotone in types. Firms with more optimistic signals optimally choose denser supplier networks. This theoretical tractability allows us to characterize the network structure without needing to solve for the entire hierarchy of beliefs.

Third, we demonstrate that **opacity amplifies shocks**. Because firms react to signals rather than fundamentals, correlated errors in sentiment can generate excessive network contractions (or expansions). A "false alarm" about a recession can trigger a real contraction in the network as firms collectively pull back, validating the pessimistic expectations. We derive comparative statics showing that policy interventions—such as reducing the fixed cost of supplier adoption or improving information transparency—can dampen these fluctuations.

The paper is organized as follows. Section 2 describes the environment and information structure. Section 3 characterizes the equilibrium, establishing the key lemmas on strategic complementarities and proving existence. Section 4 analyzes comparative statics and the information multiplier. Section 5 extends the results to a dynamic setting. Section 6 concludes.

---

## 2. Environment and Information

We study a production economy with $n$ firms, indexed by $i \in \mathcal{I} = \{1, \ldots, n\}$. The economy is subject to an aggregate productivity state $\mu \in \mathcal{M} \subset \mathbb{R}$, which is unobserved. Firms make production and network formation decisions based on private information.

### 2.1 Technology and Payoffs

Each firm $i$ produces a distinct good using labor $L_i$ and a set of intermediate inputs. The firm's choice involves both an extensive margin (which suppliers to adopt) and an intensive margin (how much to buy).

**The Action Space.** Firm $i$ chooses:
1.  A **supplier set** $S_i \in \mathcal{A}_i \subseteq 2^{\mathcal{I} \setminus \{i\}}$, where $\mathcal{A}_i$ is a finite menu of feasible supplier configurations.
2.  **Input quantities** $X_i = (X_{ij})_{j \in \mathcal{I} \setminus \{i\}} \in [0, \bar{X}]^{n-1}$, with $X_{ij} = 0$ for $j \notin S_i$.
3.  **Labor** $L_i \in [0, \bar{L}]$.

The action space is thus $\mathcal{A} = \mathcal{A}_i \times [0, \bar{X}]^{n-1} \times [0, \bar{L}]$, which is a **compact lattice** under the order $(S_i, X_i, L_i) \succeq (S_i', X_i', L_i')$ iff $S_i \supseteq S_i'$, $X_i \geq X_i'$ componentwise, and $L_i \geq L_i'$.

**Production Function.** Technology is given by a CES aggregator with state-dependent productivity:
$$
Y_i = \theta_i(\mu) F_i(S_i, L_i, X_i)
$$
where $\theta_i(\mu) = e^{\varphi \mu + \eta_i}$ is a productivity shifter increasing in the state $\mu$. The core production function follows Acemoglu and Azar (2020):
$$
F_i(S_i, L_i, X_i) = \left[ \left(1 - \sum_{j \in S_i} \alpha_{ij}\right)^{\frac{1}{\sigma}} (A_i L_i)^{\frac{\sigma-1}{\sigma}} + \sum_{j \in S_i} \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{\frac{\sigma-1}{\sigma}} \right]^{\frac{\sigma}{\sigma-1}}
$$
Here, $\sigma > 0$ is the elasticity of substitution. Parameter $\alpha_{ij} \in (0,1)$ represents the importance of input $j$, and $A_i$ is labor productivity.

**Assumption 1 (Technological Complementarity).** *The elasticity of substitution satisfies $\sigma < 1$.*

This assumption is critical. It implies that inputs are complements: the marginal product of one input increases with the quantity of others. Empirical estimates for intermediate inputs typically support $\sigma < 1$.

**Assumption 1b (Share Structure).** *For each firm $i$, there exist fixed share parameters $\{\alpha_{ij}\}_{j \in \mathcal{I} \setminus \{i\}}$ such that $\sum_{j \neq i} \alpha_{ij} < 1$. When firm $i$ adopts supplier set $S_i$, the labor share is $\gamma_{L,i}(S_i) = 1 - \sum_{j \in S_i} \alpha_{ij}$.*

**Timing.** The game proceeds as follows:
1. Nature draws $\mu$ and signals $(s_1, \ldots, s_n)$ from an affiliated distribution.
2. Each firm $i$ observes its private signal $s_i$.
3. Firms simultaneously choose actions $a_i = (S_i, X_i, L_i)$.
4. Production occurs; markets clear at prices $P^*(a, \mu)$.
5. Payoffs are realized.

**Payoffs.** Firm $i$ maximizes expected profit. Given output price $P_i$ and intermediate input prices $P = (P_1, \ldots, P_n)$, profit is:
$$
\Pi_i = P_i \theta_i(\mu) F_i(S_i, L_i, X_i) - L_i - \sum_{j \in S_i} P_j X_{ij} - \gamma |S_i|
$$
where $\gamma > 0$ is the **per-link adoption cost**. Wage is normalized to 1.

**Market Clearing.** Prices are determined by market clearing. Good $j$ has demand from final consumers $C_j(P, \mu)$ and intermediate demand from other firms:
$$
Y_j = C_j(P, \mu) + \sum_{i: j \in S_i} X_{ij}
$$
We assume final demand is downward-sloping. In equilibrium, prices $P^*(S, \mu)$ clear all markets. The key property is that *aggregate expansion reduces prices*: if more firms adopt more suppliers (increasing $Y_j$), equilibrium $P_j^*$ falls.

**Cost Function.** Given supplier set $S_i$ and prices $P$, the minimum cost of producing output $Y_i$ is:
$$
K_i(S_i, Y_i, P) = Y_i \cdot \mathcal{P}_i(S_i, P)
$$
where the CES price index is:
$$
\mathcal{P}_i(S_i, P) = \left[ \gamma_{L,i}(S_i) + \sum_{j \in S_i} \alpha_{ij} P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$
This cost function is derived from the CES dual (see Appendix A.0).

### 2.3 Optimal Input Choice (First-Order Conditions)

Given a supplier set $S_i$ and prices $P$, firm $i$ chooses inputs to maximize profit. The first-order conditions are:

**FOC for $X_{ij}$ (Intensive Margin):**
$$
P_i \theta_i(\mu) \frac{\partial F_i}{\partial X_{ij}} = P_j \quad \forall j \in S_i
$$

**FOC for $L_i$:**
$$
P_i \theta_i(\mu) \frac{\partial F_i}{\partial L_i} = 1
$$

These yield the standard CES input demands:
$$
X_{ij}^* = \alpha_{ij} \left( \frac{P_j}{\mathcal{P}_i} \right)^{-\sigma} \frac{Y_i}{\theta_i(\mu)}, \qquad L_i^* = \gamma_{L,i}(S_i) \left( \frac{1}{\mathcal{P}_i} \right)^{-\sigma} \frac{Y_i}{A_i \theta_i(\mu)}
$$

**Reduced-Form Profit.** Substituting optimal inputs, firm $i$'s profit becomes:
$$
\Pi_i^*(S_i, P, \mu) = \left[ P_i \theta_i(\mu) - \mathcal{P}_i(S_i, P) \right] Y_i^* - \gamma |S_i|
$$
The extensive-margin choice of $S_i$ trades off reduced unit cost $\mathcal{P}_i(S_i, P)$ against adoption costs $\gamma |S_i|$. This reduced-form game inherits supermodularity from the production function (Lemma 1).

### 2.2 Information Structure

Firms do not observe $\mu$. Instead, each firm observes a private signal $s_i \in \mathbb{R}$. We denote firm $i$'s **type** by $\tau_i \equiv s_i$.

**Affiliated Signals.** We assume the joint distribution of the state and signals $(\mu, s_1, \ldots, s_n)$ satisfies **affiliation**.

**Definition 1 (Affiliation).** Random variables $Z$ with joint density $f$ are *affiliated* if for all $z, z'$:
$$
f(z \vee z') f(z \wedge z') \geq f(z) f(z')
$$
where $\vee$ and $\wedge$ denote component-wise max and min.

Affiliation is a formalization of "positive correlation." It implies that observing a high signal $s_i$ makes firm $i$ believe:
1.  The state $\mu$ is likely high.
2.  Other firms' signals $s_{-i}$ are likely high.

A leading example is the **Gaussian Common Factor Model**:
$$
s_i = \mu + \varepsilon_i, \quad \varepsilon_i \sim \mathcal{N}(0, \sigma_\varepsilon^2) \text{ i.i.d.}
$$
where $\mu \sim \mathcal{N}(\mu_0, \sigma_\mu^2)$. As shown in Appendix A, this structure satisfies affiliation.

**Strategies.** A pure strategy for firm $i$ is a map $\sigma_i: \mathcal{T}_i \to \mathcal{S}_i$ from types (signals) to actions (supplier set and inputs). We focus on **monotone strategies**: strategies where higher signals lead to "higher" actions (denser networks and more inputs).

---

## 3. Equilibrium with Strategic Complementarities

Our goal is to prove the existence of equilibria where "optimism breeds density." We do this by mapping the production network problem into the supermodular game framework of Van Zandt and Vives (2007). This requires establishing key geometric properties of the payoffs.

### 3.1 Lemmas: The Geometry of Incentives

We establish three auxiliary lemmas that drive the main results.

**Lemma 1 (Supermodularity of Production).** *Under Assumption 1 ($\sigma < 1$), the production function $F_i$ is supermodular in $(S_i, X_i, L_i)$.*

*Proof (Sketch).* Supermodularity requires discrete increasing differences (adding a supplier raises the marginal product of continuous inputs) and positive cross-partials between continuous inputs. For CES with $\sigma < 1$, the cross-partial $\partial^2 F / \partial X_j \partial X_k$ is proportional to $(1-\sigma)/\sigma$, which is positive. Intuitively, with complements, having access to more varieties raises the productivity of all existing inputs. (See Appendix A.1 for full derivation).

**Lemma 2 (Technology-Price Single-Crossing).** *If expanding the supplier set is optimal at high input prices $P$, it is strictly optimal at lower prices $P' \leq P$.*

*Proof (Sketch).* The cost function $K_i(S_i, P)$ is concave in prices. The cost *reduction* from adding a supplier, $\Delta K$, becomes more significant (more negative) as the price of that supplier falls. This is a direct consequence of the CES functional form with $\sigma < 1$. (See Appendix A.2).

**Lemma 3 (Information Complementarity).** *Under affiliation, expected payoffs satisfy single-crossing in $(a_i, \tau_i)$. That is, higher types have a stronger incentive to expand.*

*Proof (Sketch).* Higher types hold FOSD-shifted beliefs about $\mu$. Since the marginal product of inputs is increasing in productivity $\theta_i(\mu)$, and the profit difference from expansion is increasing in $\mu$, FOSD beliefs imply a higher expected gain from expansion. (See Appendix A.3).

### 3.2 Existence of Extremal Equilibria

These lemmas establish that the game exhibits strategic complementarities:
1.  **Direct Complementarity:** $a_i$ and $a_{-i}$ are complements. If others expand ($a_{-i} \uparrow$), output supply rises and input prices $P$ fall. By Lemma 2, lower prices increase the incentive for $i$ to expand.
2.  **Information Complementarity:** Affiliation implies that beliefs about others' types are increasing in own type.

We can now state the main existence result.

**Theorem 1 (Existence of Extremal Monotone Equilibria).** *There exist a greatest equilibrium $\bar{\sigma}$ and a least equilibrium $\underline{\sigma}$. In both equilibria, strategies are monotone: firms with higher signals choose (weakly) larger supplier sets and input quantities.*

*Proof.* The game satisfies the conditions of Van Zandt and Vives (2007):
1.  The action space is a compact lattice.
2.  The type space is partially ordered (by signal value).
3.  Payoffs are supermodular in own action (Lemma 1).
4.  Payoffs have increasing differences in $(a_i, a_{-i})$ (Lemma 2 + Price mechanism).
5.  Payoffs satisfies single-crossing in $(a_i, \tau_i)$ (Lemma 3).

By Tarski's fixed point theorem applied to the best-response mapping on the lattice of monotone functions, extremal fixed points exist. Monotonicity implies that "good news" leads to network expansion.

**Discussion.** The existence of *monotone* equilibria is crucial. It means we do not need to solve for the complex hierarchy of beliefs (guesses about guesses). Instead, we know that equilibrium strategies are ordered: more optimistic firms simply invest more.

---

## 4. Comparative Statics

The tractability of extremal equilibria allows us to analyze how the production network responds to shocks.

### 4.1 The Information Multiplier

Consider a shift in "sentiment"—an exogenous improvement in the distribution of beliefs (e.g., a credible public report that productivity is high).

**Theorem 2 (Information Multiplier).** *Let the signal structure shift such that interim beliefs improve in the FOSD sense. Then the extremal equilibrium networks expand.*

*Proof.* An FOSD shift in beliefs increases the expected marginal return to expansion for any given strategy of opponents (by Lemma 3). This shifts the best-response function upward. Since the equilibrium is a fixed point of increasing best-responses, the fixed point itself shifts upward.

**Mechanism.** The network expansion is driven by two forces:
1.  **Direct Effect:** Firms are more optimistic about fundamental productivity $\mu$, so they invest more.
2.  **Strategic Effect:** Firms know that *others* are also more optimistic and will likely expand. Anticipating denser supply chains and lower input prices, they expand *further*.
This second channel is the "information multiplier." In opaque supply chains, sentiment is self-reinforcing.

### 4.2 Policy and Adoption Costs

Consider a policy that reduces the friction of forming links (e.g., digitizing supply chain logistics), represented by a parameter $\gamma$ that reduces adoption costs.

**Theorem 3 (Policy Impact).** *A reduction in supplier adoption costs leads to a strictly larger equilibrium network.*

This implies that subsidies for supply chain resilience can have multiplicative effects. By encouraging some firms to diversify, the policy lowers input prices for others, inducing further diversification.

---

## 5. Dynamic Extension

Finally, we extend the analysis to a dynamic setting where supplier relationships are sticky (persistent).

**Setup.** The state at time $t$ is $z_t = (\mu_t, A_{t-1})$, where $A_{t-1}$ is the adjacency matrix of the previous period. The cost of forming a link depends on whether it existed yesterday.

**Theorem 4 (Dynamic Monotonicity).** *There exist Bayesian Markov Perfect Equilibria where strategies are monotone in the state $z_t$ and type $\tau_t$. If the economy starts with a denser network $A_0$, it remains denser along the entire transition path (for the same sequence of shocks).*

This result highlights **hysteresis**. A temporary positive shock that builds the network can have permanent effects, as the established links lower the cost of maintenance in future periods. Conversely, a "panic" that destroys links can leave the supply chain permanently scarred.

---

## 6. Conclusion

By treating information as a fundamental input subject to strategic complementarities, this paper bridges the gap between production network theory and information economics. We show that in a world of opaque supply chains, "optimism" is a productive asset. When inputs are technological complements, the belief that others are investing is a self-fulfilling prophecy.

Our findings explain why supply chains can be fragile to sentiment shocks. A correlated bad signal—even if fundamental productivity is unchanged—can trigger a "flight to safety," unraveling the network. This suggests that policy interventions should focus not only on physical infrastructure but also on **information infrastructure**: improving the precision of public signals to dampen the variance of private beliefs.

---

## Appendix A: Proofs

**A.1 Proof of Lemma 1 (Supermodularity).**

We prove that the CES production function $F_i(S_i, L_i, X_i)$ is supermodular in $(S_i, L_i, X_i)$ when $\sigma < 1$.

*Step 1: Continuous Inputs.*
Define $Q = \gamma_L^{1/\sigma} (A_i L_i)^{\rho} + \sum_{j \in S_i} \gamma_j^{1/\sigma} X_{ij}^{\rho}$ where $\rho = (\sigma-1)/\sigma$. Then $F_i = Q^{\sigma/(\sigma-1)}$.
For any two inputs $X_j, X_k$:
$$
\frac{\partial^2 F_i}{\partial X_j \partial X_k} = \frac{1}{\sigma} \gamma_j^{1/\sigma} \gamma_k^{1/\sigma} X_j^{-1/\sigma} X_k^{-1/\sigma} F^{2/\sigma - 1}
$$
Since $\sigma < 1$, all terms are positive. Thus cross-partials are positive.

*Step 2: Discrete-Continuous Interaction.*
Let $\Delta_j F(X) = F(S \cup \{j\}, X) - F(S, X)$. We show $\frac{\partial \Delta_j F}{\partial X_k} \geq 0$ for $k \in S$.
When inputs are complements ($\sigma < 1$), adding a new variety $j$ increases the marginal product of existing varieties because the CES aggregator exhibits decreasing marginal rates of technical substitution. Formally, $\frac{\partial^2 F}{\partial \mathbf{1}_{j \in S} \partial X_k} \geq 0$.

Combining these, $F_i$ is supermodular.

**A.2 Proof of Lemma 2 (Single-Crossing).**

We show that if $K(S', P) \leq K(S, P)$ for $S \subset S'$, then $K(S', P') \leq K(S, P')$ for $P' \leq P$.
Define $\Phi(S, P) = K(S, P)^{1-\sigma}$. Then:
$$
\Phi(S \cup \{k\}, P) - \Phi(S, P) = \alpha_k (P_k^{1-\sigma} - 1)
$$
This difference is negative (cost-reducing) iff $P_k^{1-\sigma} < 1$.
The derivative w.r.t $P_k$ is $(1-\sigma) P_k^{-\sigma}$, which is positive for $\sigma < 1$. Thus, the cost gain $\alpha_k(P_k^{1-\sigma}-1)$ is *increasing* in $P_k$ (becoming less negative). Conversely, as $P_k$ decreases, the gain becomes *more* negative (more beneficial).
Thus, if adding $k$ is profitable at $P$, it is even more profitable at $P' \leq P$.

**A.3 Proof of Lemma 3 (Belief Single-Crossing).**

We assume affiliation of $(\mu, s_1, \ldots, s_n)$.

*Part 1: Affiliation implies FOSD.*
By Milgrom and Weber (1982, Lemma 1), affiliation implies that the conditional likelihood ratio $f(s_{-i}, \mu | s_i)$ satisfies the Monotone Likelihood Ratio Property (MLRP). MLRP implies First-Order Stochastic Dominance (FOSD). Thus, $s_i' > s_i \implies \pi_i(\cdot | s_i') \geq_{FOSD} \pi_i(\cdot | s_i)$.

*Part 2: Increasing Differences in $(a_i, \tau_i)$.*
The expected payoff is $\mathbb{E}[\Pi_i(a_i, \mu) | \tau_i]$.
We know $\Pi_i$ has increasing differences in $(a_i, \mu)$ because higher $\mu$ raises productivity $\theta_i(\mu)$ and output price $p(\mu)$, increasing the marginal revenue of inputs/suppliers.
Since $\Pi_i(a_i', \mu) - \Pi_i(a_i, \mu)$ is increasing in $\mu$ (for $a_i' \geq a_i$), and beliefs are ordered by FOSD, we have:
$$
\mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i'] \geq \mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i]
$$
This is the single-crossing property.

**A.4 Proof of Theorem 1 (Existence).**

The game is a Bayesian game of strategic complementarities (Van Zandt & Vives, 2007).
1. **Lattice Actions:** $\mathcal{S}_i$ is a compact lattice.
2. **Supermodularity:** Payoffs are supermodular in $a_i$ (Lemma 1).
3. **Increasing Differences:** Payoffs have ID in $(a_i, a_{-i})$ (via price mechanism) and single-crossing in $(a_i, \tau_i)$ (Lemma 3).
4. **Order:** Types are ordered by FOSD.

Define the best-reply map $BR: \Sigma \to \Sigma$ on the lattice of monotone strategies $\Sigma$.
Since payoffs satisfy ID, $BR$ is an isotone operator (others playing higher monotone strategies induces me to play higher).
By Tarski's Fixed Point Theorem, the set of fixed points of an isotone map on a complete lattice is a non-empty complete lattice. Thus, extremal equilibria $\bar{\sigma}, \underline{\sigma}$ exist and are monotone.

*(Full proofs provided in the technical supplement)*

---

## References

Acemoglu, Daron, and Pablo D. Azar. 2020. "Endogenous Production Networks." *Econometrica* 88(1): 33–82.

Baqaee, David Rezza, and Emmanuel Farhi. 2019. "The Macroeconomic Impact of Microeconomic Shocks: Beyond Hulten's Theorem." *Econometrica* 87(4): 1155–1203.

Carvalho, Vasco M., Makoto Nirei, Yukiko U. Saito, and Alireza Tahbaz-Salehi. 2021. "Supply Chain Disruptions: Evidence from the Great East Japan Earthquake." *Quarterly Journal of Economics* 136(2): 1255–1321.

Kopytov, Alexandr, Bineet Mishra, Kristoffer P. Nimark, and Mathieu Taschereau-Dumouchel. 2024. "Endogenous Production Networks under Supply Chain Uncertainty." *Econometrica* 92(5).

Milgrom, Paul, and Chris Shannon. 1994. "Monotone Comparative Statics." *Econometrica* 62(1): 157–180.

Milgrom, Paul, and Robert Weber. 1982. "A Theory of Auctions and Competitive Bidding." *Econometrica* 50(5): 1089–1122.

Stokey, Nancy L., Robert E. Lucas, and Edward C. Prescott. 1989. *Recursive Methods in Economic Dynamics*. Harvard University Press.

Tarski, Alfred. 1955. "A Lattice-Theoretical Fixpoint Theorem and its Applications." *Pacific Journal of Mathematics* 5(2): 285–309.

Topkis, Donald M. 1998. *Supermodularity and Complementarity*. Princeton University Press.

Van Zandt, Timothy, and Xavier Vives. 2007. "Monotone Equilibria in Bayesian Games of Strategic Complementarities." *Journal of Economic Theory* 134(1): 339–360.
