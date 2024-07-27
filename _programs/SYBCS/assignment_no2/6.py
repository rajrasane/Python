# find all positive prime nums less than given no. n

def posprime():
    num = int(input("Enter a number until which you want to check if number si prime or not :- "))
    for n in range(2,num+1):
        if(n>1):
            for i in range(2,(n//2)+1):
                if(n%i==0 and i!=n):
                    print(f"{n} is not prime.")
                    break
            else:
                print(f"{n} is a prime")

        else:
            print("Number is not prime")
posprime()