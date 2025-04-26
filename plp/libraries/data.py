import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Set style for better looking plots
plt.style.use('seaborn-v0_8')

# ========== DATA LOADING & CLEANING ==========
# Create sample sales data (or replace with pd.read_csv('your_data.csv'))
data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'Product': ['Laptop', 'Laptop', 'Laptop', 'Mouse', 'Mouse', 'Keyboard'],
    'Quantity': [10, 15, 8, 25, 30, 12],
    'Unit_Price': [1200, 1200, 1200, 25, 25, 45],
    'Region': ['East', 'West', 'East', 'West', 'East', 'North']
}

df = pd.DataFrame(data)

# Calculate Revenue and add as new column
df['Revenue'] = df['Quantity'] * df['Unit_Price']

# Convert Date to datetime and extract features
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day_name()
df['Month'] = df['Date'].dt.month_name()

# ========== DATA ANALYSIS ==========
# 1. Summary Statistics
summary_stats = df.describe()

# 2. Total Revenue
total_revenue = df['Revenue'].sum()

# 3. Best Selling Product (by quantity)
best_seller = df.groupby('Product')['Quantity'].sum().idxmax()

# 4. Revenue by Region
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)

# ========== DATA VISUALIZATION ==========
# Create figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Sales Data Analysis Dashboard', fontsize=16)

# Plot 1: Revenue by Product (Bar Chart)
df.groupby('Product')['Revenue'].sum().sort_values().plot(
    kind='barh',
    ax=axes[0,0],
    color='teal',
    title='Total Revenue by Product'
)
axes[0,0].set_xlabel('Revenue ($)')

# Plot 2: Daily Sales Trend (Line Plot)
df.groupby('Date')['Revenue'].sum().plot(
    kind='line',
    ax=axes[0,1],
    marker='o',
    color='darkorange',
    title='Daily Sales Trend'
)
axes[0,1].set_ylabel('Revenue ($)')
axes[0,1].grid(True, linestyle='--', alpha=0.6)

# Plot 3: Region Distribution (Pie Chart)
region_revenue.plot(
    kind='pie',
    ax=axes[1,0],
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66b3ff','#99ff99','#ffcc99'],
    title='Revenue Distribution by Region'
)

# Plot 4: Quantity vs Revenue Scatter
scatter = axes[1,1].scatter(
    df['Quantity'],
    df['Revenue'],
    c=df['Unit_Price'],
    cmap='viridis',
    s=100,
    alpha=0.7
)
axes[1,1].set_title('Quantity vs Revenue (Color by Unit Price)')
axes[1,1].set_xlabel('Quantity Sold')
axes[1,1].set_ylabel('Revenue ($)')
plt.colorbar(scatter, ax=axes[1,1], label='Unit Price ($)')

# Adjust layout and save
plt.tight_layout()
plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')

# ========== DISPLAY RESULTS ==========
print("=== SALES ANALYSIS REPORT ===")
print(f"\nTotal Revenue: ${total_revenue:,.2f}")
print(f"\nBest Selling Product: {best_seller}")
print("\nRevenue by Region:")
print(region_revenue.to_string())
print("\nSummary Statistics:")
print(summary_stats)

plt.show()