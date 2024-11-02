from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model, scaler, and feature names
model = joblib.load('rf_model.joblib')
scaler = joblib.load('scaler.joblib')
feature_names = joblib.load('feature_names.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    
    # Get all possible categories for protocol and action
    all_protocols = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP']
    all_actions = ['allow', 'deny', 'drop']
    
    # Create dummy variables for all possible categories
    for protocol in all_protocols:
        df[f'protocol_{protocol}'] = (df['protocol'] == protocol).astype(int)
    for action in all_actions:
        df[f'action_{action}'] = (df['action'] == action).astype(int)
    
    # Drop original 'protocol' and 'action' columns
    df = df.drop(['protocol', 'action'], axis=1)
    
    # Ensure all expected columns are present
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    
    # Select only the columns that the model expects
    features = df[feature_names]
    
    scaled_features = scaler.transform(features)
    
    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]
    
    return jsonify({
        'prediction': int(prediction),
        'probability': float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True)