import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Synthetic portfolio data
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2024-01-01", freq="ME")
df = pd.DataFrame({
    "Date": dates,
    "Assets": np.random.uniform(500000, 1000000, len(dates)),
    "RWA": np.random.uniform(300000, 800000, len(dates)),
    "Capital": np.random.uniform(50000, 150000, len(dates)),
    "Liquidity": np.random.uniform(20000, 100000, len(dates)),
    "Debt": np.random.uniform(400000, 900000, len(dates))
})

# Step 1: Calculate regulatory metrics
def compute_metrics(df):
    df["CAR"] = df["Capital"] / df["RWA"]
    df["LCR"] = df["Liquidity"] / (df["Debt"] * 0.1)
    df["Lev"] = df["Assets"] / df["Capital"]
    return df

# Step 2: Assess compliance
def evaluate_compliance(df):
    df["CAR_OK"] = df["CAR"] >= 0.08
    df["LCR_OK"] = df["LCR"] >= 1.0
    df["Lev_OK"] = df["Lev"] <= 10.0
    df["Compliant"] = df["CAR_OK"] & df["LCR_OK"] & df["Lev_OK"]
    return df

# Step 3: Get compliance percentage
def calc_rate(df):
    return df["Compliant"].mean() * 100

# Step 4: Process data
df = compute_metrics(df)
df = evaluate_compliance(df)
rate = calc_rate(df)

# Step 5: Create Plotly figure
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["Date"], y=df["CAR"], mode="lines", name="CAR",
    line=dict(color="#FF6B6B", width=2)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=[0.08]*len(df), mode="lines", name="CAR Min",
    line=dict(color="#4ECDC4", width=1, dash="dash")
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=df["LCR"], mode="lines", name="LCR", yaxis="y2",
    line=dict(color="#FF6B6B", width=2)
))
fig.add_trace(go.Scatter(
    x=df["Date"], y=[1.0]*len(df), mode="lines", name="LCR Min", yaxis="y2",
    line=dict(color="#4ECDC4", width=1, dash="dash")
))

# Step 6: Customize layout and axes
fig.update_layout(
    title=dict(
        text=f"Compliance Tracker (Rate: {rate:.1f}%)",
        font=dict(color="white", size=16)
    ),
    xaxis=dict(
        title=dict(text="Date", font=dict(color="white", size=14)),
        tickfont=dict(color="white", size=12),
        tickmode="array",
        tickvals=df["Date"][::3],  # Every 3rd month
        ticktext=[d.strftime("%b %Y") for d in df["Date"][::3]],  # Custom text
        ticks="outside",
        ticklen=8,
        gridcolor="rgba(255, 255, 255, 0.1)",
        gridwidth=0.5,
        zeroline=False  # No zeroline for date axis
    ),
    yaxis=dict(
        title=dict(text="CAR", font=dict(color="white", size=14)),
        tickfont=dict(color="white", size=12),
        tickformat=".1%",
        ticks="outside",
        gridcolor="rgba(255, 255, 255, 0.1)",
        gridwidth=0.5,
        zeroline=True,
        zerolinecolor="rgba(255, 255, 255, 0.2)",
        zerolinewidth=1
    ),
    yaxis2=dict(
        title=dict(text="LCR", font=dict(color="white", size=14)),
        tickfont=dict(color="white", size=12),
        tickformat=".2f",
        overlaying="y",
        side="right",
        zeroline=False
    ),
    plot_bgcolor="rgb(40, 40, 40)",
    paper_bgcolor="rgb(40, 40, 40)",
    legend=dict(font=dict(color="white")),
    margin=dict(l=50, r=50, t=50, b=50)
)

# Step 7: Display plot
fig.show()

# Step 8: Print summary
print(f"Compliance Rate: {rate:.1f}%")
print(f"Avg CAR: {df['CAR'].mean():.3f}")
print(f"Avg LCR: {df['LCR'].mean():.3f}")
print(f"Avg Leverage: {df['Lev'].mean():.3f}")