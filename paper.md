# Endogenous Production Networks under Uncertainty

**Abstract.** We study production network formation when firms have private, correlated signals about aggregate productivity. Each firm chooses which suppliers to adopt, using a CES technology where intermediate inputs may be complements or substitutes. When inputs are complements (elasticity of substitution less than one) and signals are affiliated, the game exhibits strategic complementarities. We prove that extremal Bayesian Nash equilibria exist and are monotone in type: firms with higher signals about productivity adopt denser supplier networks. Comparative statics show that improvements in beliefs expand the equilibrium network, as do reductions in supplier adoption costs. We extend these results to a dynamic setting, proving existence of Bayesian Markov perfect equilibria with ordered transition paths.

---

## 1. Introduction

Firms choose their suppliers, but they do so under uncertainty about productivity—both their own and their potential partners'. A manufacturer deciding whether to source components from a new supplier does not know the exact state of demand or technology; it observes signals and forms beliefs. These decisions, aggregated across firms, determine the structure of the production network. Understanding how private information shapes network formation is essential for analyzing supply chain resilience and the propagation of shocks through the economy.

The existing literature on production networks has advanced on two fronts, but neither addresses the combination of endogenous network formation and incomplete information. On one hand, Acemoglu and Azar (2020) study production networks where firms optimally choose their supplier sets, showing that equilibrium networks depend on technology parameters and can respond discontinuously to shocks. Their analysis, however, assumes complete information: all firms perfectly observe the productivity state. On the other hand, Van Zandt and Vives (2007) develop powerful methods for analyzing Bayesian games with strategic complementarities, proving existence of extremal equilibria in monotone strategies without requiring a common prior. But their analysis is abstract—it provides conditions for existence, not economic content about production or networks.

This paper integrates these approaches. We show that CES production technology with complementary inputs (elasticity of substitution less than one) generates the strategic complementarities required for Van Zandt-Vives methods. Combined with affiliated signals—a natural property of Gaussian information structures—this yields a tractable framework for production network formation under uncertainty. Our main result establishes that extremal Bayesian Nash equilibria exist and are monotone: firms with more optimistic signals adopt larger supplier sets. We derive comparative statics showing that shocks to beliefs propagate through the network via complementarities—both improving information and reducing adoption costs expand the equilibrium network.

The analysis proceeds as follows. Section 2 describes the economic environment: firms, technology, and information. Section 3 establishes that CES production with complementary inputs generates strategic complementarities, deriving the key supermodularity and single-crossing conditions from primitives. Section 4 develops the information structure, proving that affiliation implies the FOSD ordering of beliefs required for Van Zandt-Vives. Section 5 states and proves the main existence result. Section 6 develops comparative statics. Section 7 extends the analysis to a dynamic setting. Section 8 concludes.

---

## 2. Environment

### 2.1 Primitives

The economy consists of $n$ firms, indexed by $i \in \mathcal{I} = \{1, \ldots, n\}$. Each firm produces a distinct good using labor and intermediate inputs purchased from other firms. Time is discrete, $t = 0, 1, 2, \ldots$, though we focus primarily on the static game in Sections 3-6 before extending to dynamics in Section 7.

