n1 = int(input("Enter 1st num:- "))
n2 = int(input("Enter 2nd num:- "))
n3 = int(input("Enter 3rd num:- "))

if(n1>n2 and n1>n3):
    print(f"{n1} is max")
elif(n2>n3):
    print(f"{n2} is max")
else:
    print(f"{n3} is max")