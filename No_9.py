class Library:
    book_list = []
    @classmethod
    def entry_book(cls, book):
        cls.book_list.append(book)
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability
        Library.entry_book(self)  
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"Book '{self.__title}' borrowed successfully.")
        else:
            print(f"Error: Book '{self.__title}' is already borrowed.")
    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"Book '{self.__title}' returned successfully.")
        else:
            print(f"Error: Book '{self.__title}' was not borrowed.")
    def view_book_info(self):
        availability_status = "Available" if self.__availability else "Not Available"
        print(f"Book ID: {self.__book_id}\nTitle: {self.__title}\nAuthor: {self.__author}\nAvailability: {availability_status}")
    def __repr__(self):
        return f"Book(ID={self.__book_id}, title='{self.__title}', author='{self.__author}', available={self.__availability})"
    @property
    def book_id(self):
        return self.__book_id
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def availability(self):
        return self.__availability
if __name__ == "__main__":
    Book(1, "1984", "George Orwell")
    Book(2, "To Kill a Mockingbird", "Harper Lee", availability=False)
    Book(3, "The Great Gatsby", "F. Scott Fitzgerald")
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
                try:
                    book_id = int(input("Enter the Book ID to borrow: "))
                    book_found = False
                    for book in Library.book_list:
                        if book.book_id == book_id:
                            book.borrow_book()
                            book_found = True
                            break
                    if not book_found:
                        print("Error: Invalid Book ID. Book not found.")
                except ValueError:
                    print("Error: Invalid input. Please enter a valid Book ID.")
            elif choice == 3:
                try:
                    book_id = int(input("Enter the Book ID to return: "))
                    book_found = False
                    for book in Library.book_list:
                        if book.book_id == book_id:
                            book.return_book()
                            book_found = True
                            break
                    if not book_found:
                        print("Error: Invalid Book ID. Book not found.")
                except ValueError:
                    print("Error: Invalid input. Please enter a valid Book ID.")
            elif choice == 4:
                print("Exiting the Library system. Goodbye!")
                break
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
