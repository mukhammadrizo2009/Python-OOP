### ✅ 5. **Product klassini yozing**


class Product:
    def __init__(self , name: str ,
                 price: float ,
                 category: str ,
                 in_stock: bool):
        
        self.name     = name
        self.price    = price
        self.category = category
        self.instockn = in_stock
        
product01 = Product('Olma' , 12_999.99 , 'Meva' , False)
product02 = Product('Iphone' , 14_000_000 , 'Elektronika' , True)

print(f"Mahsulot- {product01.name} | Narxi- {product01.price}")
print(f"Mahsulot- {product02.name} | Narxi- {product02.price}")