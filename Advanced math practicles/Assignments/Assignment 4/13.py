income = float(input("Enter your income: "))
status = input("Enter your filing status (single, married, head of household): ").lower()

if status == "single":
    if income <= 9875:
        print("Tax bracket: 10%")
    elif income <= 40125:
        print("Tax bracket: 12%")
    else:
        print("Tax bracket: 22%")
elif status == "married":
    if income <= 19750:
        print("Tax bracket: 10%")
    elif income <= 80250:
        print("Tax bracket: 12%")
    else:
        print("Tax bracket: 22%")
elif status == "head of household":
    if income <= 14100:
        print("Tax bracket: 10%")
    elif income <= 53700:
        print("Tax bracket: 12%")
    else:
        print("Tax bracket: 22%")
else:
    print("Invalid filing status.")
