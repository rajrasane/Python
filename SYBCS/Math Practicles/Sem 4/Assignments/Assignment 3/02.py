def f(x):
    return x**2 - 4  

def regula_falsi(x0, x1):
    while True:
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        x2 = x0 - (f_x0 * (x1 - x0)) / (f_x1 - f_x0)
        
        print(f"x2 = {x2}")
        
        if abs(f(x2)) < 1e-6:
            print(f"Root found at x = {x2}")
            return x2
        
        if f_x0 * f(x2) < 0:
            x1 = x2  # The root lies between x0 and x2
        else:
            x0 = x2  # The root lies between x2 and x1

x0 = 1  
x1 = 3 

root = regula_falsi(x0, x1)
