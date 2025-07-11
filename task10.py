### ✅ **Task 10 – BankAccount klassi bilan ishlash**


class BankAccount:
    def __init__(self, owner, amount):
        self.owner = owner
        self.balance = amount  

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

user = BankAccount('Ali', 67000)

user.deposit(amount=67000)

print(user.balance) 
