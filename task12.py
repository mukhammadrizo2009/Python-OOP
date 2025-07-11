class BankAccount:
    def __init__(self , owner: str ) -> None:
        self.owner   = owner
        self.balance = 0.0
        
    def deposit(self , amount: float) -> None:
        if amount > 0:
            self.balance += amount
            
    def withdraw(self , amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
    
    def show_balance(self)-> None:
        print(f"{self.owner} Balanse: ${self.balance:,.2f}")
        
        
account = BankAccount("Azizbek")
account.deposit(10.0)
account.show_balance()