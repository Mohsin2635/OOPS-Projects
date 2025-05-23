class Book:
    total_books = 0
    def __init__(self):
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"Total books are : {cls.total_books}📗")

book1 = Book()
book2 = Book()
book3 = Book()