---
description: Brainstormed workflows for agentic paper development
---

# Agentic Workflows for Academic Paper Development

## Current Workflow (Manual)
```
User Request → Agent Edits → User Review → Repeat
```

## Proposed Workflows

---

### 1. `/math-review` - Automated Review Cycle
**Trigger:** User runs `/math-review`

```
1. Agent compiles LaTeX → PDF
2. Sends to Claude/Grok/Gemini with math_check prompts
3. Parses feedback into structured JSON:
   - critical_errors: []
   - notation_issues: []  
   - proof_gaps: []
   - suggestions: []
4. Auto-generates implementation plan from feedback
5. Asks user: "Apply these N fixes? [Y/n]"
6. If Y: applies fixes, creates latexdiff, goto step 1
7. Loop until no critical errors
```

// turbo-all

---

### 2. `/redline` - Auto-Diff Generation
**Trigger:** User runs `/redline [commit_ref]`

```
1. git show {commit_ref}:file.tex > /tmp/old.tex
2. latexdiff /tmp/old.tex file.tex > file_diff.tex
3. pdflatex file_diff.tex
4. Opens PDF in browser
```

// turbo-all

---

### 3. `/data-enrich` - CoinGecko/Flipside Data Pipeline
**Trigger:** User runs `/data-enrich [event_date]`

```
1. Parse market_events.json for event windows
2. For each event:
   - Query Flipside: get DEX volumes, bot activity
   - Query CoinGecko MCP: get market volatility, liquidity
3. Merge into 2024_panel.csv
4. Run R regressions from codex_implementation_plan.md
5. Output: regression tables, model diagnostics
```

---

### 4. `/model-fix [issue_id]` - Targeted Proof Repair
**Trigger:** User runs `/model-fix 31` (from task.md)

```
1. Agent reads task.md item #31
2. Searches codebase for relevant LaTeX sections
3. Proposes specific fix with rationale
4. On approval: applies fix, compiles, runs /math-review on that section only
```

---

### 5. `/iterate` - Full Revision Loop
**Trigger:** User runs `/iterate`

```
1. Run /math-review
2. Parse feedback → update task.md checklist
3. For each critical item:
   a. Apply fix
   b. Compile LaTeX
   c. Create mini-diff
4. Run /redline HEAD~1
5. Run /math-review on revised draft
6. If no new critical issues: done
7. Else: notify user with remaining issues
```

// turbo-all

---

## Implementation Priority

| Workflow | Complexity | Value | Priority |
|----------|------------|-------|----------|
| `/redline` | Low | High | 🟢 Now |
| `/math-review` | Medium | Very High | 🟢 Now |
| `/model-fix` | Medium | High | 🟡 Next |
| `/data-enrich` | High | Medium | 🟡 Next |
| `/iterate` | High | Very High | 🔴 Later |

---

## Questions for User

1. **Which workflows do you want me to implement first?**
2. **Should `/math-review` auto-apply non-critical fixes without asking?**
3. **Do you want email/Slack notifications when long-running reviews complete?**
4. **For `/data-enrich`, preferred data sources: Flipside SQL vs CoinGecko API vs both?**
