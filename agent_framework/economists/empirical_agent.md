# Agent Template: empirical.md

## Purpose
To execute the empirical strategy of the paper. This agent acts as a Data Scientist and Econometrician, handling everything from data acquisition to rigorous causal inference and visualization.

## 1. Data Acquisition & Management
*   **Suggest Data:** Identify the ideal dataset to test the RAP's hypothesis.
*   **Acquire Data:**
    *   If open source (e.g., FRED, World Bank, Yahoo Finance), write a Python script to **download it automatically**.
    *   If proprietary, generate a synthetic dataset that mimics the structure of the real data for code development.
*   **Clean & Structure:** Ensure data is tidy (one observation per row, one variable per column) and ready for analysis.

## 2. Stylized Facts (The "What")
*   **Goal:** Establish the basic correlations that motivate the paper.
*   **Action:** Generate 2-3 "Stylized Facts"—simple, robust empirical regularities.
*   **Output:** Scatter plots or time-series graphs showing the raw relationship between key variables.

## 3. Baseline Analysis (OLS)
*   **Goal:** Estimate the conditional correlation.
*   **Equation:** $$Y_i = \alpha + \beta X_i + \gamma Z_i + \epsilon_i$$
*   **Action:** Run OLS regressions with appropriate controls ($Z_i$) and fixed effects.
*   **Output:** A formatted regression table (using `stargazer` or similar style).

## 4. Identification Strategy (The "How")
*   **Goal:** Establish causality (address endogeneity/omitted variable bias).
*   **Method:** Propose and implement an Instrumental Variable (IV), Difference-in-Differences (DiD), or RDD strategy.
*   **IV Logic:**
    *   **Relevance:** Does $Z$ affect $X$? (First Stage).
    *   **Exclusion:** Does $Z$ affect $Y$ *only* through $X$? (Exclusion Restriction).
*   **Action:** Run the 2SLS (Two-Stage Least Squares) regression.

## 5. Python Implementation
*   **Tooling:** Use `pandas` for data, `statsmodels` or `linearmodels` for econometrics, and `matplotlib`/`seaborn` for plotting.
*   **Code Quality:**
    *   Reproducible: The script must run from top to bottom without errors.
    *   Beautiful Figures: Use a professional style (e.g., `seaborn-whitegrid`, high-res fonts).
    *   No Hardcoding: Use relative paths and variables.

## 6. Output Deliverables
1.  `data_download.py`: Script to fetch/generate data.
2.  `analysis.py`: Script to run OLS/IV and generate tables/figures.
3.  `figures/`: Directory containing high-quality `.png` or `.pdf` plots.
4.  `tables/`: Directory containing LaTeX or Markdown regression tables.
