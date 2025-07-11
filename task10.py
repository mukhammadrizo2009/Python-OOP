### ✅ **Task 10 – BankAccount klassi bilan ishlash**

class BankAccount:
    def __init__(self , owner , amount ):
        self.owner   = owner
        self.balance = 0.0
        
    def deposit(self , amount , balance):
            if amount > 0 :
                amount += balance
            else:
                print("Mablag' noto'g'ri kiritildi!")
                
    def withdraw(self , balance , withdraw):
            if withdraw <= balance and withdraw > 0:
                balance -= withdraw
            else:
                print("Echmoqchi bo'lingan mablag' noto'g'ri kiritildi!")
        
user = BankAccount('Ali' , 67000)
user.deposit(amount=67000 , balance=0)
print(list(user.deposit()))