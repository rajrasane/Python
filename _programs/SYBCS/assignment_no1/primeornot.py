def primeornot():
    n = int(input("Enter a number you want to check if it's prime or not :- "))
    if(n>1):
        for i in range(2,(n//2)+1):
            if(n%i==0 and i!=n):
                print("Number is not prime.")
                break
        else:
            print("Number is a prime")

    else:
        print("Number is not prime")   
primeornot()