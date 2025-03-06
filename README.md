# Regulatory Compliance Risk Tracker

- This tool ensures a portfolio complies with regulatory requirements (e.g., Basel III, Dodd-Frank) by tracking key metrics like capital adequacy, liquidity coverage, and leverage ratios.
- It helps the team monitor and mitigate compliance risks over time.

---

## Files
- `regulatory_compliance_tracker.py`: Main script for generating synthetic portfolio data, calculating regulatory metrics, and visualizing compliance trends with Plotly.
- `output.png`: Plot

---

## Libraries Used
- `pandas`
- `numpy`
- `plotly`

---

## Features
- **Data Generation**: Creates synthetic monthly portfolio data with assets, risk-weighted assets (RWA), capital, liquidity, and debt.
- **Regulatory Metrics**: Calculates:
  - Capital Adequacy Ratio (CAR): Capital / RWA.
  - Liquidity Coverage Ratio (LCR): Liquidity / (Debt * 0.1).
  - Leverage Ratio: Assets / Capital.
- **Compliance Check**: Evaluates compliance against thresholds (CAR ≥ 8%, LCR ≥ 1.0, Leverage ≤ 10.0) and computes an overall compliance rate.
- **Visualization**: Plots CAR and LCR over time with minimum thresholds using Plotly, styled with a dual y-axis layout.
