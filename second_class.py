# import random
# # Generate a random account number
# def generate_random_account_number():
#     return random.randint(10000000000,99999999999)
# #function to setup a new account
# # def set_up_account():
    
# #     print(f"\nAccount Created Successfully\nAccount Name: {name}\nAccount Number: {account_number}")
# #     return name, account_number,pin

# # Initialize balance 
# balance = 0.00
# def check_balance():
#     print(f"Your Account Balance is: ${balance:.2f}")
# def deposit(Amount):
#     global balance
#     if Amount < 0:
#         print(f"Error!! You cannot deposit a negetive amount")
#     elif Amount > 0:
#         balance = balance + Amount
#         print(f"${Amount:.2f} has been deposited to your account. New Balance: ${balance:.2f}")
# def withdraw(Amount):
#     global balance
#     if Amount > balance:
#         print(f"Insufficiend Funds")
#     elif Amount <= balance:
#         balance = balance-Amount
#         print(f"${Amount:.2f} has been withdrawn from your account. New Balance: ${balance:.2f}")
# def bank_app():
#     name = input("Enter your account name: ")
#     pin = "0000"
#     account_number = generate_random_account_number()
    
#     entered_pin = input("Enter your PIN to access your account: ")
#     if entered_pin != pin:
#         print(f"Wrong Password: Input the right Password")
#     while True:
#             print(f"\n Welcome , {name} \nAccount Number: {account_number}")
#             print("1. Check Balance")
#             print("2. Deposit")
#             print("3. Withdraw")
#             print("4. Exist")

#             choice = input("Please enter your preferred number: ")
#             if choice == "1":
#                 check_balance()
#             elif choice == "2":
#                 Amount = float(input("How much do you want to deposit?: $"))
#                 deposit(Amount)
#             elif choice == "3":
#                 Amount = float(input("How much do you want to Withdraw?: $"))
#                 withdraw(Amount)
#             elif choice == "4":
#                 print("Thank you for using the bank app. Goodbye!")
#                 break
#             else: 
#                 print("Invalid Choice. Input a correct number")
            
# # set_up_account()
# bank_app()

import random

# Registered users and their data
users = {
    "Ayomide": {"pin": "0000", "account_number": None, "balance": 0.00},
    "Adeola": {"pin": "0000", "account_number": None, "balance": 0.00},
    "Abdullahi": {"pin": "0000", "account_number": None, "balance": 0.00},
    "Shola": {"pin": "0000", "account_number": None, "balance": 0.00},
    "Mayowa": {"pin": "0000", "account_number": None, "balance": 0.00},
    "Timi": {"pin": "0000", "account_number": None, "balance": 0.00}
}


# Generate a random account number
def generate_random_account_number():
    return random.randint(10000000000,99999999999)

# Check balance
def check_balance(user):
    print(f"Your Account Balance is: ${users[user]['balance']:.2f}")

# Deposit
def deposit(user, Amount):
    if Amount < 0:
        print("Error!! You cannot deposit a negative amount")
    else:
        users[user]['balance'] += Amount
        print(f"${Amount:.2f} has been deposited. New Balance: ${users[user]['balance']:.2f}")

# Withdraw
def withdraw(user, Amount):
    if Amount > users[user]['balance']:
        print("Insufficient Funds")
    else:
        users[user]['balance'] -= Amount
        print(f"${Amount:.2f} has been withdrawn. New Balance: ${users[user]['balance']:.2f}")

# Bank application
def bank_app():
    name = input("Enter your account name: ")
    
    if name in users:
        if users[name]['account_number'] is None:
            users[name]['account_number'] = generate_random_account_number()
            print(f"Account successfully created for {name}")
    
        entered_pin = input("Enter your PIN: ")
        if entered_pin != users[name]['pin']:
            print("Wrong PIN. Try again.")
        else:
            account_number = users[name]['account_number']
            print(f"\nWelcome, {name}\nAccount Number: {account_number}")
            
            while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")
                
                choice = input("Please enter your choice: ")
                if choice == "1":
                    check_balance(name)
                elif choice == "2":
                    Amount = float(input("How much do you want to deposit?: $"))
                    deposit(name, Amount)
                elif choice == "3":
                    Amount = float(input("How much do you want to withdraw?: $"))
                    withdraw(name, Amount)
                elif choice == "4":
                    print("Thank you for using the bank app. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a valid number.")
    else:
        print("Name not registered.")

bank_app()
