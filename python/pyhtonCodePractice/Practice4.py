# Create a:

# BankAccount

# with:

# deposit(amount)
# withdraw(amount)
# check_balance()

# Requirements:

# Deposit must be greater than 0.
# Withdrawal must be greater than 0.
# Don't allow withdrawal greater than the balance.
# Raise appropriate exceptions for invalid operations.

# Example:

# account = BankAccount("Om", 5000)

# account.deposit(1000)
# account.withdraw(2000)

# account.check_balance()

# Expected:

# Balance: 4000

class BankAccount:
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Om", 5000)

account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())
