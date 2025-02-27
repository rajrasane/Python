credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your income: "))
if credit_score >= 700:
    if income >= 30000:
        print("You are eligible for a credit card.")
    else:
        print("Your income is too low for a credit card.")
else:
    print("Your credit score is too low for a credit card.")
