import math

def simpson_rule(f, a, b, n):
    h = (b - a) / n
    I = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            I += 2 * f(a + i * h)
        else:
            I += 4 * f(a + i * h)

    I *= h / 3

    return (f"Result : {I}")

def f(x):
    return math.sin(x)

print(simpson_rule(f, 0, math.pi, 4))
