def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def binomial_coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

n = 5  
for i in range(n):
    row = ""
    for j in range(i+1):
        row += str(binomial_coeff(i, j)) + " "
    print(row.center(n*2))
