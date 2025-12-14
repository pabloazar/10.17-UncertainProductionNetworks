# Board Report: Shadow Board of Editors

**Date:** November 25, 2025
**Subject:** Strategic Review of "Optimal Self-Custody"

## 1. The Shleifer Voice (QJE)
*   **Verdict:** "The intuition is crisp. 'Payment Kelly' is a sticky label. I like it."
*   **The Critique:** "The 'Genius Act' is a bit of a cheat. It assumes away the regulatory problem to focus on the operational one. That's fine for a model, but for the motivation, you need to convince me that this 'operational risk' is real *today*. Don't just tell me about a hypothetical future; show me that firms are scared of self-custody *now*."
*   **The Demand:** "Give me an anecdote or a fact that proves 'irreversibility' is the binding constraint. Why isn't everyone using USDC for B2B payments already? Is it just the law, or is it the fear of fat-fingering a \$10M transfer?"

## 2. The Schnabl Voice (JFE)
*   **Verdict:** "The banking friction angle is solid. Framing legacy rails as 'insurance' is a nice twist on the deposit franchise literature."
*   **The Critique:** "Your 'Velocity Premium' ($v$) is too abstract. You claim $v$ rises with interest rates. This is a testable hypothesis. If this model is true, we should see stablecoin velocity (or market cap) tracking the Fed Funds Rate. When rates were 0%, nobody cared about T+2. Now that rates are 5%, T+2 is expensive."
*   **The Demand:** "**Identification.** I need to see the data. Show me a plot of Stablecoin Velocity vs. Fed Funds Rate. Or Stablecoin Share of Settlement vs. Interest Rates. If there's no correlation, your mechanism ($v$) is weak."

## 3. The Matvos Voice (RFS)
*   **Verdict:** "Good setup on rail competition. It feels like an IO paper in disguise."
*   **The Critique:** "You treat 'firms' as a monolith. But we see segmentation. Crypto exchanges use stablecoins; Walmart uses Fedwire. Your model explains this (high $v$ vs. low $v$), but you need to document it."
*   **The Demand:** "Show me the cross-section. Who holds stablecoins? Is it just high-turnover trading firms? If you can show that 'high velocity' firms adopt first, you validate the model."

---

## Consensus Action Item

**"We need stylized facts."**

The Board agrees that the theory is elegant but floats in a vacuum. To land a Top 5, you must validate the core comparative static:
**Prediction:** Stablecoin adoption (or velocity) increases when the opportunity cost of legacy lags (interest rates) rises.

**Next Step:**
Obtain data on:
1.  **Stablecoin Velocity/Volume** (USDC/USDT) over time.
2.  **Interest Rates** (Fed Funds / T-Bills) over time.
3.  **Plot the correlation.** If they move together, you have your "Money Chart."
