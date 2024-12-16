Bank Management System
This is a simple Bank Management System web application built using Python, Flask, and SQLite. It allows multiple users to register, log in, and perform basic banking operations such as depositing funds, withdrawing funds, and checking their balance.

Features
User Authentication:
 Register as a new user.
 Login using valid credentials.
 Secure session management to maintain user state.
Bank Operations:
 Deposit: Add funds to your account.
 Withdraw: Remove funds (only if sufficient balance exists).
 Balance Check: View the current balance in your account.
Multiple User Support:
 Each user operates with their own account balance and activities.
 
File Structure
project/
├── templates/
│   ├── index.html          # Login page
│   ├── register.html       # Registration page
│   ├── BankOperations.html # Bank operations page
│   ├── result.html         # Page for showing deposit, withdrawal, or balance results
│   ├── invalid_login.html  # Page for invalid login credentials
├── app.py                  # Flask backend logic
├── bank.db                 # SQLite database (generated automatically)
Installation and Setup


Usage
Open the application in your browser at http://127.0.0.1:5000.
Register a new account or log in with existing credentials.
After logging in, perform banking operations:
Deposit funds.
Withdraw funds.
Check account balance.

Technologies Used
Backend: Python, Flask
Database: SQLite
Frontend: HTML, CSS

