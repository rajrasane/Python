def falseposition(f, x0, x1, e):
    x0 = float(x0)
    x1 = float(x1)
    e = float(e)

    if f(x0) * f(x1) > 0.0:
        print('Given values do not bracket a root.')
        print('Try with another set of values.')
        return
    
    step = 1
    condition = True
    
    while condition:
        # Calculate the new approximation using the False Position formula
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        
        print('Iteration %d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))
        
        # If the new approximation is between x0 and x2, update x1
        if f(x0) * f(x2) < 0:
            x1 = x2
        # Otherwise, update x0
        else:
            x0 = x2
        
        step += 1
        
        # Check convergence: if the absolute value of f(x2) is less than tolerance e
        condition = abs(f(x2)) > e
    
    print('\nRequired root is: %0.8f' % x2)

# Example function 1: f(x) = x^3 - 3x + 1
def f1(x):
    return x**3 - 3*x + 1

# Example function 2: f(x) = x^3 - 2x - 5
def f2(x):
    return x**3 - 2*x - 5

# Calling the function for the first example with initial guesses 0 and 1
falseposition(f1, 0, 1, 0.00001)

# Calling the function for the second example with initial guesses 2 and 3
falseposition(f2, 2, 3, 0.00001)
