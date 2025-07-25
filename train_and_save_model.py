import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load your dataset
heart_data = pd.read_csv('heart.csv')

# Split the data into features and target
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the Logistic Regression model with increased iterations
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Save the trained model as a pickle file
with open('heart_disease_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as heart_disease_model.pkl")
