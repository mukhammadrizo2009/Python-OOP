### ✅ 3. **User klassini yozing**


class User:
    def __init__(self , username: str ,
                 email: str ,
                 is_active: bool):
        
        self.username = username
        self.email    = email
        self.isactive = is_active
        
user01 = User('sherkhon01' , 'sherkhon01gmail.com' , True)
user02 = User('oqayiq0000' , 'oqayiq.uzgmail.com' , False)


print(f"Username = {user01.username} | Gmail = {user01.email} | Active = {user01.isactive}")
print(f"Username = {user02.username} | Gmail = {user02.email} | Active = {user02.isactive}")