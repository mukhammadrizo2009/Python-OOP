### ✅ 1. **Car klassini yozing**


class Car:
    def __init__(self , brand: str ,
                 model: str ,
                 year: int):
        
        self.brand  = brand
        self.model  = model
        self.year   = year
        
car = Car('BMW' , 'M5 F90 Competion' , 2025)


print(f"{car.brand} | {car.model} | {car.year}")
