# Write a python program to create Fibonacci series up to n using lambda

n = int(input("Enter a number till you want fibonacci series :- "))

def fibonacci_for_loop(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci_for_loop(n)