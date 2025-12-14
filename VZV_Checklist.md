# Van Zandt–Vives Assumptions Checklist (Step-by-Step Mapping)

This checklist verifies, one-by-one, that our Bayesian dynamic supply-chain model (built on Acemoglu–Azar’s endogenous-subset technology) satisfies the hypotheses of Van Zandt & Vives (2007, JET) for existence of greatest/least Bayesian Nash equilibria in monotone strategies and their comparative statics.

We use the interim formulation (no common prior required) and show how supermodularity and affiliation deliver the needed monotone structure. Where compactness is not literal, we impose standard coercivity/bounds to ensure argmax non-emptiness; see Step 3.4.

## Step 1 — Game Objects and Orders

1.1 Players. Finite set of firms/products `I = {1,…,n}`.

1.2 Actions (per i). `a_i = (α_i, x_i, k_i)` where:
- `α_i ∈ A_i ⊆ 2^{I\{i}}` (endogenous subset of suppliers, ordered by inclusion),
- `x_i ∈ R_+^{n-1}` (intermediate inputs),
- `k_i ∈ [0, k̄]` (scale/capital).
Order actions componentwise. `A_i` is a finite lattice; product with intervals forms a (locally) complete lattice.

1.3 Types and interim beliefs. Type `t_i` ≡ private signal `s_i` induces interim belief `π_i(·|t_i)` over `(μ, t_{-i})`. Define the partial order `t_i ⪰ t'_i` iff `π_i(·|t_i)` FOSD-dominates `π_i(·|t'_i)` (e.g., via MLR). This is exactly the interim order used in VZ–Vives.

1.4 State. `z = (μ, A_prev)` collects the aggregate shock and inherited network. We order `z` componentwise (usual order on μ; inclusion on networks).

Conclusion (Step 1): Players, action sets with a lattice order, type spaces with an interim FOSD order are defined as in VZ–Vives.

## Step 2 — Payoff Structure and Monotonicity

2.1 Technology (Acemoglu–Azar exact extensive margin). Output
```
y_i = θ_i(μ) · F(k_i, q_i),  q_i = Σ_{j∈α_i} x_{ij},  θ_i(μ) = exp(φ μ + η_i)
```
Assumptions: `F` supermodular with increasing differences (ID) in `(k_i, q_i)`; `p(μ)` increasing; costs `c_i(k_i)`, link costs `φ_{ij}(1{j∈α_i})`, and input costs `w_{ij}(μ) x_{ij}` are separable and convex.

2.2 Supermodularity preserved under expectation. With affiliated signals, higher `t_i` FOSD-shifts beliefs over `(μ, t_{-i})`. Supermodularity/ID are preserved by taking conditional expectations (Milgrom–Shannon; VZ–Vives §6).

2.3 Increasing differences in own action and others/types/state. Given `F` supermodular and `p(μ), θ_i(μ)` increasing in `μ`, we have ID in `(a_i, a_{-i})` and `(a_i, z)`. Affiliation implies a higher `t_i` raises the interim distribution of others’ actions (via higher types), yielding single-crossing/ID in `(a_i, t_i)`.

Conclusion (Step 2): The interim payoff `E[Π_i | t_i]` satisfies strategic complementarities and increasing differences required by VZ–Vives.

## Step 3 — Topology, Lattices, and Argmax Non-Emptiness

3.1 Lattice property. `A_i` is finite (complete lattice under inclusion). `[0, k̄]` is a complete lattice. For `x_i`, work on a complete lattice `X_i ⊆ R_+^{n-1}` with the product order.

3.2 Compactness/coercivity (one of the following suffices):
- (C1) Exogenous bounds: restrict `x_{ij} ∈ [0, x̄]`. Then `S_i = A_i × [0, x̄]^{n-1} × [0, k̄]` is a compact metrizable complete lattice.
- (C2) Coercivity: assume `c_i(k)` and effective marginal input cost ensure payoff is **upper semicontinuous** and **coercive** so that the argmax exists and lies in a compact sublattice `S_i(·)` for any `(t_i, z)`. (E.g., `c_i(k)` superlinear and input prices bounded away from zero.)

3.3 Measurability and continuity. Payoffs are continuous in actions and measurable in types/states, ensuring upper hemicontinuity of best replies (Maximum Theorem).

