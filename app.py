from flask import Flask, render_template, request
import joblib 
import numpy as np

app = Flask(__name__)
model = joblib.load('models/logistic_regression_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tenure = request.form.get('tenure')
    monthly_charges = request.form.get('monthly_charges')
    contract_type = request.form.get('contract_type')

    tenure_val = float(tenure)
    monthly_val = float(monthly_charges)
    contract_val = int(contract_type)

    features = [tenure_val, monthly_val, contract_val]
    prediction = model.predict([features])[0]

    result = "Likely to Churn" if prediction == 1 else "Unlikely to Churn"

    return render_template('index.html', 
                            prediction=result,
                            tenure=tenure,
                            monthly_charges=monthly_charges,
                            contract=contract_val)

if __name__ == '__main__':
    import os 
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)