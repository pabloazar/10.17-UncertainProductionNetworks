# Bayesian Dynamic Supply-Chain Model

## 1. Environment and Primitives

We study a discrete-time economy populated by firms $i\in\mathcal I=\{1,\dots,n\}$ that produce differentiated intermediate goods and choose endogenously whom to source from. Time is $t=0,1,\dots$. The aggregate state $\mu_t$ follows a Markov kernel $P(\mu'\mid\mu)$ on a compact interval $\mathcal M\subset\mathbb R$. At the beginning of each period every firm $i$ receives a private signal $s_{i,t}=\mu_t+\varepsilon_{i,t}$, where the noise vector $\varepsilon_t=(\varepsilon_{i,t})_{i\in\mathcal I}$ has affiliated components. The induced posterior over $\mu_t$ given $s_{i,t}$ defines the type $t_{i,t}$. We equip the type space with the Milgrom–Shannon order: $t_i\succeq t_i'$ whenever posteriors satisfy FOSD/MLR, i.e., $\mathbb E[\varphi(\mu)\mid t_i]\ge \mathbb E[\varphi(\mu)\mid t_i']$ for every increasing $\varphi$.

Each firm chooses a supplier intensity $\alpha_{i,t}$ and intermediate-input quantities $x_{i,t}=(x_{ij,t})_{j\ne i}$, as well as a scale variable $k_{i,t}\in[0,\bar k]$. Supplier intensities belong to a finite lattice $\mathcal A_i\subseteq 2^{\mathcal I\setminus\{i\}}$, ordered by set inclusion. Let $A_t$ denote the directed adjacency matrix with $(i,j)$ entry equal to the indicator of $j\in\alpha_{i,t}$.

Technology follows Acemoglu–Azar; the key equation is
$$
y_{i,t}=\theta_{i,t}F\big(k_{i,t},q_{i,t}\big),\qquad q_{i,t}=\sum_{j}A_{ij,t}x_{j,t},\qquad \theta_{i,t}=\exp(\alpha\mu_t+\eta_{i,t}).
$$
Here $F$ is supermodular with increasing differences in $(k,q)$. Revenues are $p_t y_{i,t}$ with $p_t$ increasing in $\mu_t$. Costs $c_i(k)$, $w_{ij}x_{ij}$, and $\phi_{ij}(\alpha_{ij})$ are separable convex. The state for the stage game is $z_t=(\mu_t,A_{t-1})$.

## 2. Strategy Spaces and Payoffs

A pure strategy for firm $i$ at state $z_t$ is a mapping $\sigma_i: \mathcal T_i\times\mathcal Z\to \mathcal A_i\times[0,\bar k]\times\mathbb R_+^{n-1}$. Given others' strategies, the expected payoff for type $t_i$ is $\mathbb E[\Pi_i(\alpha_i,x_i,k_i;\sigma_{-i},z_t)\mid t_i]$. Because signals are affiliated, the conditional distribution of others' types is nondecreasing in $t_i$.

We adopt one of two regularity paths to guarantee existence of best replies:

- (C1) Bounds: $x_{ij}\in[0,\bar x]$ and $k_i\in[0,\bar k]$ for all $i,j$, so $\mathcal S_i=\mathcal A_i\times[0,\bar k]\times[0,\bar x]^{n-1}$ is a compact metrizable complete lattice.
- (C2) Coercivity: $c_i(k)$ is superlinear and input prices satisfy $\inf_{\mu}w_{ij}(\mu)\ge\underline w>0$, so objectives are upper semicontinuous and coercive; argmax lies in a compact sublattice.

## 3. Equilibrium Concepts

**Static Bayesian Nash Equilibrium.** Given state $z_t$, a profile $\sigma(z_t)=(\sigma_i(\cdot,z_t))_{i\in\mathcal I}$ is a Bayesian Nash equilibrium if for every firm $i$ and type $t_i$, $\sigma_i(t_i,z_t)\in\arg\max_{(\alpha_i,x_i,k_i)\in\mathcal S_i}\mathbb E[\Pi_i(\alpha_i,x_i,k_i;\sigma_{-i},z_t)\mid t_i]$, where $\mathcal S_i=\mathcal A_i\times[0,\bar k]\times\mathbb R_+^{n-1}$.

**Bayesian Markov Perfect Equilibrium.** A profile of Markov strategies $(\sigma_i)_{i\in\mathcal I}$ together with a law of motion $A_t=\Gamma(A_{t-1},\sigma(z_t))$ and belief updates via Bayes' rule constitutes a BMPE if, for every $i$ and $t_i$, the value function satisfies
$$
 V_i(z_t,t_i)=\max_{(\alpha_i,x_i,k_i)\in\mathcal S_i}\Big\{\mathbb E[\Pi_i(\alpha_i,x_i,k_i;\sigma_{-i},z_t)\mid t_i]+\beta\,\mathbb E[ V_i(z_{t+1},t_{i,t+1})\mid z_t,t_i]\Big\},
$$
subject to the state transition.

## 4. Lemmas

### Lemma 1 (Strategy Lattice and Existence of Argmax)
Under C1 or C2, $\mathcal S_i$ is a complete lattice (compact under C1), and for any $(t_i,z_t)$ the argmax over $\mathcal S_i$ is nonempty.

**Proof.** $\mathcal A_i\subseteq 2^{\mathcal I\setminus\{i\}}$ is finite and a complete lattice by inclusion. Under C1, $[0,\bar k]\times[0,\bar x]^{n-1}$ is a compact complete lattice; under C2, upper semicontinuity and coercivity ensure the maximizer lies in a compact sublattice. $\square$

### Lemma 2 (Increasing Differences)
For each firm $i$, the conditional expected payoff has increasing differences in $((\alpha_i,x_i,k_i),(\alpha_{-i},x_{-i},k_{-i}),z_t,t_i)$.

**Proof.** $F$ is supermodular with increasing differences in $(k_i,q_i)$; higher $a_{-i}$ raises expected upstream availability and lowers effective marginal costs, preserving increasing differences in $(a_i,a_{-i})$. Since $p(\mu)$ and $\theta_i(\mu)$ increase in $\mu$ and signals are affiliated, a higher $t_i$ FOSD-shifts beliefs over $\mu$ and $a_{-i}$ upward, yielding single-crossing in $(a_i,t_i)$ and increasing differences in $(a_i,z)$. Separable convex costs preserve supermodularity. $\square$

### Lemma 3 (Monotone Best Responses)
For each $i$, the best-response correspondence $BR_i$ is nonempty, upper hemicontinuous, and monotone on $\mathcal S_i$.

**Proof.** Under C1, compactness ensures nonemptiness; under C2, coercivity and upper semicontinuity ensure nonemptiness. Lemma 2 provides increasing differences and single-crossing, so argmax selections are monotone (Topkis). Upper hemicontinuity follows from the Maximum Theorem. $\square$

## 5. Main Theorems

### Theorem 1 (Existence of Bayesian Nash Equilibria)
The static Bayesian stage game at any state $z_t$ admits a pure-strategy BNE. The set of equilibria is a nonempty complete lattice whose extremal elements $\underline{\sigma}(z_t)$ and $\overline{\sigma}(z_t)$ are obtained through isotone iterations of best responses.

**Proof.** Lemma 1 and Lemma 3 deliver existence of best replies with an order-preserving aggregate best-reply map (via C1 or C2). Van Zandt and Vives (2007) prove existence of greatest/least monotone BNE in such supermodular Bayesian games. Tarski then yields a nonempty complete lattice of equilibria with extremal elements obtained by isotone iterations from minimal/maximal strategies. $\square$

### Theorem 2 (Comparative Statics of Extremal Equilibria)
Let $z'\ge z$ denote a larger aggregate state (higher $\mu$ or denser inherited network). Then $\underline{\sigma}(z')\ge\underline{\sigma}(z)$ and $\overline{\sigma}(z')\ge\overline{\sigma}(z)$.

**Proof.** The stage game payoff satisfies increasing differences between own action and the state $z$ (Lemma 2). Therefore the best-response correspondence is nondecreasing in $z$. Iterating the smallest (largest) best response from the minimal (maximal) strategy yields sequences that are monotone in $z$, hence their limits inherit this monotonicity (Topkis). Uniqueness is not assured, but all equilibria lie within the isotone bounds. $\square$

### Theorem 3 (Dynamic Equilibrium and Transitional Dynamics)
A Bayesian Markov perfect equilibrium exists. Let the dynamic operator $\mathcal T$ map value functions into themselves by solving the Bellman problem given others' strategies. Then $\mathcal T$ is monotone, and the associated policy correspondence admits extremal fixed points delivering monotone transition paths. Initial states order transitional dynamics: if $z_0'\ge z_0$, then the extremal equilibrium paths satisfy $\{\underline{\sigma}_t(z_0')\}_t\ge\{\underline{\sigma}_t(z_0)\}_t$ and similarly for the upper path.

**Proof.** The continuation value inherits increasing differences because the period payoff is supermodular and the transition $\Gamma(A,\alpha)$ is isotone. Hence the Bellman operator preserves order on the lattice of bounded functions (Stokey–Lucas). Tarski yields extremal Markov strategies. Higher initial states increase period-by-period best responses and propagate via $\Gamma$. A stationary network $A^*$ solves $A^*=\Gamma(A^*,\sigma(A^*))$. $\square$

## 6. References

- Acemoglu, D., & Azar, P. (2022). *Endogenous Production Networks*. Working paper.
- Milgrom, P., & Shannon, C. (1994). "Monotone Comparative Statics." *Econometrica*.
- Topkis, D. M. (1998). *Supermodularity and Complementarity*. Princeton University Press.
- Van Zandt, T., & Vives, X. (2007). "Monotone Equilibria in Bayesian Games of Strategic Complementarities." *Journal of Economic Theory*.

