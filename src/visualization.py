import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the trained model
rf_model = joblib.load('rf_model.joblib')

# Load or define feature names
feature_names = joblib.load('feature_names.joblib')

# Get feature importances
importances = rf_model.feature_importances_

# Create a dataframe of features and their importances
feature_imp = pd.DataFrame({'feature': feature_names, 'importance': importances})

# Sort the dataframe by importance, descending
feature_imp = feature_imp.sort_values('importance', ascending=False).reset_index(drop=True)

# Select top 10 features
top_10_features = feature_imp.head(10)

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='importance', y='feature', data=top_10_features)
plt.title('Top 10 Most Important Features for Data Exfiltration Detection')
plt.xlabel('Importance Score')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig('feature_importance.png')
plt.show()

print("Feature importance visualization saved as 'feature_importance.png'")