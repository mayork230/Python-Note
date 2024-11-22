import random
# Registered User and their data
Users = {"Ayomide":{"Pin":"0000","account_number":None,"balance":0},
         "Adeola":{"Pin":"0000","account_number":None,"balance":0},
         "Abdullah":{"Pin":"0000","account_number":None,"balance":0},
         "Shola":{"Pin":"0000","account_number":None,"balance":0},
         "Mayowa":{"Pin":"0000","account_number":None,"balance":0},
         "Timi":{"Pin":"0000","account_number":None,"balance":0}
}
# Generate Random Account Number
def Generate_Random_Account_Number():
    return random.randint(1000000000,9999999999)

# Check Balance of the User
def check_balance(user):
    y = Users[user]["balance"]
    print(f"Your account balance is: $ {y}")

#Deposit
def deposit(user,Amount):
    if Amount <0:
        print("Error!!! You cannot deposit a negative amount")
    else:
        Users[user]["balance"] = Users[user]["balance"]+Amount
        y = Users[user]["balance"]
        print(f"You have successfully deposited ${Amount}. New balance is $ {y}")

#Withdraw
def Withdraw(user,Amount):
    if Amount > Users[user]["balance"]:
        print(f"Insufficient balance")
    else:
        Users[user]["balance"]=Users[user]["balance"]-Amount
        y = Users[user]["balance"]
        print(f"{Amount} has successfully been withdrawn. New balance is $ {y}")
    
# deposit("Mayowa",100000)
# check_balance("Mayowa")
# Withdraw("Mayowa",100)

# Add New User
def add_new_user():
    name = input(f"Enter your name: ")
# Check if the user exist
    if name in Users:
        print("{name} already exist")
        return None
# Create a new user with random account number
    pin = input("Set your 4 digit pin: ")
    account_number = Generate_Random_Account_Number()

    Users[name]= {"Pin":pin,"account_number":account_number,"balance":0}
    print(f"You have successfully created account for {name} with account number {account_number}")
    return name

#Transaction Menu
def transaction_menu(name):
    account_number = Users[name]["account_number"]
    print(f"\nWelcome, {name}\nAccount Number: {account_number}")
            
    while True:
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                choice = input(f"Please Enter Your Choice: ")
                if choice =="1":
                    check_balance(name)
                elif choice =="2":
                    Amount = float(input(f"How much do you want to Deposit?: "))
                    deposit(name,Amount)
                elif choice=="3":
                    Amount = float(input(f"How much do you want to withdraw?: "))
                    Withdraw(name,Amount)
                elif choice =="4":
                    print(Users)
                    print(f"Thank you for using the bank app. \nHave a nice day")
                    break
                else:
                    print(f"Invalid Choice. Please enter a valid number")

# Bank Application
def bank_app():
    print("Welcome to Mayork Bank App!")
    print("Are you an existing or new customer?")
    print("1. Existing Customer")
    print("2. New User")
    
    user_type = input("Please enter 1 for existing customer or 2 for new user: ")      
    if user_type == "1":
        name = input("Enter your account name: ")
        if name not in Users:
            print("Name not registered.")
            return
    elif user_type == "2":
        name = add_new_user()
        if name is None:
            return
    else:
        print(f"Invalid input.")
        return
    # Proceed with PIN validation and transactions for both new and existing users
    entered_pin = input("Enter your PIN: ")

    if entered_pin != Users[name]["Pin"]:
            print("Wrong PIN. Try Again.")
    else:
         transaction_menu(name)
bank_app()