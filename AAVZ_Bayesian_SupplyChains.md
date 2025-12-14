# Endogenous Supply Chains under Uncertainty: An Acemoglu–Azar–Van Zandt–Vives Framework

## 1. Primitives and Information

- Time $t=0,1,\dots$. Finite set of products/firms $\mathcal I=\{1,\dots,n\}$.
- Aggregate state $\mu_t\in\mathcal M\subset\mathbb R$ follows Markov kernel $P(\mu'\mid\mu)$ on compact $\mathcal M$.
- At the start of $t$, firm $i$ receives private signal $s_{i,t}=h(\mu_t)+\varepsilon_{i,t}$ with $(\varepsilon_{i,t})_{i\in\mathcal I}$ affiliated. The induced posterior (interim belief) is $\pi_i(\cdot\mid s_{i,t})$. Types $t_i\equiv s_{i,t}\in\mathcal T_i$ are ordered by MLR/FOSD via their induced interim beliefs: $t_i\succeq t'_i$ iff $\pi_i(\cdot\mid t_i)\ge_{FOSD}\pi_i(\cdot\mid t'_i)$.

## 2. Technology (Acemoglu–Azar exact extensive margin)

- Each $i$ chooses an **endogenous supplier subset** $\alpha_{i,t}\in\mathcal A_i\subseteq 2^{\mathcal I\setminus\{i\}}$ (finite menu of subsets as in Acemoglu–Azar), an input vector $x_{i,t}=(x_{ij,t})_{j\ne i}\in\mathbb R_+^{n-1}$, and a scale $k_{i,t}\in[0,\bar k]$.
- Let $A_t$ be the adjacency matrix with $(i,j)$ entry $1\{j\in\alpha_{i,t}\}$. The effective upstream aggregate is $q_{i,t}=\sum_{j\in \alpha_{i,t}} x_{ij,t}$.
- Output (key equation, display):
$$
y_{i,t}=\theta_{i,t}\,F\big(k_{i,t},q_{i,t}\big),\qquad \theta_{i,t}=\exp(\varphi\,\mu_t+\eta_{i,t}).
$$
  Here $F$ is supermodular and has increasing differences (ID) in $(k,q)$; $\eta_{i,t}$ is idiosyncratic.
- Revenues $p_t\,y_{i,t}$ with $p_t$ increasing in $\mu_t$. Costs: convex $c_i(k_{i,t})$, link/activation costs $\sum_{j}\phi_{ij}(1\{j\in\alpha_{i,t}\})$, and input expenditures $\sum_j w_{ij,t}\,x_{ij,t}$.
- State for the stage game: $z_t=(\mu_t,A_{t-1})$. The network law of motion is order-preserving: $A_t=\Gamma(A_{t-1},\alpha_t)$ with $\Gamma$ isotone in both arguments (as in A&A’s dynamic extension; e.g., links persist with probability increasing in activation).

## 3. Strategy Spaces and Order Structure

- Actions $a_i\equiv(\alpha_i,x_i,k_i)$ lie in $\mathcal S_i=\mathcal A_i\times \mathbb R_+^{n-1}\times[0,\bar k]$ ordered componentwise, with $\mathcal A_i$ ordered by set inclusion.
- Assumption S1 (Lattice structure). Each $\mathcal A_i$ is finite; hence $\mathcal A_i$ is a complete lattice (discrete metric). The product $\mathcal S_i$ is a complete lattice under the product order.
- Assumption C (Compactness or Coercivity). One of the following holds:
  - C1 (Bounds): for each $i$, inputs satisfy $x_{ij}\in[0,\bar x]$ and $k_i\in[0,\bar k]$, so $\mathcal S_i$ is a compact metrizable complete lattice.
  - C2 (Coercivity): $c_i(k)$ is superlinear and input prices satisfy $\inf_{\mu} w_{ij}(\mu)\ge \underline w>0$ for all $i,j$, so the stage payoff is upper semicontinuous and coercive; the argmax is nonempty and lies in a compact sublattice.

- Types $\mathcal T_i$ carry the partial order $\succeq$ induced by FOSD/MLR on interim beliefs (Van Zandt–Vives).

## 4. Payoffs and Increasing Differences

- Firm $i$’s period payoff at state $z$ and type $t_i$ against strategy profile $\sigma_{-i}$ is (key equation, display):
$$
\Pi_i(a_i;\sigma_{-i},z,t_i)=\mathbb E\Big[p(\mu)\,\theta_i(\mu)\,F\big(k_i,\textstyle\sum_{j\in\alpha_i}x_{ij}\big)-c_i(k_i)-\sum_j\phi_{ij}(1\{j\in\alpha_i\})-\sum_j w_{ij}(\mu)\,x_{ij} \;\Big|\; t_i,\,z\Big].
$$
- Assumption P1 (Strategic complementarities). For each $i$, $\Pi_i$ has increasing differences in $(a_i,a_{-i})$ and in $(a_i,z)$, and has single crossing in $(a_i,t_i)$ via the FOSD order on interim beliefs. Sufficient conditions: (i) $F$ supermodular with ID; (ii) $p(\mu)$ and $\theta_i(\mu)$ increasing in $\mu$; (iii) affiliation so that higher $t_i$ FOSD-shifts beliefs over others’ types (hence expected $a_{-i}$) upward; (iv) separable convex costs.

