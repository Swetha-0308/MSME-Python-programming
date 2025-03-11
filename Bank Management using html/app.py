from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class BankAccount:
    def __init__(self, name, account_no, initial_balance):
        self.name = name
        self.account_no = account_no
        self.balance = initial_balance

    def show_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

# Create a sample bank account
account = BankAccount("John Doe", 123456, 1000)

@app.route('/')
def index():
    return render_template('index.html', balance=account.show_balance())

@app.route('/deposit', methods=['POST'])
def deposit():
    amount = float(request.form['amount'])
    account.deposit(amount)
    return redirect(url_for('index'))

@app.route('/withdraw', methods=['POST'])
def withdraw():
    amount = float(request.form['amount'])
    if not account.withdraw(amount):
        return render_template('result.html', message="Insufficient balance!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)