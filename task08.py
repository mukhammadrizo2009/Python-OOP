### ✅ **Task 8 – Product klassi bilan ishlash**


class Product:
    def __init__(self , name: str ,
                 price: int ,
                 category: str ,
                 in_stock: bool):
        
        self.name     = name
        self.price    = price
        self.category = category
        self.instock  = in_stock
        
        def check_stock():
            return None
        
product01 = Product('Olma' , 12_999.99 , 'Meva' , True)
product02 = Product('Iphone' , 14_000_000 , 'Elektronika' , False)

print(f"{product01.name} omborda mavjud ✅")
print(f"{product02.name} hozircha tugagan ❌")