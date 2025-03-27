def euler_method(f, x0, y0, h, xn):
    n = int((xn - x0) / h)  
    x, y = x0, y0

    for _ in range(n):
        y += h * f(x, y)
        x += h

    return y

def f(x, y):
    return x + y**2

xn=1.6

print(f"y({xn}) = {euler_method(f, 1, 1, 0.1,xn):.6f}")
