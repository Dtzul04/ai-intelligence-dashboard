from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    csv_path = os.path.join('data', 'your_file.csv')
    
    df = pd.read_csv(csv_path)
    
    recent_data = df.head(5).to_dict(orient='records')
    
    return render_template('index.html', recent_data=recent_data)

if __name__ == '__main__':
    app.run(debug=True)