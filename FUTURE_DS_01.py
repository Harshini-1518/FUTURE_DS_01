import sys
print("Python path in use:")
print(sys.executable)

import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

df = pd.read_excel(r"C:\Users\ATS\OneDrive\Desktop\FUTURE_DS_01.xlsx")

print("\nDATA LOADED SUCCESSFULLY")
print(df.head())
print(df.columns)

# CLEAN DATA

df = df.dropna()

# REVENUE COLUMN

df["Revenue"] = df["Sales"]

# KPI ANALYSIS

total_revenue = df["Revenue"].sum()
avg_revenue = df["Revenue"].mean()
total_orders = df.shape[0]

print("\n===== KPI REPORT =====")
print("Total Revenue:", total_revenue)
print("Average Revenue:", avg_revenue)
print("Total Orders:", total_orders)

# TOP PRODUCTS

top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)

print("\n===== TOP PRODUCTS =====")
print(top_products)

top_products.plot(kind="bar")
plt.title("Top 10 Selling Products")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

# CATEGORY PERFORMANCE

category_sales = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)

print("\n===== CATEGORY PERFORMANCE =====")
print(category_sales)

category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

# REGION PERFORMANCE

region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)

print("\n===== REGION PERFORMANCE =====")
print(region_sales)

region_sales.plot(kind="bar")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# MONTHLY SALES TREND

if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"])

    monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Revenue"].sum()

    print("\n===== MONTHLY SALES TREND =====")
    print(monthly_sales)

    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()

print("\nANALYSIS COMPLETED SUCCESSFULLY")