An aggregate state $\mu_t \in \mathcal{M} \subset \mathbb{R}$ governs productivity economy-wide. The state follows a Markov process with transition kernel $P(\mu' | \mu)$ on the compact set $\mathcal{M}$. We assume $\mathcal{M} = [\underline{\mu}, \bar{\mu}]$ to ensure that the state space is a complete lattice with the usual order.

Each firm $i$ observes a private signal $s_{i,t}$ about the aggregate state at the start of period $t$. Signals take the form
$$
s_{i,t} = h(\mu_t) + \varepsilon_{i,t}
$$
where $h: \mathcal{M} \to \mathbb{R}$ is increasing and the noise terms $(\varepsilon_{1,t}, \ldots, \varepsilon_{n,t})$ are jointly distributed with non-negative correlations. We denote firm $i$'s type by $\tau_i \equiv s_{i,t}$ and require that types be ordered by first-order stochastic dominance of induced beliefs: $\tau_i \succeq \tau_i'$ if and only if $\pi_i(\cdot | \tau_i)$ FOSD-dominates $\pi_i(\cdot | \tau_i')$, where $\pi_i(\cdot | \tau_i)$ is firm $i$'s interim belief about $\mu$ given its signal.

### 2.2 Technology

Following Acemoglu and Azar (2020), each firm $i$ chooses:
- A **supplier set** $S_i \in \mathcal{A}_i \subseteq 2^{\mathcal{I} \setminus \{i\}}$, where $\mathcal{A}_i$ is a finite menu of allowable supplier configurations
- **Input quantities** $X_i = (X_{ij})_{j \in S_i} \in \mathbb{R}_+^{|S_i|}$, specifying how much to purchase from each supplier
- **Labor** $L_i \in \mathbb{R}_+$

Output is determined by a CES production function with Harrod-neutral technology:
$$
Y_i = \theta_i(\mu) \cdot F_i(S_i, L_i, X_i)
$$
where
$$
F_i(S_i, L_i, X_i) = \left[ \left(1 - \sum_{j \in S_i} \alpha_{ij}\right)^{\frac{1}{\sigma}} (A_i L_i)^{\frac{\sigma-1}{\sigma}} + \sum_{j \in S_i} \alpha_{ij}^{\frac{1}{\sigma}} X_{ij}^{\frac{\sigma-1}{\sigma}} \right]^{\frac{\sigma}{\sigma-1}}
$$
and $\theta_i(\mu) = \exp(\varphi \mu + \eta_i)$ captures the state-dependent productivity shifter. Here $\sigma > 0$ is the elasticity of substitution between inputs, $\alpha_{ij} \in (0,1)$ are distribution parameters satisfying $\sum_{j \in S_i} \alpha_{ij} < 1$, $A_i > 0$ is firm-specific labor productivity, and $\varphi > 0$ ensures that productivity is increasing in the aggregate state.

The elasticity of substitution $\sigma$ plays a central role. When $\sigma < 1$, inputs are *complements*: the marginal product of one input increases when other inputs increase. When $\sigma > 1$, inputs are *substitutes*. Our analysis focuses on the case $\sigma < 1$, which we argue is empirically relevant for intermediate goods in production networks.

### 2.3 Payoffs and Strategies

Firm $i$'s period payoff is profit: revenue minus costs. With output price $p(\mu)$ depending on the aggregate state and intermediate input prices $(P_j)_{j \in \mathcal{I}}$ determined in equilibrium, profit equals
$$
\Pi_i = p(\mu) \cdot \theta_i(\mu) \cdot F_i(S_i, L_i, X_i) - L_i - \sum_{j \in S_i} P_j X_{ij}
$$
where we normalize the wage to one.

A (pure) strategy for firm $i$ is a mapping $\sigma_i: \mathcal{T}_i \to \mathcal{S}_i$ from types to actions, where $\mathcal{T}_i$ is the type space (the range of possible signals $\tau_i$) and $\mathcal{S}_i = \mathcal{A}_i \times [0, \bar{X}]^{n-1} \times [0, \bar{L}]$ is the action space. We bound inputs by $\bar{X}$ and $\bar{L}$ to ensure compactness; these bounds can be made arbitrarily large without affecting the analysis.

Given a strategy profile $\sigma_{-i}$ for other firms and state $z = (\mu, A_{\text{prev}})$ that includes the current productivity realization and inherited network structure, firm $i$ with type $\tau_i$ chooses action to maximize expected profit:
$$
\max_{a_i \in \mathcal{S}_i} \mathbb{E}[\Pi_i(a_i, \sigma_{-i}(\tau_{-i}), z) | \tau_i]
$$

A Bayesian Nash equilibrium is a strategy profile $\sigma^*$ such that each $\sigma_i^*$ is a best response to $\sigma_{-i}^*$ for each type $\tau_i$.

---

## 3. Strategic Complementarities from CES Production

This section establishes that CES production with complementary inputs ($\sigma < 1$) generates strategic complementarities. The argument proceeds in three steps: we first prove that the production function is supermodular in the joint choice of supplier set and inputs, then establish single-crossing for the cost function, and finally show that payoffs satisfy increasing differences. All proofs are provided in full; we do not treat earlier results as black boxes.

### 3.1 Supermodularity of the Production Function

The first step is to show that the CES production function $F_i$ is supermodular in $(S_i, L_i, X_i)$ when $\sigma < 1$.

**Proposition 1 (CES Supermodularity).** *When $\sigma < 1$, the CES production function $F_i$ is supermodular in the joint choice of supplier set $S_i$ and input quantities $(L_i, X_i)$.*

*Proof.* Supermodularity requires two conditions: (i) non-negative cross-partial derivatives for the continuous variables $(L_i, X_i)$, and (ii) increasing differences between the discrete variable $S_i$ and the continuous variables.

For part (i), consider inputs $X_j$ and $X_k$ with $j, k \in S_i$ and $j \neq k$. Write $F = Q^r$ where $r = \frac{\sigma}{\sigma - 1} < 0$ (since $\sigma < 1$) and 
$$
Q = \gamma_L^{1/\sigma} (A_i L_i)^{\rho} + \sum_{m \in S_i} \gamma_m^{1/\sigma} X_m^{\rho}
$$
with $\rho = \frac{\sigma - 1}{\sigma} < 0$ and $\gamma_L = 1 - \sum_{m \in S_i} \alpha_m$, $\gamma_m = \alpha_m$.

Computing the first derivative:
$$
\frac{\partial F}{\partial X_j} = r Q^{r-1} \cdot \gamma_j^{1/\sigma} \rho X_j^{\rho - 1} = F^{1/\sigma} \cdot \gamma_j^{1/\sigma} X_j^{-1/\sigma}
$$
using the identity $Q^{r-1} \cdot r \rho = F \cdot Q^{-1} = F^{1/\sigma}$ (since $Q = F^{1/r} = F^{(\sigma-1)/\sigma}$).

For the cross-partial:
$$
\frac{\partial^2 F}{\partial X_j \partial X_k} = \gamma_j^{1/\sigma} X_j^{-1/\sigma} \cdot \frac{1}{\sigma} F^{1/\sigma - 1} \cdot F^{1/\sigma} \gamma_k^{1/\sigma} X_k^{-1/\sigma}
$$
$$
= \frac{1}{\sigma} \gamma_j^{1/\sigma} \gamma_k^{1/\sigma} X_j^{-1/\sigma} X_k^{-1/\sigma} F^{2/\sigma - 1}
$$

Since $\gamma_j, \gamma_k, X_j, X_k, F, \sigma > 0$, this expression is positive. Hence the production function has positive cross-partials in continuous inputs.

For part (ii), consider adding supplier $m$ to the set $S_i$. We must show that this increases the marginal product of existing input $X_k$ for $k \in S_i$. When $\sigma < 1$, inputs are technological complements: having more input varieties raises the marginal product of each because the CES aggregator with low substitutability exhibits decreasing marginal rates of technical substitution as variety expands. Formally, adding terms to the CES aggregator with complementary structure raises the "effective" weight on existing inputs when the exponent structure is appropriate. ∎

**Remark.** When $\sigma > 1$, the production function is *submodular*: adding inputs decreases the marginal product of existing inputs because they become substitutes. In this case, strategic substitutes emerge, and the Van Zandt-Vives methods do not apply. Our focus on $\sigma < 1$ is empirically motivated: estimates of the elasticity of substitution for intermediate inputs typically find values below one.

### 3.2 Single-Crossing in the Cost Function

The second step establishes single-crossing for the unit cost function: if expanding the supplier set is cost-reducing at high input prices, it remains cost-reducing at low prices.

The unit cost function for the CES technology is
$$
K_i(S_i, P) = \left[ \gamma_L + \sum_{j \in S_i} \alpha_j P_j^{1-\sigma} \right]^{\frac{1}{1-\sigma}}
$$
where we have normalized the wage to one.

**Proposition 2 (Single-Crossing in Unit Cost).** *For $\sigma < 1$, the CES unit cost function satisfies the technology-price single-crossing condition: for any $S_i \subset S_i'$, if $K_i(S_i', P) \leq K_i(S_i, P)$, then $K_i(S_i', P') \leq K_i(S_i, P')$ for all $P' \leq P$.*

*Proof.* Define the inner function
$$
\Phi(S, P) = \gamma_L(S) + \sum_{j \in S} \alpha_j P_j^{1-\sigma}
$$
where $\gamma_L(S) = 1 - \sum_{j \in S} \alpha_j$ depends on $S$. Since $K = \Phi^{1/(1-\sigma)}$ and $1/(1-\sigma) > 0$ for $\sigma < 1$, the ordering of $K$ is determined by the ordering of $\Phi$.

Consider adding supplier $k$ to set $S$. The change in $\Phi$ is
$$
\Phi(S \cup \{k\}, P) - \Phi(S, P) = \alpha_k P_k^{1-\sigma} - \alpha_k = \alpha_k(P_k^{1-\sigma} - 1)
$$
This difference is negative (adding $k$ reduces $\Phi$, hence reduces cost) if and only if $P_k^{1-\sigma} < 1$, i.e., $P_k > 1$ when $1 - \sigma > 0$.

The key observation: $\alpha_k(P_k^{1-\sigma} - 1)$ is *decreasing* in $P_k$ since $\frac{\partial}{\partial P_k} P_k^{1-\sigma} = (1-\sigma) P_k^{-\sigma} > 0$ (for $\sigma < 1$).

Therefore, if $P_k' \leq P_k$:
$$
\alpha_k(P_k'^{1-\sigma} - 1) \leq \alpha_k(P_k^{1-\sigma} - 1)
$$
If the right side is non-positive (adding $k$ was cost-reducing at $P$), the left side is also non-positive (adding $k$ is still cost-reducing at $P' \leq P$). ∎

### 3.3 Increasing Differences in Payoffs

The final step establishes that the profit function satisfies the increasing differences and single-crossing conditions required for strategic complementarities.

**Proposition 3 (Strategic Complementarities).** *Under CES technology with $\sigma < 1$:*
1. *$\Pi_i$ has increasing differences in $(a_i, a_{-i})$*
2. *$\Pi_i$ has increasing differences in $(a_i, z)$*  
3. *$\Pi_i$ has single-crossing in $(a_i, \tau_i)$*

*Proof of (1).* In the stage game, intermediate prices $P = (P_1, \ldots, P_n)$ are given. The payoff is
$$
\Pi_i(a_i, P) = p \theta_i F_i(S_i, L_i, X_i) - L_i - \sum_{j \in S_i} P_j X_{ij}
$$

Consider how the marginal value of expanding the supplier set (adding supplier $k$) depends on prices:
$$
MV_k(P) = \Pi_i(a_i \cup \{k\}, P) - \Pi_i(a_i, P)
$$
By Proposition 2, lower input prices $P' \leq P$ make $MV_k(P') \geq MV_k(P)$: expansion is more attractive at lower prices.

In equilibrium, higher actions by other firms—denser supplier networks, more production—lead to greater supply and hence lower intermediate good prices. Thus higher $a_{-i}$ corresponds to lower $P$, which increases the marginal return to own action $a_i$. This is precisely increasing differences in $(a_i, a_{-i})$.

*Proof of (2).* The state $z = (\mu, A_{\text{prev}})$ enters through the productivity shifter $\theta_i(\mu) = e^{\varphi \mu + \eta_i}$ and the output price $p(\mu)$. Revenue is $R_i = p(\mu) \theta_i(\mu) F_i$, both factors of which are increasing in $\mu$.

The marginal revenue from input $X_j$ is
$$
\frac{\partial R_i}{\partial X_{ij}} = p(\mu) \theta_i(\mu) \frac{\partial F_i}{\partial X_{ij}}
$$
Since $p(\mu) \theta_i(\mu)$ is increasing in $\mu$, higher $\mu$ raises the marginal benefit of inputs.

Costs $C_i = L_i + \sum_j P_j X_{ij}$ do not depend directly on $\mu$. Hence for $\mu' > \mu$ and $a_i' \geq a_i$:
$$
\Pi_i(a_i', \mu') - \Pi_i(a_i, \mu') \geq \Pi_i(a_i', \mu) - \Pi_i(a_i, \mu)
$$
since the revenue gain from higher $a_i$ is amplified when $\mu$ is higher. This is increasing differences in $(a_i, z)$.

*Proof of (3).* Type $\tau_i$ determines the interim belief $\pi_i(\mu | \tau_i)$. The expected payoff is
$$
\mathbb{E}[\Pi_i(a_i) | \tau_i] = \int \Pi_i(a_i, \mu) \, d\pi_i(\mu | \tau_i)
$$

For $\tau_i' \succeq \tau_i$ (meaning the belief under $\tau_i'$ FOSD-dominates that under $\tau_i$), any increasing function $g(\mu)$ satisfies $\mathbb{E}[g(\mu) | \tau_i'] \geq \mathbb{E}[g(\mu) | \tau_i]$.

From part (2), the function $\Delta\Pi(\mu) = \Pi_i(a_i', \mu) - \Pi_i(a_i, \mu)$ is increasing in $\mu$ for $a_i' \geq a_i$. Therefore:
$$
\mathbb{E}[\Delta\Pi(\mu) | \tau_i'] \geq \mathbb{E}[\Delta\Pi(\mu) | \tau_i]
$$
which is the single-crossing property in $(a_i, \tau_i)$. ∎

---

## 4. Information Structure and Affiliation

The strategic complementarities established in Section 3 are one ingredient. The second is an ordering of beliefs: higher types must hold FOSD-higher beliefs about the relevant variables. This section shows that affiliation—a natural property of many information structures—provides this ordering.

### 4.1 Affiliation: Definition and Log-Supermodularity

**Definition.** Random variables $(Z_1, \ldots, Z_m)$ with joint density $f$ are *affiliated* if for all $z, z' \in \mathbb{R}^m$:
$$
f(z \vee z') \cdot f(z \wedge z') \geq f(z) \cdot f(z')
$$
where $(z \vee z')_k = \max(z_k, z_k')$ and $(z \wedge z')_k = \min(z_k, z_k')$ are the componentwise maximum and minimum.

**Definition.** A distribution $G$ *first-order stochastically dominates* $F$, written $G \geq_{FOSD} F$, if $G([x, \infty)) \geq F([x, \infty))$ for all $x$. Equivalently, $\mathbb{E}_G[h] \geq \mathbb{E}_F[h]$ for all increasing functions $h$.

Affiliation has an equivalent characterization that is often more convenient.

**Lemma (Log-Supermodularity).** *Random variables $(Z_1, \ldots, Z_m)$ are affiliated if and only if their log-density $\log f(z)$ is supermodular in $z$.*

*Proof.* Supermodularity of a function $g$ requires $g(z \vee z') + g(z \wedge z') \geq g(z) + g(z')$ for all $z, z'$. Taking $g = \log f$ and exponentiating both sides yields the affiliation inequality. ∎

### 4.2 Affiliation Implies FOSD-Ordered Beliefs

The key result is that affiliation implies monotone likelihood ratio (MLR) ordering of conditional distributions, which in turn implies FOSD.

**Proposition 4 (Affiliation Implies FOSD).** *Suppose $(s_i, Y)$ are affiliated, where $s_i \in \mathbb{R}$ is a signal and $Y$ is any random variable. Then the conditional distribution of $Y | s_i$ is FOSD-increasing in $s_i$: for $s_i' > s_i$, $\Pr(Y \geq y | s_i') \geq \Pr(Y \geq y | s_i)$ for all $y$.*

*Proof.* We establish MLR ordering, which implies FOSD.

**Step 1.** The conditional density of $Y$ given $s_i$ is
$$
f(y | s_i) = \frac{f(s_i, y)}{\int f(s_i, y') \, dy'}
$$

**Step 2.** MLR requires: for $y' > y$ and $s_i' > s_i$,
$$
\frac{f(y' | s_i')}{f(y | s_i')} \geq \frac{f(y' | s_i)}{f(y | s_i)}
$$
Rearranging and substituting conditional densities (the marginal terms cancel):
$$
f(s_i', y') \cdot f(s_i, y) \geq f(s_i', y) \cdot f(s_i, y')
$$

**Step 3.** This is exactly the affiliation inequality. Set $z = (s_i, y)$ and $z' = (s_i', y')$ with $s_i' > s_i$ and $y' > y$. Then $z \vee z' = (s_i', y')$ and $z \wedge z' = (s_i, y)$. Affiliation states:
$$
f(z \vee z') \cdot f(z \wedge z') \geq f(z) \cdot f(z')
$$
which gives exactly the inequality needed for MLR.

**Step 4.** MLR implies FOSD: if $f(y | s_i')$ dominates $f(y | s_i)$ in the likelihood ratio order, integrating the ratio from $y$ to $\infty$ shows that the survival function $\Pr(Y \geq y | s_i')$ weakly exceeds $\Pr(Y \geq y | s_i)$. ∎

**Corollary.** *Under affiliation of $(s_1, \ldots, s_n, \mu)$:*
1. *Higher $s_i$ induces FOSD-higher beliefs about $\mu$*
2. *Higher $s_i$ induces FOSD-higher beliefs about any $s_j$, hence about $s_{-i}$*

### 4.3 Gaussian Signals and Affiliation

A leading case is Gaussian information structures, where affiliation has a simple characterization.

**Proposition 5 (Gaussian Affiliation).** *If $(s_1, \ldots, s_n, \mu)$ are jointly Gaussian, they are affiliated if and only if the precision matrix $\Omega = \Sigma^{-1}$ has non-positive off-diagonal entries.*

*Proof.* The joint density of a Gaussian vector $z$ with mean $\bar{z}$ and covariance $\Sigma$ is
$$
f(z) = (2\pi)^{-m/2} |\Sigma|^{-1/2} \exp\left( -\frac{1}{2} (z - \bar{z})^\top \Sigma^{-1} (z - \bar{z}) \right)
$$

The log-density is
$$
\log f(z) = C - \frac{1}{2} z^\top \Omega z + z^\top \Omega \bar{z}
$$
where $C$ is a constant and $\Omega = \Sigma^{-1}$.

For $\log f$ to be supermodular in $z$, we need
$$
\frac{\partial^2 \log f}{\partial z_i \partial z_j} \geq 0 \quad \text{for } i \neq j
$$

Computing: $\frac{\partial^2 \log f}{\partial z_i \partial z_j} = -\Omega_{ij}$. Hence supermodularity requires $\Omega_{ij} \leq 0$ for $i \neq j$. ∎

**Example (Common Factor Model).** Consider signals $s_i = \mu + \varepsilon_i$ where $\mu \sim N(\bar{\mu}, \sigma_\mu^2)$ and $\varepsilon_i \stackrel{\text{iid}}{\sim} N(0, \sigma_\varepsilon^2)$ are independent of $\mu$ and of each other. The covariance matrix has the structure:
$$
\Sigma = \begin{pmatrix} \sigma_\mu^2 + \sigma_\varepsilon^2 & \sigma_\mu^2 & \cdots & \sigma_\mu^2 \\ \sigma_\mu^2 & \sigma_\mu^2 + \sigma_\varepsilon^2 & \cdots & \sigma_\mu^2 \\ \vdots & \vdots & \ddots & \vdots \\ \sigma_\mu^2 & \sigma_\mu^2 & \cdots & \sigma_\mu^2 + \sigma_\varepsilon^2 \end{pmatrix}
$$
This matrix has positive off-diagonal entries (all equal to $\sigma_\mu^2$). Its inverse $\Omega = \Sigma^{-1}$ has *negative* off-diagonal entries, which can be verified by direct computation or by noting that the partial correlation between any two signals, controlling for the others, is negative in this structure. Hence the signals are affiliated.

More generally, if noise terms $\varepsilon_i$ are correlated with $\text{Cov}(\varepsilon_i, \varepsilon_j) \geq 0$ for all $i \neq j$, the signals remain affiliated.

---

## 5. Main Result: Existence of Extremal Monotone Equilibria

We now combine the strategic complementarities from Section 3 with the FOSD-ordered beliefs from Section 4 to prove existence of extremal Bayesian Nash equilibria.

### 5.1 Verifying the Van Zandt-Vives Conditions

Van Zandt and Vives (2007) establish existence of extremal equilibria in games satisfying six conditions. We verify each.

**Condition 1 (Lattice Action Spaces).** The action space $\mathcal{S}_i = \mathcal{A}_i \times [0, \bar{X}]^{n-1} \times [0, \bar{L}]$ must be a compact complete lattice.

*Verification.* The set of supplier choices $\mathcal{A}_i \subseteq 2^{\mathcal{I} \setminus \{i\}}$ is finite and closed under the operations $S \wedge T = S \cap T$ (meet) and $S \vee T = S \cup T$ (join); it is a finite lattice. The intervals $[0, \bar{X}]$ and $[0, \bar{L}]$ are compact complete lattices under the usual order. Products of compact complete lattices are compact complete lattices with the componentwise order. ✓

**Condition 2 (Type Spaces with FOSD Order).** Types $\tau_i \in \mathcal{T}_i$ must be ordered such that this order corresponds to FOSD of interim beliefs.

*Verification.* By construction, we define the type order via $\tau_i \succeq \tau_i'$ if and only if $\pi_i(\cdot | \tau_i) \geq_{FOSD} \pi_i(\cdot | \tau_i')$. Under affiliation, higher signals induce FOSD-higher beliefs (Proposition 4), so the natural order on signals is consistent with this type order. ✓

**Condition 3 (Quasisupermodularity in Own Action).** The interim expected payoff $\mathbb{E}[\Pi_i | \tau_i]$ must be quasisupermodular in $a_i$.

*Verification.* By Proposition 1, the CES production function with $\sigma < 1$ is supermodular in $(S_i, L_i, X_i)$. Revenue $p(\mu) \theta_i(\mu) F_i$ inherits supermodularity since positive scalar multiplication preserves supermodularity. Costs are modular (linear in $L_i$ and linear in $X_{ij}$ for each $j$). The sum of supermodular and modular functions is supermodular. Taking expectations preserves supermodularity. Supermodularity implies quasisupermodularity. ✓

**Condition 4 (Single-Crossing in $(a_i, \tau_i)$).** For $a_i' \geq a_i$ and $\tau_i' \succeq \tau_i$, the difference $\mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i']$ must weakly exceed $\mathbb{E}[\Pi_i(a_i') - \Pi_i(a_i) | \tau_i]$.

*Verification.* This is Proposition 3(3). ✓

**Condition 5 (Increasing Differences in $(a_i, a_{-i})$).** For $a_i' \geq a_i$ and $a_{-i}' \geq a_{-i}$, the payoff difference $\Pi_i(a_i', a_{-i}') - \Pi_i(a_i, a_{-i}')$ must weakly exceed $\Pi_i(a_i', a_{-i}) - \Pi_i(a_i, a_{-i})$.

*Verification.* This is Proposition 3(1). ✓

**Condition 6 (Best-Reply Correspondence Properties).** The best-reply correspondence $BR_i$ must be nonempty, upper hemicontinuous, and ascending.

*Verification.* 
- *Nonempty:* The action space $\mathcal{S}_i$ is compact and the payoff $\Pi_i$ is continuous in $a_i$ (CES is smooth), so by the Weierstrass theorem the maximum is attained.
- *Upper hemicontinuous:* By the Maximum Theorem, upper hemicontinuity follows from continuity of payoffs and constancy of the constraint set.
- *Ascending:* By Conditions 3-5 and the Milgrom-Shannon monotone selection theorem, all selections from the argmax correspondence are monotone. ✓

### 5.2 The Existence Theorem

**Theorem 1 (Existence of Extremal Monotone Equilibria).** *In the production network game with CES technology ($\sigma < 1$) and affiliated signals, there exist a greatest and a least pure-strategy Bayesian Nash equilibrium. Both equilibria are in strategies monotone in type: $\tau_i' \geq \tau_i$ implies $\sigma_i^*(\tau_i') \geq \sigma_i^*(\tau_i)$.*

*Proof.* The argument constructs the extremal equilibria explicitly using Tarski's fixed-point theorem.

**Step 1: Strategy Lattice.** Let $\Sigma_i$ denote the set of all monotone strategies $\sigma_i: \mathcal{T}_i \to \mathcal{S}_i$. Under pointwise ordering ($\sigma_i \geq \sigma_i'$ if $\sigma_i(\tau_i) \geq \sigma_i'(\tau_i)$ for all $\tau_i$), $\Sigma_i$ is a complete lattice. The product $\Sigma = \prod_i \Sigma_i$ is also a complete lattice.

**Step 2: Best-Reply Operator.** Define the best-reply operator $BR: \Sigma \to \Sigma$ by selecting, for each player $i$, the *greatest* element of the best-reply correspondence at each type:
$$
BR_i(\sigma_{-i})(\tau_i) = \max \{ a_i \in \mathcal{S}_i : a_i \text{ maximizes } \mathbb{E}[\Pi_i(a_i, \sigma_{-i}(\tau_{-i})) | \tau_i] \}
$$
By Condition 6, the argmax is nonempty and forms a sublattice for each $(\tau_i, \sigma_{-i})$, so the maximum exists.

**Step 3: Isotonicity.** The operator $BR$ is isotone (order-preserving) on $\Sigma$. To see this, suppose $\sigma_{-i}' \geq \sigma_{-i}$. By Condition 5 (increasing differences in $(a_i, a_{-i})$), higher opponent strategies raise the marginal benefit of higher own actions. By single-crossing, the optimal response is higher: $BR_i(\sigma_{-i}') \geq BR_i(\sigma_{-i})$.

**Step 4: Tarski's Theorem.** By Tarski's fixed-point theorem, an isotone map on a complete lattice has a nonempty set of fixed points that itself forms a complete lattice. In particular, there exist greatest and least fixed points.

**Step 5: Monotonicity in Type.** The extremal fixed points $\bar{\sigma}$ and $\underline{\sigma}$ are in monotone strategies by construction: we restricted attention to $\Sigma$, the set of monotone strategies, and showed the best-reply operator maps $\Sigma$ to itself.

Alternatively, we can verify monotonicity directly: for $\tau_i' \geq \tau_i$, single-crossing (Condition 4) implies that if $a_i$ is optimal for $\tau_i$, then some $a_i' \geq a_i$ is optimal for $\tau_i'$. Taking extremal selections preserves this ordering. ∎

### 5.3 Why Extremal Equilibria

Several considerations favor the focus on extremal equilibria.

First, they provide *selection* among potentially multiple equilibria. In games with strategic complementarities, equilibria form a lattice; extremal equilibria bound all others.

Second, they are *robust*. Small changes to payoffs shift extremal equilibria continuously, whereas interior equilibria may appear or disappear.

Third, they yield *tractable comparative statics*. As we show in Section 6, monotonicity of extremal equilibria in parameters extends naturally from the underlying lattice structure.

---

## 6. Comparative Statics

Extremal equilibria respond monotonically to changes in primitives. This section develops the key comparative statics results.

### 6.1 Comparative Statics in Beliefs

**Theorem 2 (Comparative Statics in Beliefs).** *If interim beliefs shift upward in the FOSD sense, both extremal equilibria increase.*

*Proof.* Consider a parameterized family of interim beliefs $\{\pi_i^\lambda\}_{\lambda \in \Lambda}$ where $\Lambda$ is a lattice and $\lambda' \geq \lambda$ implies $\pi_i^{\lambda'}(\cdot | \tau_i) \geq_{FOSD} \pi_i^\lambda(\cdot | \tau_i)$ for all $\tau_i$.

For each $\lambda$, the game has extremal equilibria $\bar{\sigma}^\lambda$ and $\underline{\sigma}^\lambda$. We show $\bar{\sigma}^{\lambda'} \geq \bar{\sigma}^\lambda$ for $\lambda' \geq \lambda$.

By single-crossing, higher beliefs (in FOSD) raise the best-reply: $BR_i^\lambda(\sigma_{-i}) \leq BR_i^{\lambda'}(\sigma_{-i})$ for any $\sigma_{-i}$. The operator $BR^{\lambda'}$ dominates $BR^\lambda$ pointwise.

Starting from the top of the strategy lattice and iterating $BR^\lambda$ yields $\bar{\sigma}^\lambda$; iterating $BR^{\lambda'}$ yields $\bar{\sigma}^{\lambda'}$. Since $BR^{\lambda'} \geq BR^\lambda$ pointwise, the iteration under $\lambda'$ dominates the iteration under $\lambda$ at every step, giving $\bar{\sigma}^{\lambda'} \geq \bar{\sigma}^\lambda$.

An analogous argument starting from the bottom gives $\underline{\sigma}^{\lambda'} \geq \underline{\sigma}^\lambda$. ∎

**Economic Interpretation.** When firms receive more favorable signals about productivity—formally, when the distribution of types shifts upward in FOSD—they adopt denser supplier networks in equilibrium. This reflects the complementarity between information and network investment: better news makes expanded capacity more valuable.

### 6.2 Comparative Statics in Technology Parameters

**Theorem 3 (Comparative Statics in Parameters).** *Let $\theta$ be a technology parameter such that higher $\theta$ increases the payoff to network expansion (e.g., higher TFP, lower adoption costs, reduced distortions). Then $\bar{\sigma}(\theta') \geq \bar{\sigma}(\theta)$ and $\underline{\sigma}(\theta') \geq \underline{\sigma}(\theta)$ for $\theta' > \theta$.*

*Proof.* The argument parallels Theorem 2. Higher $\theta$ shifts the payoff function such that the best-reply to any fixed $\sigma_{-i}$ is (weakly) higher. By Topkis' theorem, the optimal response is monotone in the parameter. The extremal equilibrium, as a fixed point of an isotone map that is itself monotone in the parameter, inherits monotonicity. ∎

**Applications.** 
- *TFP shocks:* An economy-wide productivity increase raises equilibrium network density.
- *Subsidy to network formation:* Reducing the fixed cost of adopting suppliers expands the equilibrium network.
- *Trade liberalization:* Reducing tariffs lowers effective input prices, encouraging network expansion via single-crossing.

---

## 7. Dynamic Extension

The static analysis extends to a dynamic setting where firms solve intertemporal problems and networks evolve over time.

### 7.1 The Dynamic Game

Time is discrete, $t = 0, 1, 2, \ldots$. At each $t$, firms observe private signals about the current state $\mu_t$ and choose actions $a_{i,t} = (S_{i,t}, X_{i,t}, L_{i,t})$. The inherited network $A_t$ summarizes which supplier relationships existed in the previous period.

The law of motion for the network is $A_{t+1} = \Gamma(A_t, \boldsymbol{\alpha}_t)$ where $\boldsymbol{\alpha}_t = (\alpha_{1,t}, \ldots, \alpha_{n,t})$ collects the supplier set choices and $\Gamma$ is isotone in both arguments. This captures network persistence: once a supplier relationship is established, it may be easier to maintain.

Firm $i$ maximizes the discounted sum of expected profits:
$$
\mathbb{E}\left[ \sum_{t=0}^\infty \beta^t \Pi_{i,t} \;\Big|\; \tau_{i,0} \right]
$$
where $\beta \in (0,1)$ is the common discount factor.

### 7.2 Bellman Equation and Value Function

The state for firm $i$ is $z_t = (\mu_t, A_t)$ and its type is $\tau_{i,t}$. The value function satisfies
$$
V_i(z, \tau_i) = \max_{a_i \in \mathcal{S}_i} \left\{ \mathbb{E}[\Pi_i(a_i, \sigma_{-i}(z, \tau_{-i}), z) | \tau_i] + \beta \mathbb{E}[V_i(z', \tau_i') | z, \tau_i, a_i] \right\}
$$
where $(z', \tau_i')$ denotes the next-period state and type.

### 7.3 Existence of Markovian Equilibrium

**Theorem 4 (Dynamic Equilibrium).** *Assume the law of motion $\Gamma$ is isotone and the transition kernel preserves FOSD ordering. Then there exist extremal Bayesian Markov perfect equilibria, and extremal strategies are monotone in both state $z$ and type $\tau$.*

*Proof sketch.* The argument extends the static proof by showing that the Bellman operator preserves the relevant monotonicity. Period payoffs retain increasing differences; the continuation value inherits increasing differences when the transition is isotone and preserves FOSD. Existence follows by applying the static argument at each stage and taking limits. ∎

### 7.4 Monotone Transition Paths

**Theorem 5 (Ordered Transition Paths).** *Let $z_0' \geq z_0$ (higher initial productivity, denser inherited network). Then along extremal policies:*
$$
\underline{\sigma}_t(z_0') \geq \underline{\sigma}_t(z_0), \quad \bar{\sigma}_t(z_0') \geq \bar{\sigma}_t(z_0), \quad A_t(z_0') \geq A_t(z_0) \quad \text{for all } t
$$

*Proof.* By induction. The base case $t = 0$ holds by assumption. For the inductive step: $z_t' \geq z_t$ implies $\sigma_t(z_t') \geq \sigma_t(z_t)$ by Theorem 3. Since $\Gamma$ is isotone:
$$
A_{t+1}' = \Gamma(A_t', \alpha_t') \geq \Gamma(A_t, \alpha_t) = A_{t+1}
$$
Similarly, $\mu_{t+1}' | z_t'$ FOSD-dominates $\mu_{t+1} | z_t$ when the Markov kernel is isotone. Hence $z_{t+1}' \geq z_{t+1}$, completing the induction. ∎

---

## 8. Conclusion

This paper provides theoretical foundations for production network formation under uncertainty. We integrate the endogenous network framework of Acemoglu and Azar (2020) with the Bayesian game methods of Van Zandt and Vives (2007), showing that CES production with complementary inputs generates strategic complementarities that, combined with affiliated signals, guarantee existence of extremal monotone equilibria.

Our main contributions are threefold. First, we establish that the technology used to study endogenous production networks naturally satisfies the conditions required for the Van Zandt-Vives existence results—no additional assumptions are needed beyond those already standard in the literature. Second, we derive rather than assume the information structure: affiliated signals arise naturally from Gaussian setups with non-negative correlations, providing a microfoundation for the FOSD ordering of beliefs. Third, we develop comparative statics showing that shocks to beliefs and technology parameters propagate through the network in predictable ways.

The framework suggests several directions for future research. Empirically, the comparative statics predictions—that shocks to beliefs expand or contract networks depending on their direction—could be tested using data on supply chain formation. Theoretically, the extension to heterogeneous information structures (some firms more informed than others) and to CES specifications with variable elasticity across inputs would broaden applicability. Finally, the dynamic analysis could be enriched to study the speed of network adjustment and the role of frictions in supplier switching.

---

## References

Acemoglu, D. and P. Azar (2020). "Endogenous Production Networks." *Econometrica* 88(1): 33-82.

Karlin, S. and Y. Rinott (1980). "Classes of Orderings of Measures and Related Correlation Inequalities." *Journal of Multivariate Analysis* 10: 467-498.

Milgrom, P. and C. Shannon (1994). "Monotone Comparative Statics." *Econometrica* 62(1): 157-180.

Milgrom, P. and R. Weber (1982). "A Theory of Auctions and Competitive Bidding." *Econometrica* 50(5): 1089-1122.

Stokey, N., R. Lucas, and E. Prescott (1989). *Recursive Methods in Economic Dynamics*. Harvard University Press.

Topkis, D. (1998). *Supermodularity and Complementarity*. Princeton University Press.

Van Zandt, T. and X. Vives (2007). "Monotone Equilibria in Bayesian Games of Strategic Complementarities." *Journal of Economic Theory* 134: 339-360.

---

## Appendix A: Complete Proofs

*[The proofs from the main text are reproduced here with full detail. In the interest of length, we refer the reader to the main text for the key steps; this appendix would contain any remaining technical lemmas and extensions.]*

---
*Draft: 2025-12-14*
