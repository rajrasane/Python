def falseposition(f, x0, x1, e):
    if f(x0) * f(x1) > 0:
        print('Invalid interval.')
        return
    
    while True:
        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        if abs(f(x2)) <= e:
            print(f'Required root: {x2:.8f}')
            return
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

def f(x):
    return x**3 - 3*x + 1

falseposition(f, 0, 1, 0.00001)
