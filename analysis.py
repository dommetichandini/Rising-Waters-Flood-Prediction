import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create static folder if not exists
os.makedirs("static", exist_ok=True)

# ✅ Reading Dataset
print("=" * 50)
print("READING DATASET")
print("=" * 50)
dataset = pd.read_excel("flood dataset.xlsx", engine="openpyxl")
print("Shape:", dataset.shape)
print("Columns:", dataset.columns.tolist())
print(dataset.head())

# ✅ Descriptive Analysis
print("\n" + "=" * 50)
print("DESCRIPTIVE ANALYSIS")
print("=" * 50)
print(dataset.describe())

# ✅ Missing Values
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(dataset.isnull().sum())

# ✅ Univariate Analysis
print("\nGenerating Univariate Analysis...")
dataset.hist(figsize=(14, 10), color='steelblue', edgecolor='black')
plt.suptitle("Univariate Analysis", fontsize=16)
plt.tight_layout()
plt.savefig("static/univariate.png")
plt.close()
print("Saved: static/univariate.png")

# ✅ Multivariate Analysis - Correlation Heatmap
print("\nGenerating Multivariate Analysis...")
plt.figure(figsize=(12, 8))
numeric_df = dataset.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Multivariate Analysis - Correlation Heatmap", fontsize=14)
plt.tight_layout()
plt.savefig("static/correlation.png")
plt.close()
print("Saved: static/correlation.png")

# ✅ Flood vs No Flood Count Plot
plt.figure(figsize=(6, 4))
target_col = dataset.columns[-1]  # last column = target
dataset[target_col].value_counts().plot(kind='bar', color=['green', 'red'])
plt.title("Flood vs No Flood Count")
plt.xlabel("Flood")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("static/flood_count.png")
plt.close()

print("\n✅ Analysis Complete!")