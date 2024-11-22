import sqlite3

# Creating a database or connecing to one if it exisits
conn = sqlite3.connect("Item_7.db")

# Creating a cursor object
cursor = conn.cursor()


cursor.execute(
    """
CREATE TABLE IF NOT EXISTS meal_table2(
id INTEGER PRIMARY KEY AUTOINCREMENT,
meal TEXT NOT NULL,
price INTEGER NOT NULL,
size TEXT NOT NULL,
type TeXT NOT NULL
)
"""
)

#POPULATE OUR MAIN TABLE
cursor.execute(
    """
Insert INTO meal_table2(meal,price,size,type)
Values
    ("Rice",5000,"Family size","Local dish"),
    ("Pounded Yam",20000,"Couple size","Local dish"),
    ("Spag",2000,"Single size","Italian dish")
    """
)
conn.commit()

cursor.execute("SELECT * from meal_table2")

rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)

# Updating Records
cursor.execute(
    """
    UPDATE meal_table2
    SET price =3500
    where meal = "Rice"
    """
)
conn.commit()

cursor.execute("SELECT * from meal_table2")

rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)


# deleting records
cursor.execute(
    """
    Delete from meal_table2
    where meal = "Spag"
    """)
conn.commit()

cursor.execute("SELECT * from meal_table2")

rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row)
conn.close()

# AUTHETICATION WITH SQL
menu = """
1. Sign Up
2. Log In
3. Log Out
4. Purchase Item
5. Exit
"""


import hashlib
from getpass import getpass
def connect_to_db():
    conn = sqlite3.connect("user_db.db")
    cursor = conn.cursor()
    return cursor,conn
def set_up():
    cursor,_=connect_to_db()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    )
    """
    )

def create_user(first_name,last_name,username,password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor,conn = connect_to_db()
    try:
        cursor.execute(
            """
            INSERT INTO users(first_name,last_name,username,password)
            VALUES (?,?,?,?)
            """,(first_name,last_name,username,hashed_password)    
        )
        conn.commit
    except sqlite3.IntegrityError:
        print("The username already exists")
    else:
        print("Account created succesfully")
    finally:
        conn.close()
def sign_up():
    while True:
        first_name = input("Enter your first name: ").strip()
        last_name = input("Enter your last name: ").strip()
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password").strip()
        confirm_password = getpass("Confirm your password: ").strip()


        if not first_name:
            print("First name cannot be empty")
            continue
        if not username:
            print("Username cannot be empty")
            continue
        if not last_name:
            print("Last name cannot be blank")
            continue
        if not password:
            print("Password field is required")
            continue
        if not confirm_password:
            print("Confirm password cannot be blank")
        if password != confirm_password:
            print("Those two password don't match")
            continue
        break
    create_user(first_name,last_name,username,password)
session = {}
def create_session(username):
    print(f"user session action for {username}")
    session[username]=True
def log_in():
    while True:
        username = input("Enter your username: ").strip()
        password = getpass("Enter your password: ").strip()

        if not username:
            print("Username cannot be blank")
            continue
        if not password:
            print("Password cannot be empty")
            continue
        break
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor,conn = connect_to_db()

    cursor.execute(
        """
    SELECT * FROM users
    WHERE username = ? AND password = ?
        """,(username,hashed_password)
    )
    user=cursor.fetchone()
    if user:
        print("Login Successful")
        create_session(username)
    else:
        print("Incorrect details, wrong username or password")
        conn.close()
def log_out():
        username = input("Enter your username: ").strip()
        if username in session:
            del session[username]
        print("Logout successfully")
def is_logged_in(username):
        return session.get(username,False)
def purchase_item():
        username = input("Enter your username: ").strip()
        if is_logged_in(username):
            print("Item purchased")
        else:
            print("You need to login first")
def program():
    set_up()
    while True:

        print(menu)
        choice = input("Enter an option from 1 to 5: ")
        if choice =="5":
                print("Existing")
                break
        elif choice =="1":
                sign_up()
        elif choice =="2":
                log_in()
        elif choice =="3":
                log_out
        elif choice == "4":
                purchase_item()
        elif choice == "5":
                print("Existing")
                break
        else: 
             print("Invalid Selection")
      

# menu = "This is a test"
# print(menu)
program()








































































































































































































































































