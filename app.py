from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'

# Initialize the database
def init_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check credentials in the database
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['username'] = username
            return redirect(url_for('bank_operations'))
        else:
            return render_template('invalid_login.html', message="Invalid credentials. Please try again or register if you're a new user.")
    return render_template('index.html')

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        try:
            cursor.execute('INSERT INTO users (username, password, balance) VALUES (?, ?, ?)', (username, password, 0))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return render_template('error.html', message="Username already exists. Please choose a different username.")
    return render_template('register.html')

# Bank Operations Page
@app.route('/bank_operations', methods=['GET'])
def bank_operations():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('BankOperations.html', username=session['username'])

# Withdraw Route
@app.route('/withdraw', methods=['POST'])
def withdraw():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    amount = float(request.form['withdraw_amount'])

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        new_balance = balance - amount
        cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
        conn.commit()
        conn.close()
        return render_template('result.html', message=f"Withdrawal successful! Your new balance is ₹{new_balance:.2f}.")
    else:
        conn.close()
        return render_template('result.html', message="Insufficient funds. Please try again.")

# Deposit Route
@app.route('/deposit', methods=['POST'])
def deposit():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    amount = float(request.form['deposit_amount'])

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = cursor.fetchone()[0]

    new_balance = balance + amount
    cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
    conn.commit()
    conn.close()
    return render_template('result.html', message=f"Deposit successful! Your new balance is ₹{new_balance:.2f}.")

# Balance Route
@app.route('/balance', methods=['GET'])
def balance():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']

    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = cursor.fetchone()[0]
    conn.close()

    return render_template('result.html', message=f"Your current balance is: ₹{balance:.2f}.")

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
