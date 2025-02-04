a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
