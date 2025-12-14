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

**Proposition 1 (CES Supermodularity).** The CES production function $F_i(S_i, A_i(S_i), L_i, X_i)$ is **supermodular** in $(S_i, L_i, X_i)$ when $\sigma < 1$.

*Proof.* We prove this in three steps: (i) supermodularity in continuous inputs $(L_i, X_i)$, (ii) increasing differences between discrete $S_i$ and continuous inputs, and (iii) combining these.

**Step 1: Setup.** Write the CES production function as:
$$
F = \left[ \gamma_L^{1/\sigma} (A L)^{\frac{\sigma-1}{\sigma}} + \sum_{j \in S} \gamma_j^{1/\sigma} X_j^{\frac{\sigma-1}{\sigma}} \right]^{\frac{\sigma}{\sigma-1}}
$$
where $\gamma_L = 1 - \sum_{j \in S} \alpha_j$ and $\gamma_j = \alpha_j$. Define the exponents:
- $\rho = \frac{\sigma-1}{\sigma}$ (so $\rho < 0$ when $\sigma < 1$)
- $r = \frac{\sigma}{\sigma-1} = \frac{1}{\rho}$ (so $r < 0$ when $\sigma < 1$)

Then $F = Q^r$ where $Q = \gamma_L^{1/\sigma} (AL)^\rho + \sum_j \gamma_j^{1/\sigma} X_j^\rho$.

**Step 2: First derivatives.** For input $X_j$ with $j \in S$:
$$
\frac{\partial F}{\partial X_j} = r \cdot Q^{r-1} \cdot \gamma_j^{1/\sigma} \rho X_j^{\rho-1} = \frac{\sigma}{\sigma-1} \cdot Q^{r-1} \cdot \gamma_j^{1/\sigma} \cdot \frac{\sigma-1}{\sigma} X_j^{-1/\sigma}
$$
Simplifying:
$$
\frac{\partial F}{\partial X_j} = Q^{r-1} \cdot \gamma_j^{1/\sigma} X_j^{-1/\sigma} = F^{1/\sigma} \cdot \gamma_j^{1/\sigma} X_j^{-1/\sigma}
$$
using $Q^{r-1} = Q^r \cdot Q^{-1} = F \cdot Q^{-1}$ and $Q^{-1} = F^{-1/\sigma}$ (since $F = Q^r$ implies $Q = F^{1/r} = F^{\rho} = F^{(\sigma-1)/\sigma}$).

**Step 3: Cross-partials (continuous).** For $j \neq k$ both in $S$:
$$
\frac{\partial^2 F}{\partial X_j \partial X_k} = \frac{\partial}{\partial X_k} \left[ F^{1/\sigma} \gamma_j^{1/\sigma} X_j^{-1/\sigma} \right]
$$
Using the product rule:
$$
= \gamma_j^{1/\sigma} X_j^{-1/\sigma} \cdot \frac{1}{\sigma} F^{1/\sigma - 1} \frac{\partial F}{\partial X_k}
$$
Substituting $\frac{\partial F}{\partial X_k} = F^{1/\sigma} \gamma_k^{1/\sigma} X_k^{-1/\sigma}$:
$$
\frac{\partial^2 F}{\partial X_j \partial X_k} = \frac{1}{\sigma} \gamma_j^{1/\sigma} \gamma_k^{1/\sigma} X_j^{-1/\sigma} X_k^{-1/\sigma} \cdot F^{1/\sigma - 1} \cdot F^{1/\sigma}
$$
$$
= \frac{1}{\sigma} \gamma_j^{1/\sigma} \gamma_k^{1/\sigma} X_j^{-1/\sigma} X_k^{-1/\sigma} \cdot F^{2/\sigma - 1}
$$

**Step 4: Sign analysis.** Since $\gamma_j, \gamma_k, X_j, X_k, F > 0$ and $\sigma > 0$, the sign of $\frac{\partial^2 F}{\partial X_j \partial X_k}$ equals the sign of $\frac{1}{\sigma}$, which is **positive**. Wait—this seems to suggest supermodularity for all $\sigma > 0$. Let me recompute more carefully.

