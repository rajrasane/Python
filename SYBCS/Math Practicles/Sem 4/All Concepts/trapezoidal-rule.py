import math

def Tr(a, b, n, f):
    h = float(b - a) / n
    I = f(a) + f(b)  # First and last terms

    for i in range(1, n):
        I += 2 * f(a + i * h)  # Intermediate terms are multiplied by 2
    
    I = (h / 2) * I  # Apply Trapezoidal Rule formula
    return I

def f(x):
    return math.sin(x)  # Corrected function

# Example Usage
result = Tr(0, math.pi, 4, f)
print(f"Approximate integral: {result}")

