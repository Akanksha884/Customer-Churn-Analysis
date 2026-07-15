"""
====================================================
Customer Churn Analysis Project
Author : Akanksha Tyagi
====================================================
"""

# ==============================
# STEP 1 : Import Libraries
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("All Libraries Imported Successfully ✅")

# ==============================
# STEP 2 : Load Dataset
# ==============================

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("\nDataset Loaded Successfully ✅")
# ==============================
# STEP 3 : View First 5 Records
# ==============================

print("\nFirst 5 Rows of Dataset")
print(df.head())
print("\nLast 5 Rows of Dataset")
print(df.tail())
print("\nShape of Dataset")
print(df.shape)
print("\nColumn Names")
print(df.columns)
print("\nData Types")
print(df.dtypes)
print("\n================ Dataset Information ================\n")
df.info()
print("\n================ Statistical Summary ================\n")
print(df.describe())
print("\n================ Missing Values ================\n")
print(df.isnull().sum())
print("\n================ Duplicate Records ================\n")
print(df.duplicated().sum())
print("\n================ Unique Values ================\n")

for column in df.columns:
    print(f"{column} : {df[column].nunique()} unique values")
    print("\n================ Churn Distribution ================\n")
print(df["Churn"].value_counts())
# ==============================
# STEP 5 : Gender Distribution
# ==============================

plt.figure(figsize=(6,4))

sns.countplot(x="gender", data=df)

plt.title("Gender Distribution")

plt.xlabel("Gender")

plt.ylabel("Number of Customers")

