import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# 1. Create the dataset
np.random.seed(42) 

data = pd.DataFrame({
    'ID': np.arange(1, 501),
    'flat': np.random.randint(1, 100, 500),         # Flats available
    'houses': np.random.randint(1, 50, 500),        # Houses available
})

# 2. Generate 'Sales' with some correlation
data['purchases'] = (
    1.5 * data['flat'] +
    2.8 * data['houses'] +
    np.random.normal(0, 10, 500) 
)

# 3. Define independent and target variables
X = data[['flat', 'houses']]
y = data['purchases']

# 4. Split into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Print training and testing data
print("Training features (X_train):\n", X_train.head(), "\n")
print("Training target (y_train):\n", y_train.head(), "\n")
print("Testing features (X_test):\n", X_test.head(), "\n")
print("Testing target (y_test):\n", y_test.head(), "\n")

# 5. Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Print model coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("Feature Names:", X.columns.tolist())

y_pred = model.predict(X_test)

# 8. Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 9. Visualization: Actual vs Predicted Purchases
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Purchases')
plt.xlabel('Actual Purchases')
plt.ylabel('Predicted Purchases')
plt.grid(True)
plt.tight_layout()
plt.show()