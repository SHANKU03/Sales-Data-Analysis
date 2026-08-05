import pandas as pd

# Load dataset
df = pd.read_csv("../Dataset/train.csv")

# Show first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Summary statistics
print(df.describe())
