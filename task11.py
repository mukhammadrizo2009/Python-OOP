class Book:
    def __init__(self, title: str , author: str , is_read: bool):
        self.title   = title
        self.author  = author
        self.is_read = is_read
        
    def status(self) -> None:
        if self.is_read:
            print(f"{self.title} kitobi o'qilgan")
        
        else:
            print(f"{self.title} kitobi o'qilmagan")
            
    def mark_as_read(self):
        self.is_read = True
        
        
book = Book("MEN" , "Fotih Duman")
book.mark_as_read()
book.status()