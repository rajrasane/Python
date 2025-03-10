import math

def s_3_8rd_rule(a, b, n, f):
    h = float(b - a) / n
    I = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 3 == 0:
            I = I + 2 * f(k)
        else:
            I = I + 3 * f(k)
    I = (3 * h / 8) * I
    print(f"Approximate Integration for function f from {a} to {b} with {n} sub-intervals is: {I:.6f}")

def f(x):
    return math.sin(x)

s_3_8rd_rule(0, math.pi, 4, f)
