import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)

data = pd.DataFrame({
    'ID' : np.arange(1, 501),
    'TV' : np.random.randint(10, 300, 500),
    'Radio' : np.random.randint(5, 50, 500),
    'Newspaper' : np.random.randint(0, 100, 500)
})

data['Sales']=(
    0.045 * data['TV'] +
    0.187 * data['Radio'] +
    0.005 * data['Newspaper'] +
    np.random.normal(0, 1, 500)
)

x = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

print("Training features (X train ):\n", x_train.head(),"\n")
print("Training target (y train ):\n", y_train.head(),"\n")
print("Testing features (X test ):\n", x_test.head(),"\n")
print("Testing target (y test ):\n", y_test.head(),"\n")

model = LinearRegression()
model.fit(x_train, y_train)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("Feature names:", x_train.columns.tolist())

y_pred = model.predict(x_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R^2: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.grid(True)
plt.tight_layout()
plt.show()