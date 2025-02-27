import math

def f(x):
    return (x * math.sin(x)) * math.cos(x)

def falsi(x0, x1, n, f):
    for i in range(n):
        x2 = x0 - (f(x0) * (x1 - x0)) / (f(x1) - f(x0))

        print(f"Iteration {i+1}: x2 = {x2}")

        if abs(f(x2)) < 1e-6:
            print(f"Root found at x = {x2}")
            return x2

        if f(x0) * f(x2) < 0:
            x1 = x2 
        else:
            x0 = x2  
    
    print("Max iterations reached")
    return x2  

root = falsi(1, 3, 4, f)
print(f"Final approximation of the root: {root}")
