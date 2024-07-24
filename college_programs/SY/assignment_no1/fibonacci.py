n = int(input("Enter until where do you want to have fibonacci series with :- "))

n1 = 0
n2 = 1
fibo = 0

for i in range(1,n+1):
    print(fibo)
    n1 = n2
    n2 = fibo
    fibo = n1 + n2