3.4 Best-reply existence. Under (C1) or (C2), for each `(t_i, z, a_{-i})`, `argmax_{a_i∈S_i}` is nonempty and forms a sublattice (Topkis).

Conclusion (Step 3): Action spaces meet VZ–Vives’ “compact locally complete metrizable lattice” (via C1) or deliver nonempty argmax and monotone selections (via C2).

## Step 4 — Monotone Best Replies and GBR Mapping

4.1 Monotone BR. From Step 2 (ID) and Step 3 (lattice/argmax), best responses are isotone in `(a_{-i}, t_i, z)` (Topkis; Milgrom–Shannon). Upper hemicontinuity follows by Step 3.3.

4.2 Generalized Best Reply (GBR). Define the product correspondence `BR(a, t, z)`. It is nonempty, order-preserving, and closed-valued on the product lattice of strategies.

Conclusion (Step 4): The conditions for VZ–Vives’ constructive fixed-point approach apply.

## Step 5 — Existence of Extremal Monotone BNE (Static)

5.1 Apply VZ–Vives (JET 2007, Thm.): In games with strategic complementarities, increasing differences in own action and type profile, and interim beliefs increasing in type (FOSD), there exist a **greatest** and a **least** pure-strategy Bayesian Nash equilibrium in **strategies monotone in type**.

5.2 Our mapping: Steps 1–4 satisfy the theorem’s hypotheses (with C1 or C2). Therefore, at each `z`, the static stage game admits extremal monotone BNE `σ̲(z), σ̄(z)`.

Conclusion (Step 5): Existence of extremal monotone BNE is established.

## Step 6 — Comparative Statics (Static)

6.1 Interim beliefs. VZ–Vives: an FOSD upward shift in interim beliefs increases both extremal equilibria.

6.2 Parameters. With any scalar parameter `τ` entering with increasing differences (e.g., lower link costs, higher demand shifter), Topkis monotone C.S. implies `σ̲(z;τ)` and `σ̄(z;τ)` increase in `τ`.

Conclusion (Step 6): Monotonicity of extremal equilibria in beliefs and parameters holds.

## Step 7 — Dynamic Extension and Transitional Dynamics

7.1 Law of motion. Let `A' = Γ(A, α)` with `Γ` isotone in both arguments (e.g., persistent links with higher retention after activation). This preserves order.

7.2 Bellman operator. Period payoffs retain ID; the continuation value inherits ID when the transition/kernel is isotone. The resulting policy correspondence is order-preserving on the strategy lattice.

7.3 Extremal BMPE and stationarity. By Tarski, there exist extremal Markov strategies; a stationary network `A*` solves `A* = Γ(A*, α*)`.

7.4 Ordered transition paths. Starting from `z0' ≥ z0`, extremal paths satisfy `σ̲_t(z0') ≥ σ̲_t(z0)` and `A_t(z0') ≥ A_t(z0)` for all `t`.

Conclusion (Step 7): Dynamic existence and monotone transitional dynamics obtain.

## Step 8 — Where We Differ from “Endogenous Network” in Taschereau‑Dumouchel et al.

- Choice object: we optimize over **subsets** of inputs (A&A extensive margin), not only continuous exposures on a fixed support.
- Information: we allow **private affiliated signals**; equilibrium is a **monotone BNE** in type (incomplete information), not a complete‑information fixed point.
- Results: we prove **extremal** equilibria and **ordered** transition paths, yielding selection‑robust, policy‑monotone predictions under uncertainty.

## Step 9 — Minimal Assumption Set (for referees)

- (A1) `A_i` finite nonempty subset of `2^{I\{i}}` (inclusion order); `[0,k̄]` compact; either `x_{ij}∈[0,x̄]` (C1) or coercivity (C2).
- (A2) `F` supermodular with ID in `(k,q)`; `p(μ), θ_i(μ)` increasing in `μ`; costs separable convex.
- (A3) Signals affiliated; define `t_i` by induced interim beliefs; type order by FOSD/MLR.
- (A4) Payoffs continuous in actions; measurable in `(t,z)`; expectation preserves supermodularity.
- (A5) `Γ` isotone in `(A, α)` for dynamics; discount `β∈(0,1)`; bounded payoffs.

Under (A1)–(A4): VZ–Vives extremal monotone BNE exist and are monotone in beliefs/parameters. Under (A5): dynamic extremal policies and ordered transitional dynamics.

