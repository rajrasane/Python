# to find the product n natural no. using while loop

n = int(input("Enter any number :- "))

prod = 1

i = 1

if(n>0):
    while(i<=n):
        prod = prod * i
        i = i+1
    print(f"Product of number until {n} is {prod}")