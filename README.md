## Bank Management System

This is a simple Bank Management System web application built using Python, Flask, and SQLite. It allows multiple users to register, log in, and perform basic banking operations such as depositing funds, withdrawing funds, and checking their balance. 

---

### Features
1. **User Authentication**:
   - Register as a new user.
   - Login using valid credentials.
   - Secure session management to maintain user state.

2. **Bank Operations**:
   - **Deposit**: Add funds to your account.
   - **Withdraw**: Remove funds (only if sufficient balance exists).
   - **Balance Check**: View the current balance in your account.

3. **Error Handling**:
   - Styled error page for invalid login credentials.
   - Prevent duplicate username registration.

4. **Multiple User Support**:
   - Each user operates with their own account balance and activities.

---

### File Structure
```
project/
├── templates/
│   ├── index.html          # Login page
│   ├── register.html       # Registration page
│   ├── BankOperations.html # Bank operations page
│   ├── result.html         # Page for showing deposit, withdrawal, or balance results
│   ├── invalid_login.html  # Page for invalid login credentials
├── app.py                  # Flask backend logic
├── bank.db                 # SQLite database (generated automatically)
```

---

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/bank-management-system.git
   cd bank-management-system
   ```

2. **Install dependencies**:
   Ensure Python is installed, then use pip to install Flask:
   ```bash
   pip install flask
   ```

3. **Initialize the database**:
   Run the application once to initialize the database:
   ```bash
   python app.py
   ```

4. **Run the application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

---

### Usage

1. Open the application in your browser at `http://127.0.0.1:5000`.
2. Register a new account or log in with existing credentials.
3. After logging in, perform banking operations:
   - Deposit funds.
   - Withdraw funds.
   - Check account balance.

---

### Screenshots

#### Login Page:
A simple login form for users to access their accounts.

#### Registration Page:
Allows new users to register with a unique username and password.

#### Bank Operations Page:
Provides options for deposit, withdrawal, and balance checks.

#### Error Page:
Displays a styled message for invalid login attempts or other errors.

---

### Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS

---

### Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature-name"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

### License

This project is licensed under the MIT License. See the `LICENSE` file for details. 

---

### Contact

For any inquiries or feedback, please contact:  
**Email**: [syedroshan1554@gmail.com](mailto:syedroshan1554@gmail.com)  
**LinkedIn**: [linkedin.com/in/syedroshan](https://linkedin.com/in/syedroshan)  

--- 

Feel free to modify this README as needed before adding it to your GitHub repository. Let me know if you'd like additional details or sections!
