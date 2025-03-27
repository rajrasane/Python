import math

def nr(f,g,x0,e,n):
    for step in range(1,n+1):
        if(g(x0)==0):
            return "Divide by zero error"
        
        x1 = x0 - f(x0) / g(x0)

        print(f"Iteration {step} : x1={x1:.4f} , f(x1)={f(x1):.4f}")

        if abs(f(x1)) < e:
            return f"Required Root :- {x1:.4f}"
        
        x0 = x1
    
    return "Not Convergent!"

def f(x):
    return 3*x - math.cos(x) - 1

def g(x):
    return 3 + math.sin(x)

print(nr(f,g,3,0.00001,20))