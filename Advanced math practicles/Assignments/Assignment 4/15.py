balance = float(input("Enter the account balance: "))
account_type = input("Enter the account type (checking, savings, money market): ").lower()

if account_type == "checking":
    if balance >= 1000:
        print("This is a Premium Checking account.")
    else:
        print("This is a Standard Checking account.")
elif account_type == "savings":
    if balance >= 5000:
        print("This is a High-Interest Savings account.")
    else:
        print("This is a Standard Savings account.")
elif account_type == "money market":
    if balance >= 10000:
        print("This is a Premium Money Market account.")
    else:
        print("This is a Standard Money Market account.")
else:
    print("Invalid account type.")
