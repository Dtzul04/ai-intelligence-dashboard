import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_my_model():

    data_path = os.path.join('data', 'customer_Data.csv')
    df = pd.read_csv(data_path)

    x = df[['tenure', 'MonthlyCharges']]
    y = df['Churn']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)       

    model = LogisticRegression()
    model.fit(x_train, y_train)     

    if not os.path.exists('models'):
        os.makedirs('models')

    joblib.dump(model, os.path.join('models', 'logistic_regression_model.pkl')) 
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    train_my_model()
           