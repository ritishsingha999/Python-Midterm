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
            print(f"Book '{self.title}' was not borrowed.")
    def view_book_info(self):
        availability_status = "Available" if self.availability else "Not Available"
        print(f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nAvailability: {availability_status}")
    def __repr__(self):
        return f"Book(ID={self.book_id}, title='{self.title}', author='{self.author}', available={self.availability})"
if __name__ == "__main__":
    Book(1, "1984", "George Orwell")
    Book(2, "To Kill a Mockingbird", "Harper Lee", availability=False)
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald")
    Book(4, "The Great Khallu", "F. Scott Fitzgerald")
    Book(5, "The Great Pallu", "F. Scott Fitzgerald")
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print("\nList of Books:")
                for book in Library.book_list:
                    book.view_book_info()
                    print("-")
            elif choice == 2:
                book_id = int(input("Enter the Book ID to borrow: "))
                book_found = False
                for book in Library.book_list:
                    if book.book_id == book_id:
                        book.borrow_book()
                        book_found = True
                        break
                if not book_found:
                    print("Book not found.")
            elif choice == 3:
                book_id = int(input("Enter the Book ID to return: "))
                book_found = False
                for book in Library.book_list:
                    if book.book_id == book_id:
                        book.return_book()
                        book_found = True
                        break
                if not book_found:
                    print("Book not found.")
            elif choice == 4:
                print("Exiting the Library system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
