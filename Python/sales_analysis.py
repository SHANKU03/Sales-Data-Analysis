import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset/train.csv")

# Show first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Summary statistics
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

print("\nTotal Sales")
print(df["Sales"].sum())

print("\nAverage Sales")
print(df["Sales"].mean())

print("\nTop 10 Products")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nCategory Wise Sales")
print(df.groupby("Category")["Sales"].sum())

print("\nRegion Wise Sales")
print(df.groupby("Region")["Sales"].sum())

# Category Wise Sales Chart

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# Region Wise Pie Chart

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(6,6))

plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Region Wise Sales")
plt.show()

# Sales Distribution

plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=30)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()


# Save Charts

category_sales.plot(kind="bar", figsize=(8,5))
plt.title("Category Wise Sales")
plt.tight_layout()
plt.savefig("Images/category_sales.png")
plt.close()

plt.figure(figsize=(6,6))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Region Wise Sales")
plt.savefig("Images/region_sales.png")
plt.close()

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.savefig("Images/sales_distribution.png")
plt.close()

print("\nCharts Saved Successfully!")