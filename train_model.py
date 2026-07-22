import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("data.csv")

# Features (input)
X = data[['hours', 'attendance']]

# Target (output)
y = data['marks']

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as model.pkl")