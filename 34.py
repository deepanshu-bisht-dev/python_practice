# Bank Account Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount positive hona chahiye")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount positive hona chahiye")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance


# Tests
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
print(acc.get_balance())   

try:
    acc.withdraw(5000)
except ValueError as e:
    print(e)               