# Board of Advisors: "AI Hallucinations and Bank Runs"

**Date:** October 2024
**Subject:** Strategic Review of "AI Hallucinations and Bank Runs"

## 1. The Shleifer Voice (QJE)
*   **Verdict:** "I love the title. 'AI Hallucinations' is a sticky label—it's the new 'Noise Trader'. The intuition that 'stupid AI' causes panics because it can't remember the past is crisp and behavioral."
*   **The Critique:** "Don't get bogged down in the complexity classes ($\text{TC}^0$ vs $\textbf{P}$). The math is fine, but the *story* is about limited attention/memory. Make sure the 'Hallucination' isn't just a mathematical artifact but feels like a 'psychological' bias of the algorithm."
*   **The Demand:** "Give me a concrete example. Show me a 'flash crash' chart and say 'This is what a hallucination looks like.' The paper needs to feel like it explains the *now*."

## 2. The Morris Voice (Econometrica / AER)
*   **Verdict:** "The theoretical contribution is elegant. You're endogenizing the 'public signal' in a global game using computational complexity. That's a genuine advance over standard 'exogenous noise' models."
*   **The Critique:** "Be very precise about the 'Common Prior' assumption. If agents are shallow, do they *know* they are shallow? Or do they think they are rational? The 'Ambiguity Aversion' fix is clever, but you need to justify why they are robust rather than just Bayesian with a wrong model."
*   **The Demand:** "Formalize the 'Limit of Vanishing Noise'. Does the hallucination survive as $\sigma \to 0$? If so, that's a powerful result (instability is robust). If not, clarify the regime where it matters."

## 3. The Goldstein Voice (JF)
*   **Verdict:** "This is a feedback-loop paper. You're showing that AI adoption creates a new source of strategic complementarity. It fits perfectly into the 'Real Effects of Financial Markets' agenda."
*   **The Critique:** "You focus on the *run*, but what about the *price*? Does the price become less informative? If AI hallucinates, does it mess up the learning for everyone else? The 'information externality' is the key finance angle."
*   **The Demand:** "Connect this to 'Liquidity'. Is the hallucination worse when liquidity is low? I want to see a comparative static on market depth ($\kappa$). Does AI make the market more fragile to liquidity shocks?"

## 4. The Guerrieri Voice (AER)
*   **Verdict:** "A solid macro-finance equilibrium. The decomposition of the jump intensity into 'structural' and 'self-fulfilling' parts is very clean."
*   **The Critique:** "What about the *distribution* of types? You have 'Shallow' vs 'Deep'. What happens if the market is 90% Shallow? Is there a tipping point where the Deep agents can no longer stabilize the price? The 'Systemic Risk' angle needs to be quantitative (even if stylized)."
*   **The Demand:** "Add a 'Comparative Statics' proposition. Show me $\partial \lambda^{\text{run}} / \partial \mu_{\text{shallow}} > 0$. Prove that replacing humans with shallow AI makes the market strictly worse."

## 5. The Simsek Voice (JFE / AER)
*   **Verdict:** "It's a belief disagreement paper. Shallow and Deep agents see the same data but form different beliefs. I like the 'Limits to Arbitrage' implication."
*   **The Critique:** "Why don't the Deep agents arbitrage the Shallow agents? If Shallow agents panic when they shouldn't, Deep agents should buy. You need to explain why Deep agents can't stop the run. Is it capital constraints? Or is the run self-fulfilling even for them once it starts?"
*   **The Demand:** "Clarify the 'Wealth Dynamics'. If Shallow agents keep hallucinating, do they lose money? Do they eventually vanish? Or does the 'panic' actually protect them (better safe than sorry)?"
