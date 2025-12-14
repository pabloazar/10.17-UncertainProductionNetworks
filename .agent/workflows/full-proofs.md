# Full Proofs Workflow

**Goal**: Transform sketch proofs into rigorous derivations using "Cloud" reasoning (Claude High Thinking).

## Steps

// turbo-all

1. **Scan**:
   - Identify "Sketch" or "Omitted" proofs in the document.

2. **Cloud Derivation**:
   - **Action**: detailed-thinking-mode
   - **Prompt**: "Act as a mathematician. Derive the full proof for [Proposition Name] starting from Assumptions P1-P4. Show every algebraic step. Do *not* skip steps."
   
3. **Synthesis**:
   - Take the "Cloud" output.
   - Verify it maps correctly to the paper's specific notation (check $X_{ij}$ vs $x_{ij}$, $\sigma$ vs $\epsilon$).

4. **Implementation**:
   - Replace the sketch in the text/appendix with the full derivation.
   - Use `$$` for block math.

5. **Commit**:
    ```bash
    git add . && git commit -m "Expanded proof using High Thinking derivation"
    ```
