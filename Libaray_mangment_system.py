import os

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()
        self.number_of_books = len(self.books)

    def add_book(self, book_name):
        self.books.append(book_name)
        self.number_of_books = len(self.books)
        self.save_books()
        print(f'"{book_name}" added successfully.')

    def show_all_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nBooks in Library:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def get_number_of_books(self):
        return self.number_of_books

    def get_books(self):
        return self.books

    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(book + "\n")

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.books = [book.strip() for book in file.readlines()]


# ---------------- Main Program ----------------

library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Show All Books")
    print("2. Add Book")
    print("3. Get Number of Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.show_all_books()

    elif choice == "2":
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == "3":
        print("Total Books:", library.get_number_of_books())

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