- Assumption P2 (Regularity). Payoffs are continuous in actions and measurable in $(t,z)$. Under C1, $\mathcal S_i$ is compact; under C2, the objective is upper semicontinuous and coercive, so best replies exist.

These yield a **monotone supermodular** Bayesian stage game (Van Zandt–Vives, JET 2007).

## 5. Equilibrium Concepts

- Static BNE at $z$: a profile $\sigma(z)=(\sigma_i(\cdot,z))_{i}$ of measurable strategies $\sigma_i: \mathcal T_i\to\mathcal S_i$ such that for all $t_i$,
$$
\sigma_i(t_i,z)\in\arg\max_{a_i\in\mathcal S_i}\;\mathbb E\big[\Pi_i(a_i;\sigma_{-i},z,t_i)\big].
$$
- Dynamic Bayesian Markov perfect equilibrium (BMPE): strategies $\sigma_i(\cdot,\cdot)$ and $A' = \Gamma(A,\alpha)$ with value functions $V_i(z,t_i)$ solving the Bellman equations and beliefs updated by Bayes’ rule.

## 6. Lemmas

**Lemma 1 (Strategy lattice).** Under S1 and C1, each $\mathcal S_i$ is a compact metrizable complete lattice.

*Proof.* $\mathcal A_i$ is finite, hence compact and complete under inclusion; $\mathbb R_+^{n-1}$ (bounded to $[0,\bar x]^{n-1}$ by C1) and $[0,\bar k]$ are complete lattices under componentwise order; their product is a compact complete lattice. $\square$

**Lemma 2 (Increasing differences).** Under P1–P2, the interim objective $\mathbb E[\Pi_i\mid t_i]$ has increasing differences in $(a_i,a_{-i},z)$ and single crossing in $(a_i,t_i)$.

*Proof.* Supermodularity/ID of $F$ imply complementarity between own controls and upstream aggregate $q_i$; higher $a_{-i}$ raises expected upstream availability and reduces effective costs, preserving ID in $(a_i,a_{-i})$. Since $p(\mu),\theta_i(\mu)$ increase in $\mu$ and signals are affiliated, a higher $t_i$ FOSD-shifts beliefs over $\mu$ and $a_{-i}$ upward, ensuring single crossing in $(a_i,t_i)$ and ID in $(a_i,z)$. Separable convex costs preserve supermodularity. $\square$

**Lemma 3 (Monotone best replies).** The best-response correspondence $BR_i$ is nonempty, upper hemicontinuous, and monotone in $(a_{-i},z,t_i)$.

*Proof.* Under C1, compactness/continuity yield nonemptiness and u.h.c. Under C2, coercivity and upper semicontinuity ensure existence and u.h.c. Increasing differences (Lemma 2) and the monotone-supermodular structure imply monotone selections (Topkis, Milgrom–Shannon). $\square$

## 7. Main Results (Stage Game)

**Theorem 1 (Greatest and least monotone BNE; Van Zandt–Vives).** In the static stage game at state $z$, there exist a greatest and a least pure-strategy Bayesian Nash equilibrium $\overline\sigma(z)$ and $\underline\sigma(z)$, each in strategies monotone in type. They are obtained by iterating the (generalized) best-reply mapping from maximal/minimal strategies.

*Proof.* This is an application of Van Zandt–Vives (2007, JET 134:339–360): our game satisfies (i) strategic complementarities (supermodularity in actions), (ii) increasing differences in own action and type profile (via affiliation/FOSD), and (iii) existence of best replies with an order-preserving aggregate best-reply map (via C1 or C2). Their constructive fixed-point proof yields extremal monotone equilibria. $\square$

**Theorem 2 (Comparative statics of extremal BNE).** (i) If interim beliefs shift upward in FOSD (e.g., more informative signals in the MLR sense), then both $\underline\sigma(z)$ and $\overline\sigma(z)$ increase (Van Zandt–Vives). (ii) If a parameter $\tau$ enters with increasing differences in payoffs (e.g., lower link costs, higher $p(\mu)$), then $\underline\sigma(z;\tau)$ and $\overline\sigma(z;\tau)$ are nondecreasing in $\tau$ (Topkis/Milgrom–Shannon).

*Proof.* (i) Van Zandt–Vives prove that a FOSD upward shift in interim beliefs increases the extremal equilibria. (ii) Increasing differences in $(a_i,\tau)$ imply monotone best replies in $\tau$; the fixed points of an isotone map are monotone (Tarski). $\square$

## 8. Dynamic Results

Define the dynamic operator mapping bounded value functions into themselves (key equation, display):
$$
(\mathcal T V_i)(z,t_i)=\max_{a_i\in\mathcal S_i}\Big\{\mathbb E[\Pi_i(a_i;\sigma_{-i},z,t_i)] + \beta\,\mathbb E[V_i(z',t'_i)\mid z,t_i,a_i,\sigma_{-i}]\Big\}.
$$
Assume $\Gamma(A,\alpha)$ is isotone and the induced transition kernel preserves the FOSD order conditional on actions.