plt.savefig("images/gender_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
# ==============================
# STEP 6 : Churn Distribution
# ==============================

plt.figure(figsize=(6,4))

sns.countplot(x="Churn", data=df)

plt.title("Customer Churn Distribution")

plt.xlabel("Churn")

plt.ylabel("Number of Customers")

plt.savefig("images/churn_distribution.png", dpi=300, bbox_inches="tight")

plt.show()
# ==============================
# STEP 7 : Gender vs Churn
# ==============================

plt.figure(figsize=(7,5))

sns.countplot(x="gender", hue="Churn", data=df)

plt.title("Gender vs Customer Churn")

plt.xlabel("Gender")

plt.ylabel("Number of Customers")

plt.savefig("images/gender_vs_churn.png", dpi=300, bbox_inches="tight")

plt.show()
# ==============================
# STEP 8 : Tenure Statistics
# ==============================

print("\n================ Tenure Statistics ================\n")

print(df["tenure"].describe())
# ==============================
# STEP 9 : Tenure Distribution
# ==============================

plt.figure(figsize=(8,5))

plt.hist(df["tenure"], bins=20)

plt.title("Distribution of Customer Tenure")

plt.xlabel("Tenure (Months)")

plt.ylabel("Number of Customers")

plt.savefig("images/tenure_distribution.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 9 : Tenure vs Churn
# ==============================

plt.figure(figsize=(8,5))

sns.boxplot(x="Churn", y="tenure", data=df)

plt.title("Tenure vs Customer Churn")

plt.xlabel("Churn")

plt.ylabel("Tenure (Months)")

plt.savefig("images/tenure_vs_churn.png", dpi=300, bbox_inches="tight")

plt.show()
# ==============================
# STEP 10 : Monthly Charges Distribution
# ==============================

plt.figure(figsize=(8,5))

plt.hist(df["MonthlyCharges"], bins=25)

plt.title("Distribution of Monthly Charges")

plt.xlabel("Monthly Charges")

plt.ylabel("Number of Customers")

plt.savefig("images/monthly_charges_distribution.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 11 : Monthly Charges vs Churn
# ==============================

plt.figure(figsize=(8,5))

sns.boxplot(x="Churn",
            y="MonthlyCharges",
            data=df)

plt.title("Monthly Charges vs Churn")

plt.xlabel("Churn")

plt.ylabel("Monthly Charges")

plt.savefig("images/monthly_charges_vs_churn.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 12 : Contract Type vs Churn
# ==============================

plt.figure(figsize=(8,5))

sns.countplot(x="Contract",
              hue="Churn",
              data=df)

plt.title("Contract Type vs Churn")

plt.xlabel("Contract Type")

plt.ylabel("Number of Customers")

plt.xticks(rotation=15)

plt.savefig("images/contract_vs_churn.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 13 : Internet Service Distribution
# ==============================

plt.figure(figsize=(8,5))

sns.countplot(x="InternetService", data=df)

plt.title("Internet Service Distribution")

plt.xlabel("Internet Service")

plt.ylabel("Number of Customers")

plt.savefig("images/internet_service_distribution.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 14 : Internet Service vs Churn
# ==============================

plt.figure(figsize=(8,5))

sns.countplot(
    x="InternetService",
    hue="Churn",
    data=df
)

plt.title("Internet Service vs Churn")

plt.xlabel("Internet Service")

plt.ylabel("Number of Customers")

plt.savefig("images/internet_service_vs_churn.png",
            dpi=300,
            bbox_inches="tight")

plt.show()
# ==============================
# STEP 15 : ML Preparation
# ==============================

data = df.copy()

print(data.head())
print("\nData Types")

print(data.dtypes)
data.drop("customerID", axis=1, inplace=True)

print(data.head())
# Convert TotalCharges to numeric
data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"],
    errors="coerce"
)

# Fill missing values using median
data["TotalCharges"] = data["TotalCharges"].fillna(
    data["TotalCharges"].median()
)

# Verify
print("\nMissing values in TotalCharges:")
print(data["TotalCharges"].isnull().sum())
print("\nRemaining Missing Values")
print(data.isnull().sum())
# ==============================
# STEP 16 : Encode Target
# ==============================

data["Churn"] = data["Churn"].map(
    {
        "Yes":1,
        "No":0
    }
)

print(data["Churn"].head())
categorical_columns = data.select_dtypes(
    include="object"
).columns

print(categorical_columns)
data = pd.get_dummies(
    data,
    columns=categorical_columns,
    drop_first=True
)

print(data.head())
# ==============================
# STEP 17 : Split Features & Target
# ==============================

X = data.drop("Churn", axis=1)

y = data["Churn"]

print("Features Shape :", X.shape)

print("Target Shape :", y.shape)
from sklearn.model_selection import train_test_split
# ==============================
# STEP 18 : Train Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data")

print(X_train.shape)

print(y_train.shape)

print("\nTesting Data")

print(X_test.shape)

print(y_test.shape)
# ==============================
# STEP 23 : Feature Scaling
# ==============================
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
scaler = StandardScaler()

numerical_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X_train[numerical_columns] = scaler.fit_transform(
    X_train[numerical_columns]
)

X_test[numerical_columns] = scaler.transform(
    X_test[numerical_columns]
)

print("Feature Scaling Completed ✅")
from sklearn.linear_model import LogisticRegression
# ==============================
# STEP 18 : Logistic Regression
# ==============================

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model Trained Successfully ✅")
y_pred = model.predict(X_test)

print("\nFirst 10 Predictions")

print(y_pred[:10])

print("\nActual Values")

print(y_test.values[:10])
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
# ==============================
# STEP 19 : Model Evaluation
# ==============================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy")

print(f"{accuracy:.4f}")
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")

print(cm)

print("\nClassification Report")

print(classification_report(y_test, y_pred))
plt.figure(figsize=(6,5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.savefig(
    "images/confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
from sklearn.tree import DecisionTreeClassifier
# ==========================
# Decision Tree
# ==========================

dt_model = DecisionTreeClassifier(
    random_state=42
)
dt_model.fit(
    X_train,
    y_train
)
dt_pred = dt_model.predict(
    X_test
)
dt_accuracy = accuracy_score(
    y_test,
    dt_pred
)

print("\nDecision Tree Accuracy")

print(dt_accuracy)
print(
classification_report(
    y_test,
    dt_pred
))
dt_cm = confusion_matrix(
    y_test,
    dt_pred
)

print(dt_cm)
plt.figure(figsize=(6,5))

sns.heatmap(
    dt_cm,
    annot=True,
    fmt="d",
    cmap="Greens"
)

plt.title("Decision Tree Confusion Matrix")

plt.savefig(
"images/dt_confusion_matrix.png",
dpi=300,
bbox_inches="tight"
)

plt.show()
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf_model.fit(
    X_train,
    y_train
)
rf_pred = rf_model.predict(
    X_test
)
rf_accuracy = accuracy_score(
    y_test,
    rf_pred
)

print(
"\nRandom Forest Accuracy"
)

print(rf_accuracy)
print(
classification_report(
    y_test,
    rf_pred
))
rf_cm = confusion_matrix(
    y_test,
    rf_pred
)

plt.figure(figsize=(6,5))

sns.heatmap(
    rf_cm,
    annot=True,
    fmt="d",
    cmap="Oranges"
)

plt.title(
"Random Forest Confusion Matrix"
)

plt.savefig(
"images/rf_confusion_matrix.png",
dpi=300,
bbox_inches="tight"
)

plt.show()
results = pd.DataFrame({

    "Model":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "Accuracy":[
        accuracy,
        dt_accuracy,
        rf_accuracy
    ]

})

print(results)
plt.figure(figsize=(8,5))

sns.barplot(
    data=results,
    x="Model",
    y="Accuracy"
)

plt.title(
"Model Comparison"
)

plt.savefig(
"images/model_comparison.png",
dpi=300,
bbox_inches="tight"
)

plt.show()
importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

importance["Absolute"] = importance["Coefficient"].abs()

importance = importance.sort_values(
    by="Absolute",
    ascending=False
)

print(importance.head(15))
top15 = importance.head(15)

plt.figure(figsize=(10,6))

plt.barh(
    top15["Feature"],
    top15["Coefficient"]
)

plt.title("Top 15 Important Features")

plt.xlabel("Coefficient")

plt.tight_layout()

plt.savefig(
    "images/feature_importance.png",
    dpi=300
)

plt.show()
from sklearn.metrics import roc_curve, roc_auc_score
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
auc_score = roc_auc_score(y_test, y_prob)

print(f"AUC Score : {auc_score:.4f}")
plt.figure(figsize=(8,6))

plt.plot(fpr, tpr, label=f"AUC = {auc_score:.4f}")

plt.plot([0,1], [0,1], linestyle="--")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve - Logistic Regression")

plt.legend()

plt.grid(True)

plt.savefig(
    "images/roc_curve.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
import pickle
# ==============================
# Save Best Model
# ==============================

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Saved Successfully ✅")
with open("scaler.pkl", "wb") as file:
    pickle.dump(scaler, file)

print("Scaler Saved Successfully ✅")


