import math

def simpson_rule(f, a, b, n):
    if n % 2 == 1:  # Simpson's rule requires an even number of subintervals
        raise ValueError("n must be an even number")

    h = (b - a) / n
    I = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            I += 2 * f(a + i * h)
        else:
            I += 4 * f(a + i * h)

    I *= h / 3

    print(f"Approximate Integration for function dx from {a} to {b} with {n} sub-intervals is: {I}")

# Example: Integral from 0 to π for sin(x) where n = 4
def sin_func(x):
    return math.sin(x)

simpson_rule(sin_func, 0, math.pi, 4)
