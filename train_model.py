import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

os.makedirs("models", exist_ok=True)

# ✅ Reading Dataset
print("=" * 50)
print("LOADING DATASET")
print("=" * 50)
dataset = pd.read_excel("flood dataset.xlsx", engine="openpyxl")
print("Shape:", dataset.shape)
print(dataset.head())

# ✅ Handling Missing Values
dataset.fillna(dataset.mean(numeric_only=True), inplace=True)
print("\n✅ Missing values handled")

# ✅ Handling Categorical Values
dataset = pd.get_dummies(dataset)
print("✅ Categorical values encoded")

# ✅ Features and Target
target_col = dataset.columns[-1]
X = dataset.drop(columns=[target_col])
y = dataset[target_col]

print(f"\nTarget Column: {target_col}")
print(f"Features: {X.shape[1]}")

# ✅ Handling Outliers (IQR Method)
Q1 = X.quantile(0.25)
Q3 = X.quantile(0.75)
IQR = Q3 - Q1
X = X[~((X < (Q1 - 1.5 * IQR)) | (X > (Q3 + 1.5 * IQR))).any(axis=1)]
y = y[X.index]
print("✅ Outliers handled")

# ✅ Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\n✅ Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

# ✅ Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("✅ Feature Scaling done")

# ✅ Model Building
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "XGBoost": XGBClassifier(random_state=42, eval_metric='logloss')
}

print("\n" + "=" * 50)
print("MODEL TRAINING & COMPARISON")
print("=" * 50)

best_model = None
best_accuracy = 0
best_name = ""

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n{name} Accuracy: {acc * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    if acc > best_accuracy:
        best_accuracy = acc
        best_model = model
        best_name = name

print("=" * 50)
print(f"\n🏆 Best Model: {best_name} — Accuracy: {best_accuracy * 100:.2f}%")

# ✅ Saving Best Model and Scaler
pickle.dump(best_model, open("models/flood_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(list(X.columns), open("models/features.pkl", "wb"))

print("\n✅ Model saved: models/flood_model.pkl")
print("✅ Scaler saved: models/scaler.pkl")
print("✅ Features saved: models/features.pkl")