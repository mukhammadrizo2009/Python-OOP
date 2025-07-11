### ✅ **Task 13 – Library kitoblari ro‘yxati**


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False  
    
    def mark_as_read(self):
        self.is_read = True
    
    def status(self):
        return "O'qilgan" if self.is_read else "O'qilmagan"


book1 = Book("Yashamoq", "Yu Hua")
book2 = Book("MEN-bas qil ey nafs!", "Fotih Duman")
book3 = Book("Halqa", "Akrom Malik")
book4 = Book("Jinoyat va Jazo", "Dostayevskiy")


book1.mark_as_read()
book3.mark_as_read()


books = [book1, book2, book3, book4]

for book in books:
    print(f"Kitob: '{book.title}' muallif: {book.author} — Holat: {book.status()}")
