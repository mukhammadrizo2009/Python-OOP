### ✅ **Task 6 – Student klassi bilan ishlash**


class Student:
    def __init__(self , name: str ,
                 age: int ,
                 grade: int):
        
        self.name  = name
        self.age   = age
        self.grade = grade
        
    def info(self)-> str:
            return None
        
pupil = Student('Ali' , 15 , 9)


print(f"{pupil.name} | {pupil.age}-yoshda | {pupil.grade}-sinf o'quvchisi")