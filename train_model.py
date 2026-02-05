import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

print("1. Loading data...")
df = pd.read_csv('data/customer_data.csv')

X = df[['tenure', 'MonthlyCharges', 'Contract']]
y = df['Churn']

print("2. Training model...")
model = LogisticRegression()
model.fit(X, y)

print("3. Saving model...")
joblib.dump(model, 'logistic_regression_model.pkl')

print("--- FINISHED! Check 'ls' now ---")