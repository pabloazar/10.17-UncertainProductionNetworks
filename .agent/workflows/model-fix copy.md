---
description: Apply a specific fix from the task.md checklist
---

# Model Fix Workflow

Apply a targeted fix for a specific issue from task.md.

## Usage
```
/model-fix [issue_id]
```
Example: `/model-fix 31` fixes task.md item #31 (Proposition 3 circular logic)

## Steps

1. Read task.md and find the item with the specified `id`:
```
- [ ] Fix Proposition 3 (circular logic) <!-- id: 31 -->
```

2. Search the LaTeX file for the relevant section:
```bash
grep -n "Proposition 3" new_draft_2.tex
```

3. View the surrounding context (±50 lines).

4. Propose a specific fix with rationale.

5. On user approval:
   - Apply the fix
   - Mark the task.md item as `[x]` completed
   - Compile LaTeX to verify

6. Run a focused /math-review on just that section (optional).

7. Commit with message: "Fix task #31: [description]"

## Output
- Fixed `new_draft_2.tex`
- Updated `task.md` with completed item
