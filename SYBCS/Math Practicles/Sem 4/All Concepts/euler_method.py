import numpy as np

def euler_method(f, x0, y0, h, xn):
    n = int((xn - x0) / h)  # Number of steps
    X = np.linspace(x0, xn, n + 1)  # Create x values
    Y = np.zeros(n + 1)  # Array to store y values
    Y[0] = y0  # Set initial y value

    for i in range(n):
        Y[i + 1] = Y[i] + h * f(X[i], Y[i])  # Euler formula

    return X, Y

# Function defining the ODE dy/dx = x + y
def f(x, y):
    return x + y

# Initial Conditions
x0, y0 = 0, 1  # y(0) = 1
h = 0.1        # Step size
xn = 0.3       # Solve until x = 0.3

# Compute solution using Euler's method
X, Y = euler_method(f, x0, y0, h, xn)

# Display results
for i in range(len(X)):
    print(f"x = {X[i]:.2f}, y = {Y[i]:.4f}")