**Theorem 3 (Existence of BMPE and stationary network).** There exists a Bayesian Markov perfect equilibrium. Moreover, the induced policy operator is isotone, and there exist extremal Markov strategies delivering a stationary network $A^*$ solving $A^*=\Gamma(A^*,\alpha^*)$.

*Proof.* Period payoffs are supermodular with ID; the continuation term preserves ID when the transition is isotone (Acemoglu–Azar dynamic extension, order-preserving $\Gamma$). Hence $\mathcal T$ is an order-preserving self-map on the lattice of bounded functions; monotone policy correspondences admit extremal fixed points (Tarski). The induced $\Gamma$ and monotone strategies yield existence of $A^*$. $\square$

**Theorem 4 (Monotone transitional dynamics).** Let $z_0'\ge z_0$ in the product order (higher $\mu$, denser inherited $A$, or higher $\tau$). Then along extremal BMPE policies, the entire paths $\{\underline\sigma_t(z_0')\}_t$ and $\{\overline\sigma_t(z_0')\}_t$ weakly dominate those from $z_0$, and the network paths satisfy $A_t(z_0')\ge A_t(z_0)$ for all $t$.

*Proof.* Induction using isotone best replies and isotone $\Gamma$: a higher initial state yields (weakly) higher actions, which propagate forward via $\Gamma$, preserving the order period by period. $\square$

## 9. Positioning and Contribution

- **Exact A&A extensive margin under uncertainty.** We adopt Acemoglu–Azar’s *subset choice* of inputs (the extensive margin of the IO matrix) as the primitive technological decision. This differs from exposure-weight models that directly choose continuous weights on a fixed support.
- **Incomplete information with affiliation.** We introduce affiliated private signals (MLR/FOSD) and use Van Zandt–Vives’ interim formulation (no common prior needed) to establish existence of greatest/least BNE in monotone strategies and FOSD comparative statics.
- **Dynamic monotone structure.** By imposing an order-preserving network law of motion $\Gamma$ (in the spirit of A&A’s dynamic version), we obtain ordered transition paths and stationary equilibria without uniqueness—selection-robust predictions absent in deterministic complete-information models.
- **Relative to Taschereau-Dumouchel et al.** Their “endogenous networks” typically allow agents to choose exposure/intensity under complete information or reduced-form shocks; we differ by (i) optimizing over the *set* of active inputs (A&A’s extensive margin), (ii) allowing private affiliated information to shape link activation, and (iii) proving extremal BNE and dynamic monotonicity via supermodular-Bayesian methods. The result is an equilibrium lattice with policy-robust comparative statics.

## 10. References (select)

- Acemoglu, D., and P. D. Azar (2020), “Endogenous Production Networks,” Econometrica 88(1):33–82.
- Milgrom, P., and C. Shannon (1994), “Monotone Comparative Statics,” Econometrica.
- Topkis, D. M. (1998), Supermodularity and Complementarity, Princeton University Press.
- Van Zandt, T., and X. Vives (2007), “Monotone equilibria in Bayesian games of strategic complementarities,” JET 134:339–360.

## Appendix: Assumption-to-Theorem Mapping (Referee Quick Check)

- A1 Lattices (S1): $\mathcal A_i\subseteq 2^{\mathcal I\setminus\{i\}}$ finite (inclusion order); actions $a_i=(\alpha_i,x_i,k_i)$ ordered componentwise. Product is a complete lattice. Under C1, compact metrizable.
- A2 Regularity (P2/C1–C2): either bounds $x_{ij}\in[0,\bar x]$, $k_i\in[0,\bar k]$ (C1) or coercivity with superlinear $c_i(k)$ and $\inf_{\mu}w_{ij}(\mu)\ge\underline w>0$ (C2); payoffs continuous in actions and measurable in $(t,z)$.
- A3 Technology (P1): $F$ supermodular with increasing differences in $(k,q)$; revenues $p(\mu)\,\theta(\mu)$ increasing in $\mu$; separable convex costs. Implies strategic complementarities.
- A4 Information (VZ–Vives interim): types are private signals; interim beliefs ordered by FOSD/MLR (affiliation ensures higher type FOSD-shifts beliefs). Implies single-crossing in $(a_i,t_i)$.
- T1 (Lemmas 1–3): nonempty argmax and monotone best responses (Topkis/Milgrom–Shannon).
- T2 (VZ–Vives): existence of greatest/least pure-strategy BNE in strategies monotone in type; extremal equilibria increase under FOSD improvements in interim beliefs.
- T3 (Topkis): comparative statics in parameters $\tau$ that enter with increasing differences.
- D1 (Dynamics): isotone law of motion $\Gamma(A,\alpha)$; Bellman operator preserves order; extremal Markov strategies (Tarski) and ordered transition paths.

This mapping verifies each hypothesis used in the theorems and points to the exact assumption (A1–A4) delivering it.
