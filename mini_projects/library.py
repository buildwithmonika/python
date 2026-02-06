class Library:
    num_books = 0

    def __init__(self):
        print("Library initialized.")
        self.books = []

    @classmethod
    def handle_books_count(cls):
        cls.num_books += 1

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")
        self.handle_books_count()

    def show_books(self):
        print(self.books)
        if len(self.books) == 0:
            print("No books in the library.")
            return 
        
        for i, book in enumerate(self.books):
            print(f"Book {i}: {book}")

    @classmethod
    def total_books(cls):
        return cls.num_books
    

if __name__ == "__main__":
    library = Library()
    while True:
        option = input("WELCOME TO THE LIBRARY. Select operation to perform (1. Add Book \n 2. Show books list \n 3. Total books \n 4. Exit): ").strip()
        if option == '1':
            book = input("Enter book name to add: ")
            library.add_book(book)
        elif option == '2':
            library.show_books()
        elif option == '3':
            print("Total books in library:", Library.total_books())
        elif option == '4':
            print("Exiting the library system. This will reset the books list. Goodbye!")
            break