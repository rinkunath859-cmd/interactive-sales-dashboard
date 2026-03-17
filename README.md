📊 Interactive Sales Dashboard
📌 Project Overview

The Interactive Sales Dashboard is a data analysis and visualization project designed to explore sales performance across products, regions, and time.

This dashboard combines Seaborn statistical visualizations with Plotly interactive charts to deliver meaningful business insights.

🎯 Objectives

Analyze sales trends over time

Identify top-performing products

Understand regional sales distribution

Explore customer purchasing patterns

Build an interactive dashboard for data exploration

📁 Dataset Description

The dataset contains transactional sales data with the following columns:

Column	Description
Date	Transaction date
Product	Product name
Quantity	Units sold
Price	Price per unit
Customer_ID	Unique customer identifier
Region	Sales region
Total_Sales	Total transaction value
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/sales-dashboard.git
cd sales-dashboard
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Dashboard
python dashboard.py
🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Plotly

📊 Visualizations Included
🔹 1. Sales Trend (Line Chart)

Displays total sales over time

Helps identify trends and seasonality

🔹 2. Product Performance (Bar Chart)

Compares total sales by product

Highlights top-performing products

🔹 3. Price Distribution (Box Plot)

Shows spread of product prices

Identifies outliers

🔹 4. Regional Sales Distribution (Violin Plot)

Displays distribution of sales across regions

Shows density and variation

🔹 5. Correlation Heatmap

Shows relationships between:

Quantity

Price

Total Sales

🔹 6. Interactive Plotly Charts

Interactive bar chart

Pie chart for regional sales

Hover, zoom, and dynamic exploration

📈 Dashboard Layout

Multi-panel dashboard (2×2 grid)

Clean and consistent styling

Interactive and static charts combined

📷 Dashboard Demo

📁 Project Structure
sales-dashboard/

dashboard.py
dashboard.ipynb
sales_data.csv
requirements.txt
dashboard_demo.gif

visualizations/
sales_trend.png
product_sales.png
price_boxplot.png
region_violin.png
correlation_heatmap.png

README.md
🔍 Key Insights

Certain products contribute significantly to total revenue

Sales vary across different regions

Price variations exist within product categories

Strong relationship observed between quantity and total sales

Interactive charts improve data exploration

🧠 Technical Details

Used Pandas groupby() for aggregation

Applied Seaborn for statistical plots

Built Plotly dashboards for interactivity

Implemented subplot layouts for dashboard design

✅ Requirements

Install all dependencies using:

pip install -r requirements.txt
