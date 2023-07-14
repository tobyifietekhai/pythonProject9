import tkinter as tk

class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")

        # Create account number entry
        self.account_number_label = tk.Label(root, text="Account Number:")
        self.account_number_label.pack()
        self.account_number_entry = tk.Entry(root)
        self.account_number_entry.pack()

        # Create account holder entry
        self.account_holder_label = tk.Label(root, text="Account Holder:")
        self.account_holder_label.pack()
        self.account_holder_entry = tk.Entry(root)
        self.account_holder_entry.pack()

        # Create initial deposit entry
        self.initial_deposit_label = tk.Label(root, text="Initial Deposit:")
        self.initial_deposit_label.pack()
        self.initial_deposit_entry = tk.Entry(root)
        self.initial_deposit_entry.pack()

        # Create create account button
        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

        # Create amount entry
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        # Create deposit button
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        # Create withdraw button
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        # Create balance label
        self.balance_label = tk.Label(root, text="Balance: ")
        self.balance_label.pack()

        self.bank = Bank()

    def create_account(self):
        account_number = int(self.account_number_entry.get())
        account_holder = self.account_holder_entry.get()
        initial_deposit = float(self.initial_deposit_entry.get())

        self.bank.create_account(account_number, account_holder, initial_deposit)

        self.account_number_entry.delete(0, tk.END)
        self.account_holder_entry.delete(0, tk.END)
        self.initial_deposit_entry.delete(0, tk.END)

    def deposit(self):
        account_number = int(self.account_number_entry.get())
        amount = float(self.amount_entry.get())

        account = self.bank.get_account(account_number)
        if account:
            account.deposit(amount)
            self.amount_entry.delete(0, tk.END)

    def withdraw(self):
        account_number = int(self.account_number_entry.get())
        amount = float(self.amount_entry.get())

        account = self.bank.get_account(account_number)
        if account:
            account.withdraw(amount)
            self.amount_entry.delete(0, tk.END)

    def update_balance_label(self, account_number):
        account = self.bank.get_account(account_number)
        if account:
            balance = account.get_balance()
            self.balance_label.config(text=f"Balance: {balance}")

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_holder, initial_deposit=0.0):
        account = Account(account_number, account_holder, initial_deposit)
        self.accounts.append(account)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

# Create the Tkinter application
root = tk.Tk()
app = BankApp(root)

# Start the Tkinter event loop
root.mainloop()
