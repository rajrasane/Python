gpa = float(input("Enter your GPA: "))
income = float(input("Enter your family income: "))
if gpa >= 3.5:
    if income <= 50000:
        print("You are eligible for the scholarship.")
    else:
        print("Your family income is too high for the scholarship.")
else:
    print("Your GPA is too low for the scholarship.")