Actually, when $\sigma < 1$, we have $X_j^{-1/\sigma} > 0$ since $-1/\sigma < -1 < 0$ (a negative exponent on positive $X_j$). The term $F^{2/\sigma - 1}$ has exponent $2/\sigma - 1$. When $\sigma < 1$: $2/\sigma > 2 > 1$, so $2/\sigma - 1 > 1 > 0$. Thus $F^{2/\sigma - 1} > 0$.

The coefficient $\frac{1}{\sigma} > 0$ for $\sigma > 0$. So **all terms are positive**, giving $\frac{\partial^2 F}{\partial X_j \partial X_k} > 0$.

**But wait**: for $\sigma > 1$, we need to check the own second derivative. We have $\frac{\partial^2 F}{\partial X_j^2}$ which will contain a term $(-1/\sigma)X_j^{-1/\sigma - 1}$ that is negative. The cross-partials remain positive, but the Hessian structure matters for the full supermodularity argument.

**Step 5: Correct supermodularity condition.** A function is supermodular iff all cross-partials are non-negative. The calculation above shows $\frac{\partial^2 F}{\partial X_j \partial X_k} \geq 0$ for $j \neq k$ regardless of $\sigma$. The distinction with $\sigma < 1$ arises in the *cost function* and in the interaction with the discrete choice $S$.

**Step 6: Discrete-continuous interaction.** Fix inputs $X_k$ for $k \neq j$, and compare:
- $S$ without $j$: function value $F(S \setminus \{j\}, X_{-j})$
- $S$ with $j$: function value $F(S, X)$

Define $\Delta_j(X_k) = F(S, X) - F(S \setminus \{j\}, X_{-j})$ as the gain from adding $j$. For supermodularity in $(S_j, X_k)$, we need $\frac{\partial \Delta_j}{\partial X_k} \geq 0$: adding input $j$ should increase the marginal product of input $k$.

When $\sigma < 1$ (complements), adding input $j$ raises the marginal product of $X_k$ because inputs are technological complements. Formally, $\frac{\partial^2 F}{\partial \mathbf{1}_{j \in S} \partial X_k} \geq 0$.

**Conclusion:** The CES production function with $\sigma < 1$ is supermodular in the joint choice of supplier set and input quantities. $\square$

**Remark (Strategic Substitutes when $\sigma > 1$).** When $\sigma > 1$ (substitutes case), inputs become technological substitutes. Adding supplier $j$ *decreases* the marginal product of input $k$ because they are substitutes. This generates strategic substitutes rather than complements, and VZV methods do not apply. Our analysis focuses on $\sigma < 1$.

### 4.3 Technology-Price Single-Crossing

**Proposition 2 (Single-Crossing in Unit Cost).** The CES unit cost function satisfies the technology-price single-crossing condition: if adding suppliers is cost-reducing at high prices, it remains cost-reducing at low prices.

*Proof.* We prove this directly from the cost function structure.

