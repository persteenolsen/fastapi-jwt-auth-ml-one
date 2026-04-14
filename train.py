import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv("data.csv")

X = df[["size", "rooms"]]
y = df["price"]

# Split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Validate
score = model.score(X_val, y_val)
print("Validation score:", score)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")