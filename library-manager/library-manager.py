import json
import os

data_file = 'library.txt'

# Encapsulation: The Book class encapsulates the details of a book.
class Book:
    def __init__(self, title, author, year, genre, read=False):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read = read

    # Abstraction: Provides a simple interface to get book information.
    def get_info(self):
        status = "Read" if self.read else "Unread"
        return f'{self.title} by {self.author} ({self.year}) - {self.genre} - {status}'

# Encapsulation: The Library class manages a collection of books.
class Library:
    def __init__(self):
        self.books = self.load_library()

    # Abstraction: Hides the complexity of loading the library from a file.
    def load_library(self):
        if os.path.exists(data_file):
            with open(data_file, 'r') as file:
                # Polymorphism: Using the Book class to create book objects.
                return [Book(**book) for book in json.load(file)]
        return []

    # Abstraction: Hides the complexity of saving the library to a file.
    def save_library(self):
        with open(data_file, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    # Encapsulation: Manages adding a book to the library.
    def add_book(self, book):
        self.books.append(book)
        self.save_library()
        print(f'Book "{book.title}" added successfully!')

    # Encapsulation: Manages removing a book from the library.
    def remove_book(self, title):
        initial_length = len(self.books)
        self.books = [book for book in self.books if book.title.lower() != title.lower()]
        if len(self.books) < initial_length:
            self.save_library()
            print(f'Book {title} removed successfully!')
        else:
            print(f'Book "{title}" not found.')

    # Encapsulation: Manages searching for books in the library.
    def search_books(self, search_by, search_term):
        results = [book for book in self.books if search_term.lower() in getattr(book, search_by).lower()]
        if results:
            for book in results:
                print(book.get_info())
        else:
            print("No matching books found.")

    # Encapsulation: Manages displaying all books in the library.
    def display_all_books(self):
        if self.books:
            for book in self.books:
                print(book.get_info())
        else:
            print("No books in the library.")

    # Encapsulation: Manages displaying statistics about the library.
    def display_statistics(self):
        total_books = len(self.books)
        read_books = len([book for book in self.books if book.read])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        print(f"Total Books: {total_books}")
        print(f"Percentage Read: {percentage_read:.2f}%")

def main():
    library = Library()

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            genre = input("Enter genre: ")
            read = input("Have you read this book? (yes/no): ").lower() == 'yes'
            book = Book(title, author, year, genre, read)
            library.add_book(book)
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice == '3':
            search_by = input("Search by title or author: ").lower()
            search_term = input(f"Enter the {search_by}: ").lower()
            library.search_books(search_by, search_term)
        elif choice == '4':
            library.display_all_books()
        elif choice == '5':
            library.display_statistics()
        elif choice == '6':
            print("Exiting the Library Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