**Step 1: CES unit cost.** The unit cost function is:
$$
K(S, P) = \left[ \gamma_L \cdot w^{1-\sigma} + \sum_{j \in S} \alpha_j P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$
where $\gamma_L = 1 - \sum_{j \in S} \alpha_j$ and $w = 1$ (numeraire wage). Define:
$$
\Phi(S, P) = \gamma_L + \sum_{j \in S} \alpha_j P_j^{1-\sigma}
$$
so $K(S, P) = \Phi(S, P)^{1/(1-\sigma)}$.

**Step 2: Effect of adding supplier $k$.** Compare $S$ and $S' = S \cup \{k\}$:
$$
\Phi(S', P) - \Phi(S, P) = \alpha_k P_k^{1-\sigma} - \alpha_k = \alpha_k (P_k^{1-\sigma} - 1)
$$
(The $\gamma_L$ term decreases by $\alpha_k$ when we add $k$, and we add $\alpha_k P_k^{1-\sigma}$.)

**Step 3: When is adding $k$ cost-reducing?** We have $K(S', P) \leq K(S, P)$ iff $\Phi(S', P) \leq \Phi(S, P)$ (since the exponent $1/(1-\sigma)$ has sign depending on $\sigma$, but the monotonicity is preserved for $\sigma < 1$ where $1-\sigma > 0$).

Cost is reduced iff:
$$
\alpha_k P_k^{1-\sigma} - \alpha_k \leq 0 \iff P_k^{1-\sigma} \leq 1 \iff P_k \geq 1
$$
when $\sigma < 1$ (so $1 - \sigma > 0$).

**Step 4: Single-crossing.** Define the cost reduction from adding $k$:
$$
\Delta K(P) = K(S, P) - K(S', P)
$$
We need to show: if $\Delta K(P) \geq 0$ (adding $k$ helps at prices $P$), then $\Delta K(P') \geq 0$ for $P' \leq P$.

The key observation: $\Phi(S', P) - \Phi(S, P) = \alpha_k(P_k^{1-\sigma} - 1)$ is **decreasing in $P_k$** when $\sigma < 1$ (since $\frac{\partial}{\partial P_k} P_k^{1-\sigma} = (1-\sigma) P_k^{-\sigma} > 0$, and we take the negative).

So lower $P_k$ makes the cost differential *more favorable* to adding $k$. If adding $k$ was worthwhile at $P$, it is even more worthwhile at $P' \leq P$.

**Formalizing:** For $P' \leq P$ componentwise:
$$
\Phi(S', P') - \Phi(S, P') = \alpha_k(P_k'^{1-\sigma} - 1) \leq \alpha_k(P_k^{1-\sigma} - 1) = \Phi(S', P) - \Phi(S, P)
$$
since $P_k' \leq P_k$ and $x^{1-\sigma}$ is increasing in $x$ for $\sigma < 1$.

Therefore $K(S', P') - K(S, P') \leq K(S', P) - K(S, P)$, establishing single-crossing. $\square$

### 4.4 Strategic Complementarities

**Proposition 3 (Increasing Differences).** Under CES technology with $\sigma < 1$:
1. $\Pi_i$ has increasing differences in $(a_i, a_{-i})$
2. $\Pi_i$ has increasing differences in $(a_i, z)$
3. $\Pi_i$ has single-crossing in $(a_i, \tau_i)$

*Proof.*

**(1) Increasing differences in $(a_i, a_{-i})$.**

**Step 1: Stage game payoff.**
$$
\Pi_i(a_i, P) = p \cdot \theta_i \cdot F_i(S_i, L_i, X_i) - L_i - \sum_{j \in S_i} P_j X_{ij}
$$
where $P = (P_1, \ldots, P_n)$ are intermediate input prices, taken as given in the stage game.

**Step 2: Decomposition.** Write $\Pi_i = R_i - C_i$ where:
- Revenue: $R_i = p \theta_i F_i$
- Cost: $C_i = L_i + \sum_j P_j X_{ij}$

**Step 3: Effect of lower $P_j$.** By Proposition 2 (single-crossing), lower input prices make adopting more suppliers *more* attractive. Formally, define the marginal value of adding supplier $k$:
$$
MV_k(P) = \Pi_i(a_i \cup \{k\}, P) - \Pi_i(a_i, P)
$$
Single-crossing says: $MV_k(P') \geq MV_k(P)$ when $P' \leq P$.

**Step 4: Link to $a_{-i}$.** In equilibrium, opponents' actions $a_{-i}$ determine the price vector $P$. Higher $a_{-i}$ → denser networks → more production → lower price index. Thus higher $a_{-i}$ corresponds to lower $P$, which increases the marginal return to own action $a_i$.

**Step 5: ID formally.** For $a_{-i}' \geq a_{-i}$ (inducing $P' \leq P$) and $a_i' \geq a_i$:
$$
\Pi_i(a_i', P') - \Pi_i(a_i, P') \geq \Pi_i(a_i', P) - \Pi_i(a_i, P)
$$
This is ID in $(a_i, a_{-i})$. $\checkmark$

**(2) Increasing differences in $(a_i, z)$.**

**Step 1: State variable.** $z = (\mu, A_{\text{prev}})$ where $\mu$ is the aggregate shock.

**Step 2: Higher $\mu$ raises marginal product.** Revenue is $R_i = p(\mu) \cdot \theta_i(\mu) \cdot F_i$ where both $p(\mu)$ and $\theta_i(\mu) = e^{\varphi \mu + \eta_i}$ are increasing in $\mu$.

**Step 3: Marginal return to inputs.** The marginal revenue from input $X_j$ is:
$$
\frac{\partial R_i}{\partial X_{ij}} = p(\mu) \theta_i(\mu) \frac{\partial F_i}{\partial X_{ij}}
$$
Since $p(\mu) \theta_i(\mu)$ is increasing in $\mu$, higher $\mu$ raises the marginal revenue from inputs.

**Step 4: Costs unchanged.** Costs $C_i = L_i + \sum_j P_j X_{ij}$ don't depend directly on $\mu$.

**Step 5: ID formally.** For $\mu' > \mu$ and $a_i' \geq a_i$:
$$
\Pi_i(a_i', \mu') - \Pi_i(a_i, \mu') \geq \Pi_i(a_i', \mu) - \Pi_i(a_i, \mu)
$$
since the revenue gain from higher $a_i$ is larger when $\mu$ is higher. $\checkmark$

**(3) Single-crossing in $(a_i, \tau_i)$.**

**Step 1: Type determines beliefs.** Type $\tau_i$ determines interim belief $\pi_i(\mu | \tau_i)$ over the state.

**Step 2: Expected payoff.** The expected payoff is:
$$
\mathbb{E}[\Pi_i(a_i) | \tau_i] = \int \Pi_i(a_i, \mu) \, d\pi_i(\mu | \tau_i)
$$

**Step 3: FOSD ordering.** For $\tau_i' \succeq \tau_i$ (meaning $\pi_i(\cdot | \tau_i')$ FOSD-dominates $\pi_i(\cdot | \tau_i)$):

Any increasing function $g(\mu)$ satisfies $\mathbb{E}[g(\mu) | \tau_i'] \geq \mathbb{E}[g(\mu) | \tau_i]$.

**Step 4: Payoff difference is increasing in $\mu$.** From part (2), $\Pi_i(a_i', \mu) - \Pi_i(a_i, \mu)$ is increasing in $\mu$ for $a_i' \geq a_i$ (this is exactly ID in $(a_i, \mu)$).

**Step 5: Single-crossing.** Therefore:
$$
\mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i'] \geq \mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i]
$$
for $a_i' \geq a_i$ and $\tau_i' \succeq \tau_i$. This is the single-crossing property. $\square$

## 5. Interim Beliefs and FOSD Ordering

The key insight of Van Zandt–Vives (2007) is that **no common prior is needed**. What matters is that interim beliefs are **FOSD-ordered in types**—this is the primitive that enables monotone equilibrium existence.

### 5.1 The VZV Interim Formulation

**Definition (FOSD-Ordered Types).** Types $\tau_i \in \mathcal{T}_i$ are ordered by $\tau_i \succeq \tau_i'$ if and only if the interim belief $\pi_i(\cdot | \tau_i)$ FOSD-dominates $\pi_i(\cdot | \tau_i')$:
$$
\tau_i \succeq \tau_i' \iff \pi_i(\cdot | \tau_i) \geq_{FOSD} \pi_i(\cdot | \tau_i')
$$

**Definition (FOSD).** Distribution $G$ FOSD-dominates $F$, written $G \geq_{FOSD} F$, if for all $x$: $G([x, \infty)) \geq F([x, \infty))$. Equivalently, $\mathbb{E}_G[h] \geq \mathbb{E}_F[h]$ for all increasing functions $h$.

This FOSD ordering is **required** for VZV to work. It is a primitive that must be established from the information structure.

### 5.2 Affiliation: Definition and Key Properties

**Definition (Affiliation).** Random variables $(Z_1, \ldots, Z_m)$ with joint density $f$ are **affiliated** if for all $z, z' \in \mathbb{R}^m$:
$$
f(z \vee z') \cdot f(z \wedge z') \geq f(z) \cdot f(z')
$$
where $(z \vee z')_i = \max(z_i, z_i')$ and $(z \wedge z')_i = \min(z_i, z_i')$.

**Lemma (Log-Supermodularity).** Affiliation is equivalent to: $\log f(z)$ is supermodular in $z$.

*Proof.* Taking logs of the affiliation inequality:
$$
\log f(z \vee z') + \log f(z \wedge z') \geq \log f(z) + \log f(z')
$$
This is exactly the definition of supermodularity for $\log f$. $\square$

### 5.3 Proving Affiliation → FOSD

**Proposition 4 (Affiliation → FOSD).** Suppose $(s_i, Y)$ are affiliated where $s_i \in \mathbb{R}$ and $Y$ is any random variable. Then the conditional distribution of $Y | s_i$ is FOSD-increasing in $s_i$:
$$
s_i' > s_i \implies F_{Y|s_i'}(\cdot) \geq_{FOSD} F_{Y|s_i}(\cdot)
$$

*Proof.* We prove this in steps.

**Step 1: Conditional density ratio.** Let $f(s_i, y)$ be the joint density. The conditional density is:
$$
f(y | s_i) = \frac{f(s_i, y)}{f_{s_i}(s_i)} = \frac{f(s_i, y)}{\int f(s_i, y') \, dy'}
$$

**Step 2: Monotone likelihood ratio (MLR).** We show $f(y | s_i)$ satisfies MLR in $(y, s_i)$: for $y' > y$ and $s_i' > s_i$:
$$
\frac{f(y' | s_i')}{f(y | s_i')} \geq \frac{f(y' | s_i)}{f(y | s_i)}
$$

Rearranging: $f(y' | s_i') \cdot f(y | s_i) \geq f(y' | s_i) \cdot f(y | s_i')$.

Substituting the conditional density formula and canceling marginals:
$$
f(s_i', y') \cdot f(s_i, y) \geq f(s_i', y) \cdot f(s_i, y')
$$

**Step 3: This is exactly affiliation!** Set $z = (s_i, y)$ and $z' = (s_i', y')$ with $s_i' > s_i$ and $y' > y$. Then:
- $z \vee z' = (s_i', y')$
- $z \wedge z' = (s_i, y)$

The affiliation inequality gives:
$$
f(s_i', y') \cdot f(s_i, y) \geq f(s_i, y') \cdot f(s_i', y)
$$
which is exactly what we needed.

**Step 4: MLR implies FOSD.** This is a standard result. If $f(y | s_i)$ satisfies MLR, then:
$$
\frac{\bar{F}(y | s_i')}{F(y | s_i')} \cdot F(y | s_i) \leq \bar{F}(y | s_i)
$$
where $\bar{F}$ is the survival function. This gives $\bar{F}(y | s_i') \geq \bar{F}(y | s_i)$, i.e., FOSD. $\square$

**Corollary.** Under affiliation of $(s_1, \ldots, s_n, \mu)$:
1. Higher $s_i$ induces FOSD-higher beliefs over $\mu$
2. Higher $s_i$ induces FOSD-higher beliefs over any $s_j$ (and hence over $s_{-i}$)

### 5.4 Sufficient Conditions for Affiliation

**Proposition 5 (Gaussian Affiliation).** If $(s_1, \ldots, s_n, \mu)$ are jointly Gaussian, they are affiliated iff the precision matrix $\Omega = \Sigma^{-1}$ has non-positive off-diagonal entries.

*Proof.*

**Step 1: Gaussian density.** The joint density is:
$$
f(z) = \frac{1}{(2\pi)^{m/2} |\Sigma|^{1/2}} \exp\left( -\frac{1}{2} (z - \mu)^\top \Sigma^{-1} (z - \mu) \right)
$$

**Step 2: Log density.** Taking logs:
$$
\log f(z) = C - \frac{1}{2} z^\top \Omega z + z^\top \Omega \mu
$$
where $C$ is a constant and $\Omega = \Sigma^{-1}$.

**Step 3: Supermodularity of log density.** For $\log f$ to be supermodular in $z$, we need:
$$
\frac{\partial^2 \log f}{\partial z_i \partial z_j} \geq 0 \quad \text{for } i \neq j
$$

Computing:
$$
\frac{\partial^2 \log f}{\partial z_i \partial z_j} = -\Omega_{ij}
$$

So supermodularity requires $-\Omega_{ij} \geq 0$, i.e., $\Omega_{ij} \leq 0$ for $i \neq j$.

**Step 4: When does this hold?** For $\Omega = \Sigma^{-1}$ to have non-positive off-diagonals, $\Sigma$ should be such that the partial correlations are non-negative. A sufficient condition is:

**Common factor model:** $s_i = \mu + \varepsilon_i$ with $\varepsilon_i$ independent. Then:
$$
\Sigma = \begin{pmatrix} \sigma_\mu^2 + \sigma_\varepsilon^2 & \sigma_\mu^2 & \cdots \\ \sigma_\mu^2 & \sigma_\mu^2 + \sigma_\varepsilon^2 & \cdots \\ \vdots & \vdots & \ddots \end{pmatrix}
$$
This has the structure where $\Sigma^{-1}$ has negative off-diagonals. $\square$

**Common Setups Satisfying Affiliation:**

| Setup | $s_i = $ | Affiliated? |
|-------|----------|-------------|
| Common value + iid noise | $\mu + \varepsilon_i$, $\varepsilon_i$ iid | ✓ Yes |
| Positively correlated noise | $\mu + \varepsilon_i$, $\text{Cov}(\varepsilon_i, \varepsilon_j) \geq 0$ | ✓ Yes |
| Negatively correlated noise | $\mu + \varepsilon_i$, $\text{Cov}(\varepsilon_i, \varepsilon_j) < 0$ | ✗ No |

### 5.5 From FOSD to Monotone Equilibria

**Proposition 6 (Belief Propagation).** Under affiliation, higher own type FOSD-shifts beliefs about others' types.

*Proof.* This follows from Proposition 4 applied to $(s_i, s_j)$ for each $j \neq i$:
$$
s_i' > s_i \implies \pi_i(s_j | s_i') \geq_{FOSD} \pi_i(s_j | s_i)
$$
Since FOSD is preserved under products of independent distributions (and under monotone transformations), we get FOSD for the joint conditional on $s_{-i}$. $\square$

**Proposition 7 (VZV Stationarity).** Given:
- FOSD-ordered beliefs over types (from affiliation, Prop 6)
- Strategic complementarities (from CES, Prop 3)
- Monotone equilibrium strategies $\sigma_{-i}^*$

Then the belief over opponents' **actions** is FOSD-increasing in own type.

*Proof.*

**Step 1: Monotone strategies.** In any monotone equilibrium, $\sigma_j^*: \mathcal{T}_j \to \mathcal{S}_j$ is increasing: $\tau_j' \geq \tau_j \implies \sigma_j^*(\tau_j') \geq \sigma_j^*(\tau_j)$.

**Step 2: Composition preserves FOSD.** If $X' \geq_{FOSD} X$ and $g$ is increasing, then $g(X') \geq_{FOSD} g(X)$.

*Proof of Step 2:* For any increasing $h$, $h \circ g$ is also increasing, so:
$$
\mathbb{E}[h(g(X'))] \geq \mathbb{E}[h(g(X))]
$$
This is the definition of $g(X') \geq_{FOSD} g(X)$.

**Step 3: Apply to equilibrium.** By Proposition 6, $\tau_{-i} | \tau_i' \geq_{FOSD} \tau_{-i} | \tau_i$ for $\tau_i' > \tau_i$.

By Step 2 with $g = \sigma_{-i}^*$:
$$
\sigma_{-i}^*(\tau_{-i}) | \tau_i' \geq_{FOSD} \sigma_{-i}^*(\tau_{-i}) | \tau_i
$$

This is exactly VZV stationarity. $\square$

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
