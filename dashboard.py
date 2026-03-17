# ================================
# Interactive Sales Dashboard
# ================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Preview data
print(df.head())

# Set visualization style
sns.set_style("whitegrid")
# ==================================
# 1. Sales Trend Over Time (Line Plot)
# ==================================

daily_sales = df.groupby("Date")["Total_Sales"].sum()

plt.figure(figsize=(10,5))
sns.lineplot(x=daily_sales.index, y=daily_sales.values)

plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.show()
# ==================================
# 2. Product Performance (Bar Chart)
# ==================================

product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values()

plt.figure(figsize=(8,5))

sns.barplot(
    x=product_sales.values,
    y=product_sales.index,
    palette="viridis"
)

plt.title("Sales by Product")
plt.xlabel("Total Sales")
plt.ylabel("Product")


plt.show()
# ==================================
# 3. Price Distribution (Box Plot)
# ==================================

plt.figure(figsize=(8,5))

sns.boxplot(
    x="Product",
    y="Price",
    data=df,
    palette="Set2"
)

plt.title("Price Distribution by Product")


plt.show()
# ==================================
# 4. Sales Distribution (Violin Plot)
# ==================================

plt.figure(figsize=(8,5))

sns.violinplot(
    x="Region",
    y="Total_Sales",
    data=df,
    palette="coolwarm"
)

plt.title("Sales Distribution by Region")


plt.show()
# ==================================
# 5. Correlation Heatmap
# ==================================

corr = df[["Quantity", "Price", "Total_Sales"]].corr()

plt.figure(figsize=(6,5))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix")


plt.show()
# ==================================
# INTERACTIVE DASHBOARD (Plotly)
# ==================================

# Sales by Product
product_sales = df.groupby("Product")["Total_Sales"].sum().reset_index()

fig1 = px.bar(
    product_sales,
    x="Product",
    y="Total_Sales",
    color="Product",
    title="Interactive Sales by Product"
)

fig1.show()


# Sales by Region
region_sales = df.groupby("Region")["Total_Sales"].sum().reset_index()

fig2 = px.pie(
    region_sales,
    values="Total_Sales",
    names="Region",
    title="Regional Sales Distribution"
)

fig2.show()
# ==================================
# MULTI-PLOT DASHBOARD
# ==================================

trend = df.groupby("Date")["Total_Sales"].sum()
prod = df.groupby("Product")["Total_Sales"].sum()
region = df.groupby("Region")["Total_Sales"].sum()

fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Sales Trend",
        "Product Sales",
        "Region Sales",
        "Quantity vs Price"
    )
)

# Sales Trend
fig.add_trace(
    go.Scatter(
        x=trend.index,
        y=trend.values,
        mode='lines',
        name="Sales Trend"
    ),
    row=1,
    col=1
)

# Product Sales
fig.add_trace(
    go.Bar(
        x=prod.index,
        y=prod.values,
        name="Product Sales"
    ),
    row=1,
    col=2
    )

# Region Sales
fig.add_trace(
    go.Bar(
        x=region.index,
        y=region.values,
        name="Region Sales"
    ),
    row=2,
    col=1
)

# Quantity vs Price
fig.add_trace(
    go.Scatter(
        x=df["Quantity"],
        y=df["Price"],
        mode='markers',
        name="Quantity vs Price"
    ),
    row=2,
    col=2
)

fig.update_layout(
    title="Interactive Sales Dashboard",
    height=700,
    showlegend=False
)

fig.show()

print("Dashboard Generated Successfully!")