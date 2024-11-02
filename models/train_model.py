import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def generate_ip():
    return f"{np.random.randint(1, 256)}.{np.random.randint(0, 256)}.{np.random.randint(0, 256)}.{np.random.randint(0, 256)}"

def generate_log_data(num_records, start_date, end_date):
    data = []
    for _ in range(num_records):
        timestamp = start_date + timedelta(seconds=np.random.randint(0, int((end_date - start_date).total_seconds())))
        source_ip = generate_ip()
        destination_ip = generate_ip()
        source_port = np.random.randint(1024, 65535)
        destination_port = np.random.choice([80, 443, 22, 3389])
        protocol = np.random.choice(['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP'])
        bytes_sent = np.random.randint(100, 10000)
        bytes_received = np.random.randint(100, 10000)
        action = np.random.choice(['allow', 'deny', 'drop'], p=[0.7, 0.2, 0.1])
        
        is_suspicious = np.random.choice([0, 1], p=[0.95, 0.05])
        if is_suspicious:
            bytes_sent = np.random.randint(50000, 1000000)
            destination_ip = np.random.choice(['10.0.0.1', '192.168.1.1'])
        
        data.append([timestamp, source_ip, destination_ip, source_port, destination_port, 
                     protocol, bytes_sent, bytes_received, action, is_suspicious])
    
    columns = ['timestamp', 'source_ip', 'destination_ip', 'source_port', 'destination_port', 
               'protocol', 'bytes_sent', 'bytes_received', 'action', 'is_suspicious']
    
    return pd.DataFrame(data, columns=columns)

# Generate data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
df = generate_log_data(100000, start_date, end_date)

# Preprocess data
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek

# Create dummy variables
df = pd.get_dummies(df, columns=['protocol', 'action'])

# Define features
all_protocols = ['TCP', 'UDP', 'HTTP', 'HTTPS', 'ICMP']
all_actions = ['allow', 'deny', 'drop']

feature_names = ['source_port', 'destination_port', 'bytes_sent', 'bytes_received', 'hour', 'day_of_week'] + \
                [f'protocol_{protocol}' for protocol in all_protocols] + \
                [f'action_{action}' for action in all_actions]

# Ensure all feature columns exist
for col in feature_names:
    if col not in df.columns:
        df[col] = 0

X = df[feature_names]
y = df['is_suspicious']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train the model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_scaled, y_train)

# Evaluate the model
y_pred = rf_model.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

# Save the model, scaler, and feature names
joblib.dump(rf_model, 'rf_model.joblib')
joblib.dump(scaler, 'scaler.joblib')
joblib.dump(feature_names, 'feature_names.joblib')

print("Model, scaler, and feature names saved.")