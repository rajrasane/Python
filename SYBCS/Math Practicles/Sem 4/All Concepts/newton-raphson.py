def newton_raphson(f, g, x0, e, N):
    for step in range(1, N+1):
        if g(x0) == 0:
            print("Divide by zero error!")
            return
        x1 = x0 - f(x0) / g(x0)
        print(f"Iteration-{step}, x1={x1:.6f}, f(x1)={f(x1):.6f}")
        if abs(f(x1)) <= e:
            print(f"\nRoot: {x1:.8f}")
            return
        x0 = x1
    print("\nNot convergent.")

def f(x): return x**3 - 5*x + 1
def g(x): return 3*x**2 - 5

newton_raphson(f, g, 0.1, 1e-5, 100)
