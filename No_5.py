class Library:
    book_list = []
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability
        Library.entry_book(self) 
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"Book '{self.title}' borrowed successfully.")
        else:
            print(f"Book '{self.title}' is not available for borrowing.")
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"Book '{self.title}' returned successfully.")
        else:
            print(f"Book '{self.title}' is already available.")
    def __repr__(self):
        return f"Book(ID={self.book_id}, title='{self.title}', author='{self.author}', available={self.availability})"
if __name__ == "__main__":
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", availability=False)
    print(Library.book_list)
    book1.borrow_book()
    book2.borrow_book()
    book1.return_book()
    book2.return_book()
    print(Library.book_list)
