# Task Checklist: AAVZ Bayesian Supply Chains

## ✅ Completed

- [x] Adopt CES production function from Acemoglu-Azar (eq. 11 in their Appendix) <!-- id: 1 -->
- [x] Derive supermodularity from CES with σ < 1 (Proposition 1) <!-- id: 2 -->
- [x] Prove technology-price single-crossing from A&A Proposition 3 (Proposition 2) <!-- id: 3 -->
- [x] Derive affiliation from Gaussian structure (Proposition 5) <!-- id: 4 -->
- [x] Prove FOSD ordering of beliefs via Milgrom-Weber (Proposition 4) <!-- id: 5 -->
- [x] Verify all 6 Van Zandt-Vives conditions from primitives <!-- id: 6 -->
- [x] Fix notation: use τ_i for types (avoid conflict with time t) <!-- id: 10 -->
- [x] Fix causality: Affiliation → FOSD → VZV monotone equilibria <!-- id: 11 -->
- [x] Add discrete complementarity argument in Prop 1 proof <!-- id: 12 -->
- [x] Clarify ID in (a_i, a_{-i}) mechanism (stage game vs equilibrium) <!-- id: 13 -->
- [x] Fix Gaussian affiliation claim (Karlin-Rinott precision) <!-- id: 14 -->
- [x] Add discussion of σ > 1 case (strategic substitutes, VZV doesn't apply) <!-- id: 15 -->

## 📋 To Do (Minor)

- [ ] Consider using different letter for parameter in Thm 2 (avoid τ confusion) <!-- id: 20 -->
- [ ] Add specific VZV (2007) theorem/assumption citations <!-- id: 21 -->
- [ ] Add empirical justification for σ < 1 assumption <!-- id: 22 -->

## 📋 To Consider

- [ ] Add numerical example illustrating equilibrium computation <!-- id: 30 -->
- [ ] Expand comparison table with Taschereau-Dumouchel <!-- id: 31 -->
- [ ] Add welfare analysis section <!-- id: 32 -->

---

## Key Logic Chain (Current Structure)

```
P1: CES with σ < 1
    → Supermodularity (Prop 1)
    → Technology-price single-crossing (Prop 2, from A&A)
    → Strategic complementarities ID(a_i, a_{-i}) (Prop 3.1)
    → ID(a_i, z) (Prop 3.2)

P2: Affiliation (Gaussian sufficient)
    → FOSD-ordered beliefs over μ (Prop 4.1)
    → FOSD-ordered beliefs over τ_{-i} (Prop 4.2, Prop 6)
    → Single-crossing in (a_i, τ_i) (Prop 3.3)

P3: Bounded action spaces
    → Compact lattice (Lemma 1)
    → Best-reply existence (Prop 9)

P1 + P2 + P3
    → VZV conditions verified
    → Extremal monotone BNE exist (Thm 1)
    → Comparative statics (Thm 2)

P4: Isotone dynamics
    → BMPE exists (Thm 3)
    → Ordered transition paths (Thm 4)
```

---
*Last updated: 2025-12-14 (Round 2 math review)*
