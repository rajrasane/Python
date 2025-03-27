import math

def Tr(f , a, b, n):
    h = float(b - a) / n
    I = f(a) + f(b) 

    for i in range(1, n):
        I += 2 * f(a + i * h)  
    
    I = (h / 2) * I  
    return I

def f(x):
    return math.sin(x)  

print(f"Approximate integral: {Tr(f, 0, math.pi, 4)}")