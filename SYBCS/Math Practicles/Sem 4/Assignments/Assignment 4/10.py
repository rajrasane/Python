import math
num = int(input("Enter a number: "))
sqrt = math.sqrt(num)
if sqrt == int(sqrt):
    if num > 100:
        print("The number is a perfect square and greater than 100.")
    else:
        print("The number is a perfect square but not greater than 100.")
else:
    print("The number is not a perfect square.")
