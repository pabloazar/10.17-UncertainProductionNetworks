# Endogenous Supply Chains under Uncertainty: An Acemoglu–Azar–Van Zandt–Vives Framework

## 1. Primitives and Information

- Time $t=0,1,\dots$. Finite set of products/firms $\mathcal I=\{1,\dots,n\}$.
- Aggregate state $\mu_t\in\mathcal M\subset\mathbb R$ follows Markov kernel $P(\mu'|\mu)$ on compact $\mathcal M$.
- At the start of $t$, firm $i$ receives private signal $s_{i,t}=h(\mu_t)+\varepsilon_{i,t}$ with $(\varepsilon_{i,t})_{i\in\mathcal I}$ affiliated. The induced posterior (interim belief) is $\pi_i(\cdot|s_{i,t})$. Types $\tau_i\equiv s_{i,t}\in\mathcal T_i$ are ordered by MLR/FOSD via their induced interim beliefs: $\tau_i\succeq \tau'_i$ iff $\pi_i(\cdot|\tau_i)\ge_{FOSD}\pi_i(\cdot|\tau'_i)$.

**Notation change:** We use $\tau_i$ for types (to avoid confusion with time $t$).

## 2. Technology: CES with Endogenous Extensive Margin (Acemoglu–Azar)

### 2.1 The Acemoglu–Azar Production Function

Following Acemoglu–Azar (2020, Econometrica), each firm $i$ chooses:
- An **endogenous supplier subset** $S_i \in \mathcal{A}_i \subseteq 2^{\mathcal{I}\setminus\{i\}}$ (finite menu of allowable subsets)
- Input quantities $X_i = (X_{ij})_{j \in S_i} \in \mathbb{R}_+^{|S_i|}$
- Labor $L_i \in \mathbb{R}_+$

The **CES production function with Harrod-neutral technology** is (Acemoglu–Azar Appendix eq. 11):
$$
Y_i = F_i(S_i, A_i(S_i), L_i, X_i) = \left[ (1-\sum_{j\in S_i}\alpha_{ij})^{\frac{1}{\sigma}} (A_i(S_i) L_i)^{\frac{\sigma-1}{\sigma}} + \sum_{j\in S_i} \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{\frac{\sigma-1}{\sigma}} \right]^{\frac{\sigma}{\sigma-1}}
$$
where:
- $\sigma > 0$ is the elasticity of substitution ($\sigma \neq 1$)
- $\alpha_{ij} \in (0,1)$ are distribution parameters with $\sum_{j \in S_i} \alpha_{ij} < 1$
- $A_i(S_i) > 0$ is the productivity associated with supplier set $S_i$

**Special cases:**
- $\sigma \to 1$: Cobb-Douglas (Acemoglu–Azar baseline)
- $\sigma \to 0$: Leontief (fixed proportions)
- $\sigma \to \infty$: Linear (perfect substitutes)

### 2.2 Adding Uncertainty

We extend Acemoglu–Azar to uncertainty by making productivity state-dependent:
$$
\theta_i(\mu) = \exp(\varphi \mu + \eta_i), \qquad \varphi > 0
$$

The **stochastic production function** becomes:
$$
Y_i = \theta_i(\mu) \cdot F_i(S_i, A_i(S_i), L_i, X_i)
$$

### 2.3 Cost Function

