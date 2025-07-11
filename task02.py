### ✅ 2. **Student klassini yozing**


class Student:
    def __init__(self , name: str ,
                 age: int ,
                 grade: int):
        
        self.name  = name
        self.age   = age
        self.grade = grade
        
pupil01 = Student('ALi' , 18 , 5)
pupil02 = Student('Vali' , 17 , 4)
pupil03 = Student('Mukhammadrizo' , 16 , 2)


print(f"{pupil01.name}-ismi | {pupil01.age}-yoshi | {pupil01.grade}-bahosi")
print(f"{pupil02.name}-ismi | {pupil02.age}-yoshi | {pupil02.grade}-bahosi")
print(f"{pupil03.name}-ismi | {pupil03.age}-yoshi | {pupil01.grade}-bahosi")