class Library:
    book_list = []
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    Library.entry_book(book1)
    Library.entry_book(book2)
    print(Library.book_list)
