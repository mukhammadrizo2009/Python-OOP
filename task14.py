### ✅ **Task 11 – Book klassi bilan ishlash**


class Student:
    def __init__(self , name: str , age: int):
        self.name = name
        self.age  = age
        
    def show_info(self):
        print(f"{self.name}, {self.age}- yoshda!")
        
def main():
    student1 = Student("Malika" , 17)
    student2 = Student("Nilufar" , 14)
    student3 = Student("Dilnura" , 15)
    student4 = Student("Gulzoda" , 16)
    student5 = Student("Munira" , 18)
    
    max([student1 , student2 , student3 , student4 , student5], key=lambda i:i.age).show_info()


if __name__ == "__main__":
    main()