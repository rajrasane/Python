import math

def rpn(n, limit):
    result = []
    for i in range(1, limit): 
        if math.gcd(i, n) == 1:  
            result.append(i)
    return result

numbers = rpn(111, 150)
print("Numbers relatively prime to 111 under 150:")
print(numbers)