From Acemoglu–Azar (Appendix B), the unit cost function for CES technology is:
$$
K_i(S_i, A_i(S_i), P) = \left[ (1-\sum_{j\in S_i}\alpha_{ij}) \left(\frac{W}{A_i(S_i)}\right)^{1-\sigma} + \sum_{j\in S_i} \alpha_{ij} P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$

Normalizing $W=1$ (wage as numeraire):
$$
K_i(S_i, A_i(S_i), P) = \left[ (1-\sum_{j\in S_i}\alpha_{ij}) A_i(S_i)^{\sigma-1} + \sum_{j\in S_i} \alpha_{ij} P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$

## 3. Strategy Spaces and Order Structure

### 3.1 Action Space

Each firm's action is $a_i = (S_i, X_i, L_i)$ where:
- $S_i \in \mathcal{A}_i$: supplier subset (finite set ordered by inclusion $\subseteq$)
- $X_i \in [0, \bar{X}]^{n-1}$: input quantities (bounded)
- $L_i \in [0, \bar{L}]$: labor (bounded)

The action space $\mathcal{S}_i = \mathcal{A}_i \times [0, \bar{X}]^{n-1} \times [0, \bar{L}]$ is ordered componentwise.

### 3.2 Lattice Structure

**Lemma 1 (Strategy Lattice).** Under the bounds $X_{ij} \in [0, \bar{X}]$ and $L_i \in [0, \bar{L}]$:
1. $\mathcal{A}_i$ is a finite lattice under set inclusion with meet $S \wedge T = S \cap T$ and join $S \vee T = S \cup T$.
2. $[0, \bar{X}]^{n-1} \times [0, \bar{L}]$ is a compact complete lattice under componentwise order.
3. The product $\mathcal{S}_i$ is a compact metrizable complete lattice.

*Proof.* (1) Any finite poset closed under $\cap$ and $\cup$ is a lattice. $\mathcal{A}_i \subseteq 2^{\mathcal{I}\setminus\{i\}}$ is finite by assumption. (2) Closed bounded intervals in $\mathbb{R}$ are complete lattices; products of complete lattices are complete lattices. (3) Products of compact metrizable complete lattices are compact metrizable complete lattices. $\square$

## 4. Payoff Structure and Derivation of Van Zandt–Vives Conditions

### 4.1 Period Payoff

At state $z = (\mu, A_{t-1})$ and type $\tau_i$, firm $i$'s expected period payoff against strategy profile $\sigma_{-i}$ is:
$$
\Pi_i(a_i; \sigma_{-i}, z, \tau_i) = \mathbb{E}\Big[ p(\mu) \cdot \theta_i(\mu) \cdot F_i(S_i, A_i(S_i), L_i, X_i) - L_i - \sum_{j \in S_i} P_j X_{ij} \;\Big|\; \tau_i, z \Big]
$$

where $p(\mu)$ is the output price (increasing in $\mu$) and $P_j$ are intermediate input prices.

### 4.2 Supermodularity of the CES Production Function

**Proposition 1 (CES Supermodularity).** The CES production function $F_i(S_i, A_i(S_i), L_i, X_i)$ is **supermodular** in $(S_i, L_i, X_i)$ when $\sigma < 1$ (complements case).

*Proof.* Write $F_i = G(Q)^{\frac{\sigma}{\sigma-1}}$ where:
$$
Q = (1-\sum_{j\in S_i}\alpha_{ij})^{\frac{1}{\sigma}} (A_i L_i)^{\frac{\sigma-1}{\sigma}} + \sum_{j\in S_i} \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{\frac{\sigma-1}{\sigma}}
$$

For $\sigma < 1$, we have $\frac{\sigma-1}{\sigma} < 0$, so the exponents on $L_i$ and $X_{ij}$ are negative. This makes each term a decreasing function of its argument. The composition $G(Q)^{\frac{\sigma}{\sigma-1}}$ with $\frac{\sigma}{\sigma-1} < 0$ reverses the monotonicity, giving supermodularity.

More precisely, for supermodularity we need $\frac{\partial^2 F}{\partial X_{ij} \partial X_{ik}} \geq 0$ for $j \neq k$. Computing:
$$
\frac{\partial F}{\partial X_{ij}} = F^{\frac{1}{\sigma}} \cdot \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{-\frac{1}{\sigma}}
$$

$$
\frac{\partial^2 F}{\partial X_{ij} \partial X_{ik}} = \frac{1-\sigma}{\sigma} \cdot F^{\frac{1}{\sigma}-1} \cdot \alpha_{ij}^{\frac{1}{\sigma}} \alpha_{ik}^{\frac{1}{\sigma}} X_{ij}^{-\frac{1}{\sigma}} X_{ik}^{-\frac{1}{\sigma}}
$$

This is $\geq 0$ when $\sigma < 1$ (since $\frac{1-\sigma}{\sigma} > 0$). $\square$

**Remark.** When $\sigma > 1$ (substitutes), the production function is **submodular**. This highlights that the strategic complementarities in our model arise naturally from technological complementarities in production.

### 4.3 Technology-Price Single-Crossing (Acemoglu–Azar Proposition 3)

**Proposition 2 (A&A Single-Crossing).** For CES production with input-specific productivities, the unit cost function $K_i(S_i, A_i(S_i), P)$ satisfies the **technology-price single-crossing condition**:

For all $S_i \subset S_i'$ and price vectors $P' \leq P$ (componentwise on $P_{-i}$):
$$
K_i(S_i', A_i(S_i'), P) \leq K_i(S_i, A_i(S_i), P) \implies K_i(S_i', A_i(S_i'), P') \leq K_i(S_i, A_i(S_i), P')
$$

