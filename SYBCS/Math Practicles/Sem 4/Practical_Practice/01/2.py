# x**3 - 2*x - 5 in 2,3

def rf(f,x0,x1,e):
    if f(x0) * f(x1) > 0 :
        return "Invalid Interval"
    
    while True:
        x2 = x0 - (x1-x0) * f(x0) / (f(x1) - f(x0))

        if abs(f(x2)) < e :
            return f"Required Root : {x2:.4f}"
        
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

def f(x):
    return x**3 - 2*x - 5

print(rf(f,2,3,0.00001))