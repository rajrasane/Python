def gcd(n1,n2):
    i = 0
    if(n1<=n2):
        n = n1
    else:
        n = n2

    for i in range(1,n+1):
        if(n1%i==0 and n2%i==0):
            div = i
            if(i>div):
                div=i
    print(div)

gcd(25,50)