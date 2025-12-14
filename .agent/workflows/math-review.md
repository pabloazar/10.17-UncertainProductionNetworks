---
description: Send paper to LLM reviewers and parse feedback
---

# Math Review Workflow

Automated review cycle: compile → send to reviewers → parse feedback → apply fixes.

## Usage
```
/math-review
```

## Steps

// turbo-all

1. Read the paper content from `AAVZ_Bayesian_SupplyChains.md`

2. Send to LLM reviewers for mathematical review using web search or direct analysis

3. Summarize feedback with priority ranking:
- **Fatal errors**: Must fix before next round
- **Moderate issues**: Should fix
- **Minor issues**: Can defer

4. For each fatal error:
- Apply fix to `AAVZ_Bayesian_SupplyChains.md`
- Update `task.md` with new items or mark resolved

5. Commit fixes:
```bash
git add AAVZ_Bayesian_SupplyChains.md task.md && git commit -m "Address reviewer feedback: [summary]"
```

6. If fatal errors were fixed, loop back to step 1 for another round.

## Output
- Updated `task.md` with reviewer findings
- Fixed `AAVZ_Bayesian_SupplyChains.md` (committed)

## Notes
- Prioritize Claude feedback over Grok when in conflict
- Maximum 5 rounds before asking user for direction
