age = int(input("Enter your age: "))
weight = int(input("Enter your weight (in kg): "))
if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You need to weigh at least 50 kg to donate blood.")
else:
    print("You need to be at least 18 years old to donate blood.")
