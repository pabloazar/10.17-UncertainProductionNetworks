# RAP: Endogenous Production Networks under Uncertainty

## R: Research Question

**How do firms optimally choose their supplier networks when they receive private, correlated signals about aggregate productivity—and what characterizes the resulting equilibrium?**

More precisely: In a production economy where (i) firms choose which suppliers to adopt, (ii) inputs are technological complements, and (iii) information about the state is private but affiliated, does a well-defined equilibrium exist? If so, what are its properties—and how does it respond to changes in uncertainty and technology?

---

## A: Answer (The Mechanism)

**Equilibria exist, are extremal, and exhibit monotone comparative statics.**

When intermediate inputs are complements (elasticity of substitution less than one) and signals are affiliated:

1. **Existence:** There exist a *greatest* and a *least* Bayesian Nash equilibrium in supplier network choices. Both are in strategies monotone in type: firms with higher signals about productivity adopt denser supplier networks.

2. **Mechanism:** Two forces combine:
   - *Technological complementarity*: Under CES production with low substitutability, adding suppliers raises the marginal product of existing inputs. This creates strategic complementarities—firms want to expand their networks when others do.
   - *Informational complementarity*: Affiliated signals mean that observing a high signal about one's own productivity is "good news" about others' signals. This creates correlated beliefs that reinforce the strategic complementarity.

3. **Comparative statics:** Shocks that improve the distribution of beliefs (FOSD shifts) increase equilibrium network density. Policy interventions that reduce the cost of adopting suppliers expand networks, and this expansion propagates through the economy.

---

## P: Positioning (The Contribution)

### Context: The Real World

Modern production is a complex web of varying reliability. As emphasized by **Acemoglu and Azar (2020)**, supply chains have evolved from simple raw materials (wood, steel) to complex, multi-component assemblies (semiconductors, specialized software) where a single missing input can halt production. **Taschereau-Dumouchel et al. (2024)** highlight that in this volatile environment, firms actively manage risk by choosing "safer" suppliers.

### The Problem: Opaque Supply Chains

However, these decisions are made in the fog of war. A firm rarely knows the precise productivity or reliability of potential partners. Instead, managers operate on **signals**: industry news, earnings calls, or minor delivery delays that hint at broader upstream troubles. Crucially, these signals are **correlated**—a chip shortage affects all auto manufacturers, but each observes different local symptoms.

### The Gap

Existing theory models network formation under two extremes:
1.  **Complete Information (Acemoglu & Azar, 2020):** Firms perfectly observe everyone's productivity.
2.  **Known Risk Profiles (Kopytov et al., 2024):** Firms know the variance of suppliers and optimize the trade-off.

Neither accounts for the **inference** problem: how firms use private signals to form beliefs about the economy, and how these beliefs interact with network formation.

### The Contribution

We provide a theory of **production network formation under dispersed information**. By integrating the technological structure of Acemoglu-Azar with the information economics of **Van Zandt and Vives (2007)**, we show:
1.  **Information is a Complement:** When inputs are complements ($\sigma < 1$), "good news" is super-modular. Optimistic beliefs trigger network expansion, which (due to affiliation) coincides with others expanding, reinforcing the incentive.
2.  **Opacity Amplifies Shocks:** Because firms react to *signals* of aggregate states, correlated errors in sentiment can generate excessive network contractions (or expansions) disconnected from fundamental productivity.
3.  **Tractable Equilibrium:** Despite the complexity of inferring millions of states, we derive existence of **extremal monotone equilibria**, allowing for clean comparative statics.

---

## Key Concepts (The "Rhyme")

These terms will be used consistently throughout the paper:

| Concept | Definition | Never Say |
|---------|------------|-----------|
| **Supplier set** | The endogenous choice of which inputs to adopt | "Network links", "IO matrix entries" |
| **Monotone strategy** | A strategy where higher types choose larger supplier sets | "Increasing policy function" |
| **Affiliated signals** | Signals whose joint distribution satisfies log-supermodularity | "Correlated information" |
| **Strategic complementarities** | Property where higher actions by others increase the marginal return to own action | "Positive spillovers", "Complementary behavior" |
| **Extremal equilibrium** | The greatest or least equilibrium in the lattice of monotone strategies | "Maximal BNE" |

---

## Core Testable Hypothesis

**If the mechanism is correct, then:**

1. *Cross-sectional prediction*: Firms with more precise signals about aggregate productivity should have denser supplier networks.

2. *Time-series prediction*: Negative shocks to average beliefs (e.g., unexpected recessions) should trigger network contraction that is amplified by complementarities.

3. *Policy prediction*: Reducing fixed costs of supplier adoption should expand networks more in sectors with lower elasticity of substitution (higher complementarities).

---

## The Three Logical Checks

### 1. Does P make space for R?

**Yes.** The positioning establishes that:
- Acemoglu-Azar study network formation under complete information
- Van Zandt-Vives study abstract games with complementarities
- *Neither* addresses production networks under incomplete information

This gap creates space for the question: what happens when we combine these features?

### 2. Does A answer R?

**Yes.** The research question asks: does equilibrium exist, and what are its properties? The answer states: equilibria exist (extremal, monotone), and they exhibit specific comparative statics (FOSD shifts increase networks).

### 3. Does A answer the "Idle Question"?

**Yes.** When confronted with the gap (no theory of networks under uncertainty), the natural question is: "So what *does* equilibrium look like in this setting?" The answer directly addresses this: it looks like extremal monotone equilibria with predictable responses to information shocks.

---
*Last updated: 2025-12-14*
