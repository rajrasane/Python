n = int(input("Enter a num to check if armstrong or not :- "))

b = str(n)

arm = 0

for i in b:
    c = int(i)
    arm = arm + c**3 

if(arm == n):
    print("Number is Armstrong Number")
else:
    print("Number is not armstong!")