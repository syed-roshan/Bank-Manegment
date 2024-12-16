import sqlite3

# Database setup
def setup_database():
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()
    
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )''')

    connection.commit()
    connection.close()

# Register a new user
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")
    finally:
        connection.close()

# Login user
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    connection.close()

    if user:
        print(f"Welcome, {username}!")
        return user
    else:
        print("Invalid username or password.")
        return None

# Withdraw money
def withdraw(user):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute("SELECT balance FROM users WHERE id = ?", (user[0],))
    balance = cursor.fetchone()[0]

    if amount > balance:
        print("Insufficient balance.")
    else:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, user[0]))
        connection.commit()
        print(f"Withdrawal successful! New balance: {balance - amount}")

    connection.close()

# Deposit money
def deposit(user):
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, user[0]))
    connection.commit()

    cursor.execute("SELECT balance FROM users WHERE id = ?", (user[0],))
    balance = cursor.fetchone()[0]

    print(f"Deposit successful! New balance: {balance}")

    connection.close()

# Check balance
def check_balance(user):
    connection = sqlite3.connect("bank.db")
    cursor = connection.cursor()

    cursor.execute("SELECT balance FROM users WHERE id = ?", (user[0],))
    balance = cursor.fetchone()[0]

    print(f"Your current balance is: {balance}")

    connection.close()

# Close account
def close_account(user):
    confirmation = input("Are you sure you want to close your account? (yes/no): ").lower()
    if confirmation == "yes":
        connection = sqlite3.connect("bank.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user[0],))
        connection.commit()

        print("Your account has been closed.")

        connection.close()
        return True
    else:
        print("Account closure canceled.")
        return False

# Main menu
def main_menu(user):
    while True:
        print("\n1. Withdraw\n2. Deposit\n3. Check Balance\n4. Close Account\n5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            withdraw(user)
        elif choice == "2":
            deposit(user)
        elif choice == "3":
            check_balance(user)
        elif choice == "4":
            if close_account(user):
                break
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main application loop
def main():
    setup_database()

    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = login()
            if user:
                main_menu(user)
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