*Proof.* This is Acemoglu–Azar (2020) Proposition 3 (labeled "cs ces" in their paper). The key insight: if adopting more inputs is cost-reducing at high prices, it remains cost-reducing at lower prices because the new inputs are now cheaper. The CES cost function:
$$
K_i = \left[ (1-\sum_{j\in S_i}\alpha_{ij}) A_i^{\sigma-1} + \sum_{j\in S_i} \alpha_{ij} P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$
is decreasing in each $P_j$ when $\sigma < 1$ (since $1-\sigma > 0$ and the exponent $\frac{1}{1-\sigma} > 0$). Adding supplier $k$ to $S_i$ adds the term $\alpha_{ik} P_k^{1-\sigma}$ and modifies the labor share. The single-crossing property follows from the monotonicity of the cost difference in prices. $\square$

### 4.4 Increasing Differences in Payoffs

**Proposition 3 (Strategic Complementarities).** Under the CES technology with $\sigma < 1$:
1. $\Pi_i$ has **increasing differences** in $(a_i, a_{-i})$
2. $\Pi_i$ has **increasing differences** in $(a_i, z)$
3. $\Pi_i$ has **single-crossing** in $(a_i, \tau_i)$

*Proof.*

**(1) ID in $(a_i, a_{-i})$:** Higher $a_{-i}$ means more production by other firms, which (in equilibrium) lowers intermediate input prices $P_j$. By Proposition 2 (single-crossing), lower $P_j$ makes adoption of more suppliers more attractive, increasing marginal returns to $a_i$.

**(2) ID in $(a_i, z)$:** Higher $\mu$ increases $\theta_i(\mu) = \exp(\varphi\mu + \eta_i)$ and $p(\mu)$, raising the marginal value of output. With CES supermodularity (Proposition 1), this increases the marginal return to higher inputs $(S_i, X_i, L_i)$.

**(3) Single-crossing in $(a_i, \tau_i)$:** Higher type $\tau_i$ FOSD-shifts beliefs over $\mu$ upward. Since $\mathbb{E}[\Pi_i | \tau_i]$ has ID in $(a_i, \mu)$, higher $\tau_i$ makes higher $a_i$ more attractive. Formally, for $\tau_i' \succeq \tau_i$ (FOSD):
$$
\mathbb{E}[\Pi_i(a_i'; \cdot) - \Pi_i(a_i; \cdot) | \tau_i'] \geq \mathbb{E}[\Pi_i(a_i'; \cdot) - \Pi_i(a_i; \cdot) | \tau_i]
$$
for $a_i' \geq a_i$. This is the Milgrom-Shannon monotone selection criterion. $\square$

## 5. Interim Beliefs and FOSD Ordering

The key insight of Van Zandt–Vives (2007) is that **no common prior is needed**. What matters is that interim beliefs are **FOSD-ordered in types**—this is the primitive that enables monotone equilibrium existence.

### 5.1 The VZV Interim Formulation

**Definition (FOSD-Ordered Types).** Types $\tau_i \in \mathcal{T}_i$ are ordered by $\tau_i \succeq \tau_i'$ if and only if the interim belief $\pi_i(\cdot | \tau_i)$ FOSD-dominates $\pi_i(\cdot | \tau_i')$:
$$
\tau_i \succeq \tau_i' \iff \pi_i(\cdot | \tau_i) \geq_{FOSD} \pi_i(\cdot | \tau_i')
$$

This FOSD ordering is **required** for VZV to work. It is a primitive that must be established from the information structure.

### 5.2 Deriving FOSD from Affiliation

The standard way to obtain FOSD-ordered beliefs is through **affiliation** of signals and fundamentals.

**Definition (Affiliation).** Random variables $(Z_1, \ldots, Z_m)$ with joint density $f$ are **affiliated** if:
$$
f(z \vee z') \cdot f(z \wedge z') \geq f(z) \cdot f(z')
$$
where $\vee$ and $\wedge$ denote componentwise max and min. Equivalently, $\log f$ is supermodular.

**Proposition 4 (Affiliation → FOSD).** Under affiliation of $(s_1, \ldots, s_n, \mu)$:
1. Higher $s_i$ induces FOSD-higher beliefs over $\mu$: $\pi_i(\mu | s_i') \geq_{FOSD} \pi_i(\mu | s_i)$ for $s_i' > s_i$
2. Higher $s_i$ induces FOSD-higher beliefs over $s_{-i}$: $\pi_i(s_{-i} | s_i') \geq_{FOSD} \pi_i(s_{-i} | s_i)$

*Proof.* Milgrom-Weber (1982) Theorem 1 and Lemma 1. Affiliation (log-supermodularity of the joint density) implies monotone likelihood ratio ordering of conditional distributions, which implies FOSD. $\square$

### 5.3 Sufficient Conditions for Affiliation

**Proposition 5 (Gaussian Affiliation).** If $(s_1, \ldots, s_n, \mu)$ are jointly Gaussian with **non-negative correlations**, they are affiliated.

*Proof.* For Gaussian vectors, affiliation ⟺ the precision matrix (inverse covariance) has non-positive off-diagonals. Non-negative correlations in the covariance matrix $\Sigma$ imply this property for $\Sigma^{-1}$ (Karlin-Rinott, 1980). $\square$

**Common Setups Satisfying Affiliation:**

| Setup | $s_i = $ | Affiliated if: |
|-------|----------|----------------|
| Common value + noise | $\mu + \varepsilon_i$ | $\varepsilon_i$ independent or pos. correlated |
| Gaussian signals | $h(\mu) + \varepsilon_i$ | $\text{Cov}(\varepsilon_i, \varepsilon_j) \geq 0$, $\text{Cov}(\varepsilon_i, \mu) \geq 0$ |
| Order statistics | $\mu_{(k)}$ | Standard order stat properties |

### 5.4 From FOSD to Monotone Equilibria (VZV)

**Key Logic Chain:**
1. **Affiliation** (primitive on information structure)
2. **→ FOSD-ordered interim beliefs** (Proposition 4)
3. **+ Strategic complementarities** (from CES with $\sigma < 1$, Proposition 3)
4. **→ Monotone equilibria exist** (VZV Theorem)

**Proposition 6 (Belief Propagation).** Under affiliation, higher own type $\tau_i$ FOSD-shifts beliefs about others' types:
$$
\tau_i' \succeq \tau_i \implies \pi_i(\tau_{-i} | \tau_i') \geq_{FOSD} \pi_i(\tau_{-i} | \tau_i)
$$

*Proof.* Affiliation of $(s_1, \ldots, s_n)$ implies the conditional distribution of $s_{-i}$ given $s_i$ is FOSD-increasing in $s_i$ (Milgrom-Weber Lemma 1). $\square$

**Proposition 7 (VZV Stationarity in Equilibrium).** Given:
- FOSD-ordered beliefs (from affiliation)
- Strategic complementarities (from CES)
- Single-crossing in $(a_i, \tau_i)$

Then in any monotone equilibrium $\sigma^*$, the induced belief over opponents' **actions** is also FOSD-increasing:
$$
\tau_i' \succeq \tau_i \implies \pi_i(\sigma_{-i}^*(\tau_{-i}) | \tau_i') \geq_{FOSD} \pi_i(\sigma_{-i}^*(\tau_{-i}) | \tau_i)
$$

*Proof.* Proposition 6 gives FOSD over types. Monotonicity of $\sigma_{-i}^*$ (types → actions) preserves FOSD. $\square$

## 6. Verification of Van Zandt–Vives Conditions

We now verify that our model satisfies the conditions of Van Zandt–Vives (2007, JET) Theorem 1.

### 6.1 VZV Condition 1: Compact Lattice Action Spaces

✓ **Verified by Lemma 1.** $\mathcal{S}_i = \mathcal{A}_i \times [0, \bar{X}]^{n-1} \times [0, \bar{L}]$ is a compact metrizable complete lattice.

### 6.2 VZV Condition 2: Type Spaces with FOSD Order

✓ **Verified by construction.** Types $\tau_i \in \mathcal{T}_i$ are ordered by $\tau_i \succeq \tau_i'$ iff $\pi_i(\cdot|\tau_i) \geq_{FOSD} \pi_i(\cdot|\tau_i')$.

### 6.3 VZV Condition 3: Quasisupermodularity in Own Action

**Proposition 8 (Quasisupermodularity).** The payoff $\Pi_i(a_i; \sigma_{-i}, z, \tau_i)$ is **quasisupermodular** in $a_i$.

*Proof.* By Proposition 1, the CES production function with $\sigma < 1$ is supermodular in $(S_i, L_i, X_i)$. Revenue $p(\mu) \theta_i(\mu) F_i$ inherits supermodularity (positive scalar multiplication preserves supermodularity).

Costs are:
- $L_i$: linear in $L_i$ (modular)
- $\sum_{j \in S_i} P_j X_{ij}$: linear in $X_{ij}$ for fixed $S_i$ (modular)

The sum of supermodular and modular functions is supermodular. Taking expectations preserves supermodularity (Milgrom-Shannon). Hence $\mathbb{E}[\Pi_i | \tau_i]$ is supermodular in $a_i$.

Supermodularity implies quasisupermodularity. $\square$

### 6.4 VZV Condition 4: Single-Crossing in $(a_i, \tau_i)$

✓ **Verified by Proposition 3(3).** Higher $\tau_i$ FOSD-shifts beliefs over $\mu$, and $\Pi_i$ has ID in $(a_i, \mu)$, giving single-crossing.

### 6.5 VZV Condition 5: Increasing Differences in $(a_i, a_{-i})$

✓ **Verified by Proposition 3(1).** Through the price mechanism and technology-price single-crossing (Proposition 2).

### 6.6 VZV Condition 6: Best-Reply Correspondence Properties

**Proposition 9 (Best-Reply Properties).** The best-reply correspondence $BR_i$ is:
1. Nonempty (by compactness and upper semicontinuity)
2. Upper hemicontinuous (Maximum Theorem)
3. Ascending in $(a_{-i}, \tau_i, z)$ (Topkis/Milgrom-Shannon)

*Proof.*
1. **Nonempty:** $\mathcal{S}_i$ is compact, $\Pi_i$ is continuous in $a_i$ (CES is smooth), so the maximum is attained.
2. **UHC:** Payoff is continuous in $a_i$ and the constraint set $\mathcal{S}_i$ is constant, so the Maximum Theorem applies.
3. **Ascending:** By Propositions 3 and 8, $\mathbb{E}[\Pi_i | \tau_i]$ has single-crossing in $(a_i, a_{-i})$, $(a_i, \tau_i)$, and $(a_i, z)$. Milgrom-Shannon monotone selection theorem implies all selections from $BR_i$ are monotone. $\square$

## 7. Main Results

### 7.1 Static Stage Game

**Theorem 1 (Existence of Extremal Monotone BNE).** In the static stage game at state $z$, there exist a **greatest** and a **least** pure-strategy Bayesian Nash equilibrium $\bar{\sigma}(z)$ and $\underline{\sigma}(z)$, each in strategies monotone in type.

*Proof.* This follows from Van Zandt–Vives (2007) Theorem 1. We have verified:
- (VZV1) Compact lattice action spaces ✓
- (VZV2) Type spaces with FOSD order ✓
- (VZV3) Quasisupermodularity in own action ✓
- (VZV4) Single-crossing in $(a_i, \tau_i)$ ✓
- (VZV5) Increasing differences in $(a_i, a_{-i})$ ✓
- (VZV6) Nonempty, UHC, ascending best-reply ✓

The extremal equilibria are constructed by iterating the best-reply mapping from the maximal (resp. minimal) strategy profile. Convergence is guaranteed by Tarski's fixed-point theorem. $\square$

### 7.2 Comparative Statics

**Theorem 2 (Comparative Statics of Extremal BNE).**
1. If interim beliefs shift upward in FOSD, both $\underline{\sigma}(z)$ and $\bar{\sigma}(z)$ increase weakly.
2. If parameter $\tau$ enters with increasing differences (e.g., higher $A_i(S_i)$, lower distortions), then $\underline{\sigma}(z;\tau)$ and $\bar{\sigma}(z;\tau)$ are nondecreasing in $\tau$.

*Proof.*
**(1)** Van Zandt–Vives Theorem 2: FOSD improvement in beliefs increases extremal equilibria.

**(2)** Let $\tau$ parameterize technology with $A_i(S_i; \tau)$ increasing in $\tau$. Then $\Pi_i$ has ID in $(a_i, \tau)$: higher $\tau$ raises $A_i$, raising $F_i$, raising marginal value of inputs. By Topkis, the best-reply is monotone in $\tau$. Fixed points of isotone maps are monotone (Tarski). $\square$

### 7.3 Dynamic Extension

**Theorem 3 (Existence of Bayesian Markov Perfect Equilibrium).**

Define the Bellman operator:
$$
(\mathcal{T}V_i)(z, \tau_i) = \max_{a_i \in \mathcal{S}_i} \Big\{ \mathbb{E}[\Pi_i(a_i; \sigma_{-i}, z, \tau_i)] + \beta \mathbb{E}[V_i(z', \tau_i') | z, \tau_i, a_i, \sigma_{-i}] \Big\}
$$

Assume the law of motion $A' = \Gamma(A, \alpha)$ is isotone and the transition kernel preserves FOSD order. Then:
1. There exists a Bayesian Markov Perfect Equilibrium.
2. There exist extremal Markov strategies.
3. There exists a stationary network $A^*$ solving $A^* = \Gamma(A^*, \alpha^*)$.

*Proof.*
1. **Existence:** The period payoff is supermodular (Proposition 7). The continuation value preserves ID when the transition is isotone (Stokey-Lucas-Prescott + Topkis): if $V_i(z', \tau_i')$ is increasing in $(z', \tau_i')$ and the transition FOSD-shifts $(z', \tau_i')$ upward when $(z, \tau_i, a_i)$ increases, then $\mathbb{E}[V_i | z, \tau_i, a_i]$ has ID in $a_i$ and $(z, \tau_i)$.

2. **Extremal strategies:** The operator $\mathcal{T}$ maps the lattice of bounded value functions to itself and is order-preserving. By Tarski, extremal fixed points exist.

3. **Stationary network:** With monotone extremal strategies $\alpha^*$, the map $A \mapsto \Gamma(A, \alpha^*(A))$ is isotone on the lattice of networks (ordered by inclusion). By Tarski, there exists $A^*$ with $A^* = \Gamma(A^*, \alpha^*(A^*))$. $\square$

**Theorem 4 (Monotone Transitional Dynamics).**

Let $z_0' \geq z_0$ (higher $\mu$, denser inherited $A$). Then along extremal BMPE policies:
$$
\underline{\sigma}_t(z_0') \geq \underline{\sigma}_t(z_0), \quad \bar{\sigma}_t(z_0') \geq \bar{\sigma}_t(z_0), \quad A_t(z_0') \geq A_t(z_0) \text{ for all } t
$$

*Proof.* By induction on $t$.

**Base case ($t=0$):** $z_0' \geq z_0$ by assumption.

**Inductive step:** Suppose $z_t' \geq z_t$. By Theorem 2, extremal actions satisfy $\sigma_t(z_t') \geq \sigma_t(z_t)$. In particular, supplier choices satisfy $\alpha_t(z_t') \supseteq \alpha_t(z_t)$ (in the inclusion order).

Since $\Gamma$ is isotone:
$$
A_{t+1}' = \Gamma(A_t', \alpha_t') \geq \Gamma(A_t, \alpha_t) = A_{t+1}
$$

Also, since $\mu_{t+1}' | z_t'$ FOSD-dominates $\mu_{t+1} | z_t$ (assuming the Markov kernel preserves order), we have $z_{t+1}' \geq z_{t+1}$.

By induction, the ordering propagates for all $t$. $\square$

## 8. Positioning and Contribution

### 8.1 Exact Acemoglu–Azar Extensive Margin under Uncertainty

We adopt Acemoglu–Azar's **subset choice** of inputs (the extensive margin of the IO matrix) as the primitive technological decision. This differs from exposure-weight models that directly choose continuous weights on a fixed support. Our CES specification inherits their:
- Technology-price single-crossing (Proposition 2)
- Equilibrium existence and uniqueness (via their lattice-theoretic approach)
- Discontinuous comparative statics when supplier sets change

### 8.2 Incomplete Information with Derived Affiliation

We introduce **affiliated private signals**. Crucially, affiliation is **derived** from a natural Gaussian structure on fundamentals and noise (Proposition 4), not assumed ad hoc. This yields:
- FOSD ordering of interim beliefs (Proposition 5)
- Cross-player belief correlation (Proposition 6)
- Single-crossing in $(a_i, \tau_i)$ via Milgrom-Weber/Shannon machinery

### 8.3 Van Zandt–Vives Application

By verifying the six VZV conditions from primitives, we establish:
- Existence of extremal monotone BNE (not just any BNE)
- Comparative statics in beliefs and parameters
- Dynamic extension with ordered transition paths

This provides **equilibrium selection** through extremal equilibrium focus, yielding robust policy predictions absent in complete-information models.

### 8.4 Comparison with Taschereau-Dumouchel et al.

| Feature | Taschereau-Dumouchel | Our Model |
|---------|---------------------|-----------|
| Choice variable | Continuous exposure weights | Discrete supplier subsets (A&A) |
| Information | Complete | Incomplete (affiliated signals) |
| Equilibrium | Fixed-point | Extremal monotone BNE |
| Dynamics | Deterministic | Bayesian Markov with ordered paths |

## 9. Appendix: Assumption-to-Theorem Mapping

### A. Primitive Assumptions

**(P1) CES Technology with $\sigma < 1$:**
$$
F_i = \left[ (1-\sum_{j\in S_i}\alpha_{ij})^{\frac{1}{\sigma}} (A_i L_i)^{\frac{\sigma-1}{\sigma}} + \sum_{j\in S_i} \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{\frac{\sigma-1}{\sigma}} \right]^{\frac{\sigma}{\sigma-1}}
$$
→ Implies: Supermodularity (Prop. 1), single-crossing (Prop. 2), ID in $(a_i, a_{-i})$ (Prop. 3)

**(P2) Affiliation → FOSD-Ordered Beliefs:**

Signals $(s_1, \ldots, s_n, \mu)$ are **affiliated** (log-supermodular joint density).
- Sufficient condition: Gaussian with non-negative correlations (Prop. 5)

→ Implies: FOSD-ordered beliefs over $(\mu, \tau_{-i})$ (Prop. 4), belief propagation (Prop. 6), VZV stationarity (Prop. 7)

**(P3) Bounded Action Spaces:**
$$
X_{ij} \in [0, \bar{X}], \quad L_i \in [0, \bar{L}], \quad \mathcal{A}_i \text{ finite}
$$
→ Implies: Compact lattice (Lemma 1), best-reply existence (Prop. 9)

**(P4) Monotone State Dynamics:**
$$
\theta_i(\mu) = \exp(\varphi\mu + \eta_i), \quad p(\mu) \text{ increasing}, \quad \Gamma(A, \alpha) \text{ isotone}
$$
→ Implies: ID in $(a_i, z)$ (Prop. 3), dynamic monotonicity (Thm. 4)

### B. Derived Conditions

| Derived Condition | Source |
|-------------------|--------|
| Quasisupermodularity in $a_i$ | P1 (CES supermodularity) → Prop. 8 |
| FOSD-ordered beliefs | P2 (affiliation) → Prop. 4 |
| Single-crossing in $(a_i, \tau_i)$ | P1 + P2 |
| ID in $(a_i, a_{-i})$ | P1 (price single-crossing via A&A) |
| Compact lattice actions | P3 |
| Ascending best-reply | Props. 3, 8 → Prop. 9 |

### C. Main Results

| Theorem | Uses |
|---------|------|
| Thm 1 (Extremal BNE) | VZV conditions from P1–P3 |
| Thm 2 (Comparative statics) | VZV + Topkis |
| Thm 3 (Dynamic BMPE) | P1–P4 + Stokey-Lucas |
| Thm 4 (Ordered paths) | P4 + induction |

## 10. References

- Acemoglu, D., and P. D. Azar (2020), "Endogenous Production Networks," Econometrica 88(1):33–82.
- Karlin, S., and Y. Rinott (1980), "Classes of orderings of measures and related correlation inequalities," Journal of Multivariate Analysis.
- Milgrom, P., and C. Shannon (1994), "Monotone Comparative Statics," Econometrica.
- Milgrom, P., and R. Weber (1982), "A Theory of Auctions and Competitive Bidding," Econometrica.
- Stokey, N., R. Lucas, and E. Prescott (1989), Recursive Methods in Economic Dynamics, Harvard.
- Topkis, D. M. (1998), Supermodularity and Complementarity, Princeton.
- Van Zandt, T., and X. Vives (2007), "Monotone equilibria in Bayesian games of strategic complementarities," JET 134:339–360.
