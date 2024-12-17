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
    def __repr__(self):
        return f"Book(ID={self.book_id}, title='{self.title}', author='{self.author}', available={self.availability})"
if __name__ == "__main__":
    book1 = Book(1, "1984", "George Orwell")
    book2 = Book(2, "To Kill a Mockingbird", "Harper Lee", availability=False)
    Library.entry_book(book1)
    Library.entry_book(book2)
    print(Library.book_list)
