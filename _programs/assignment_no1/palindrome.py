n = int(input("Enter a number which you want to check if it's palindrome or not :- "))

a = str(n)[::-1]
revi = int(a)

if(revi==n):
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")