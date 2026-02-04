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
    # This is where we will grab the data next time
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)