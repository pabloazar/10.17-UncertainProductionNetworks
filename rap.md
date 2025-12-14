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

### Context: What We Know

The study of production networks has advanced on two fronts.

First, a growing literature examines *endogenous* production networks—where firms choose their suppliers rather than taking the input-output matrix as given. Acemoglu and Azar (2020) show that when firms face fixed costs of adopting suppliers, the equilibrium network depends on technology parameters and can exhibit discontinuous responses to shocks. Their analysis, however, assumes *complete information*: all firms observe the state perfectly.

Second, the theory of games with strategic complementarities provides powerful tools for analyzing equilibria. Van Zandt and Vives (2007) establish that Bayesian games with complementarities admit extremal equilibria in monotone strategies, even without a common prior. But their analysis is abstract—it provides conditions, not economic content.

### The Gap: What We Don't Know

*No existing work combines these approaches.* We lack a theory of production network formation when:
- Firms have private, heterogeneous information about productivity
- This information is naturally correlated (affiliated) across firms
- The technology exhibits complementarities

This gap matters because real-world supply chain decisions are made under uncertainty. Firms choose suppliers based on imperfect signals about demand conditions, input prices, and their own productivity. Understanding how information shapes network formation is essential for policy—particularly in the context of supply chain resilience.

### The Contribution: What This Paper Adds

We fill this gap by:

1. **Integrating production theory with information economics.** We show that the CES production technology with complementary inputs (σ < 1) naturally generates the strategic complementarities required for Van Zandt-Vives methods.

2. **Deriving, not assuming, the key conditions.** Affiliation of signals and FOSD ordering of beliefs are derived from a Gaussian information structure—not imposed as black-box assumptions.

3. **Establishing substantive economic results.** We prove that extremal equilibria exist, exhibit monotonicity in information, and respond predictably to policy. We extend these results to a dynamic setting with persistent network formation.

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
