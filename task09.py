### ✅ **Task 9 – User klassi bilan ishlash**


class User:
    def __init__(self , username: str ,
                 email: str ,
                 is_active: bool):
        
        self.username = username
        self.email    = email
        self.isactive = is_active
        
    def activate(self):
        self.is_active = True
        print(f"{self.username} faol emas.")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} faol.")
        
user01 = User('sherkhon01' , 'sherkhon01gmail.com' , False)
user02 = User('oqayiq0000' , 'oqayiq.uzgmail.com' , True)

user01.activate()
user02.deactivate()