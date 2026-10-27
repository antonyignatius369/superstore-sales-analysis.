# Superstore Sales Analysis
# Run in Google Colab after uploading "Sample - Superstore.csv".
# If your CSV has another name, update CSV_PATH below.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

CSV_PATH = "/content/Sample - Superstore.csv"
df = pd.read_csv(CSV_PATH)

# Q1. Dataset size and structure
print("Q1: Dataset shape:", df.shape)
print("\nColumns:\n", df.columns.tolist())
print("\nData types and non-null counts:")
df.info()
display(df.head())

# Parse dates using month/day/year format in the standard dataset
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Q2. Missing values and duplicates
print("\nQ2: Missing values by column:")
display(df.isna().sum().sort_values(ascending=False))
print("Exact duplicate rows:", df.duplicated().sum())
print("Duplicate Row ID values:", df["Row ID"].duplicated().sum() if "Row ID" in df.columns else "N/A")

# Clean: retain first occurrence of exact duplicates only, if any.
df = df.drop_duplicates().copy()
# Check date parsing and required numeric fields
for col in ["Sales", "Profit", "Quantity", "Discount"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Q3. Sales, profit, and average order-line sales
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_line_sales = df["Sales"].mean()
print(f"\nQ3: Total sales = ${total_sales:,.2f}")
print(f"Total profit = ${total_profit:,.2f}")
print(f"Average order-line sales = ${avg_line_sales:,.2f}")
print(f"Distinct orders = {df['Order ID'].nunique():,}")

# Q4. Product category sales
category_sales = df.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
print("\nQ4: Sales by category:")
display(category_sales)
sns.barplot(data=category_sales, x="Category", y="Sales")
plt.title("Total Sales by Product Category")
plt.ylabel("Sales (USD)")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Q5. Highest and lowest profit sub-categories
subcategory_profit = df.groupby("Sub-Category", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False)
print("\nQ5: Sub-categories ranked by total profit:")
display(subcategory_profit)
print("Highest profit:", subcategory_profit.iloc[0].to_dict())
print("Lowest profit:", subcategory_profit.iloc[-1].to_dict())
plt.figure(figsize=(10, 6))
sns.barplot(data=subcategory_profit, x="Profit", y="Sub-Category")
plt.title("Total Profit by Sub-Category")
plt.tight_layout()
plt.show()

# Q6. Region with highest sales
region_sales = df.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
print("\nQ6: Sales by region:")
display(region_sales)
print("Highest-sales region:", region_sales.iloc[0].to_dict())

# Q7. Customer segment contributing most sales
segment_sales = df.groupby("Segment", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
print("\nQ7: Sales by customer segment:")
display(segment_sales)
print("Top segment:", segment_sales.iloc[0].to_dict())

# Q8. Relationship between discounts and profit
discount_profit = df.groupby("Discount", as_index=False).agg(
    Average_Profit=("Profit", "mean"),
    Total_Profit=("Profit", "sum"),
    Line_Count=("Profit", "size"),
    Total_Sales=("Sales", "sum")
).sort_values("Discount")
print("\nQ8: Profit metrics by discount level:")
display(discount_profit)
print("Pearson correlation (discount vs profit):", df[["Discount", "Profit"]].corr().iloc[0, 1])
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.35)
plt.title("Discount vs Profit per Order Line")
plt.tight_layout()
plt.show()

# Q9. Sales over time
df["Order Year"] = df["Order Date"].dt.year
annual_sales = df.groupby("Order Year", as_index=False)["Sales"].sum().sort_values("Order Year")
monthly_sales = df.set_index("Order Date").resample("MS")["Sales"].sum().reset_index()
print("\nQ9: Annual sales:")
display(annual_sales)
plt.figure(figsize=(9, 4))
sns.lineplot(data=annual_sales, x="Order Year", y="Sales", marker="o")
plt.title("Annual Sales Trend")
plt.ylabel("Sales (USD)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
sns.lineplot(data=monthly_sales, x="Order Date", y="Sales")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales (USD)")
plt.tight_layout()
plt.show()

# Q10. Business recommendations informed by the results above
print("""
Q10: Business recommendations
1. Protect and expand profitable categories and sub-categories after checking margins, not sales alone.
2. Review loss-making sub-categories (especially Tables in the standard dataset) for pricing, sourcing, shipping, and discount policy.
3. Evaluate discount levels using both average and total profit; introduce approval thresholds for discounts that repeatedly produce losses.
4. Use the strongest region and customer segment as benchmarks, while investigating opportunities in lower-sales regions.
5. Plan inventory and campaigns around monthly/annual patterns, while remembering this dataset covers 2014–2017.
6. Validate findings with current company data before making operational decisions; this is a historical sample dataset.
""")
