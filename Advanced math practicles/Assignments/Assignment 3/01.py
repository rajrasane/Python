def falsePosition(f, x0, x1, e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(x0) * f(x1) > 0.0:
        print('Given guess values do not bracket the root.')
        print('Try again with different values.')
        return

    else:
        step = 1
        condition = True
        print(f"{'Iteration':<10}{'x2':<15}{'f(x2)':<15}")
        print("-" * 40)

        while condition:
            # False Position formula
            x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
            print(f"{step:<10}{x2:<15.6f}")

            # Update the interval based on the sign of f(x2)
            if f(x0) * f(x2) < 0:
                x1 = x2
            else:
                x0 = x2

            step += 1
            condition = abs(f(x2)) > e  # Convergence check

        print(f"\nRequired root is: {x2:.8f}")


def f(x):
    return x**3 - 3 * x + 1

falsePosition(f, 0, 1, 0.00001)
