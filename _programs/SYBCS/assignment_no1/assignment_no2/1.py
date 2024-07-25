# find 10 terms of the sequence of function f(x) =  x**2 +x

def f(x):
    return (x**2) + x

for i in range(1,11):
    print(f"Term {i} : {f(i)}")