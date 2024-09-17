# 1. Create a Book class with attributes for title, author, and availability.
class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        search_title = lambda book: book.title.lower() == title.lower()
        return list(filter(search_title, self.books))

    def search_by_author(self, author):
        search_author = lambda book: book.author.lower() == author.lower()
        return list(filter(search_author, self.books))

    def update_availability(self, title, available):
        update_book = lambda book: setattr(book, 'availability', available) if library.books.index(book) == title else None
        list(map(update_book, self.books))

# Create library class instance
library = Library()

# Create book class instances
book1 = Book('Think and Grow Rich', 'Napoleon Hill', 45)
book2 = Book('The Chimp Paradox', 'Steve Peters', 23)
book3 = Book('The Power of Habit', 'Charles Duhigg', 37)
book4 = Book('Rich Dad Poor Dad', 'Robert Kiyosaki', 14)

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)


print("Welcome to the Library Inventory Management system!")
print("====================================")
print("1. View current books")
print("2. Add a book")
print("3. Update book availability")
print("====================================")
choice = int(input("What would you like to do? (1/2/3): "))

if choice == 1:
    print("====================================")
    print("1. Title")
    print("2. Author")
    print("3. View All")
    print("====================================")
    search_choice = int(input("What would you like to search? (1/2/3): "))

    # Search for books by title
    if search_choice == 1:
        search_title = input("Title: ").lower()
        print("====================================")
        for book in library.search_by_title(search_title):
            print(f'- {book.title} found! Author: {book.author}, Availability: {book.availability}')
        print("====================================")

    # Search for books by Author
    elif search_choice == 2:
        search_author = input("Author: ").lower()
        print("====================================")
        for book in library.search_by_author(search_author):
            print(f'{book.author} has written {book.title}! {book.availability} left in stock!')
        print("====================================")

    # Search all books in library
    elif search_choice == 3:
        print("====================================")
        for book in library.books:
            print(f'Title: {book.title}, Author: {book.author}, Availability: {book.availability}')
        print("====================================")
    else:
        print("Invalid choice")

# Add book to library
elif choice == 2:
    # Capture inputs
    title = input('Title: ').capitalize()
    author = input('Author: ').capitalize()
    availability = input('Availability: ')

    # Create new book instance
    book = Book(title, author, availability)

    # Add instance to library
    library.add_book(book)

    print("Book added!")
    print("Here are all books in the store including yours:")

    # Print all books to show it's been added
    print("====================================")
    for book in library.books:
        print(f'Title: {book.title}, Author: {book.author}, Availability: {book.availability}')
    print("====================================")

# Update book availability
elif choice == 3:
    print("====================================")
    for book in library.books:
        print(f'{library.books.index(book)}. Title: {book.title} | Availability: {book.availability}')
    print("====================================")
    book_selector = int(input("What book would you like to update?: (1/2/3/4) "))

    # Confirm chosen book
    for book in library.books:
        if book_selector == library.books.index(book):
            print(f"You've chosen: {book.title} | Availability: {book.availability}")

    new_availability = int(input("How many copies are now available?: "))

    # Update availability in library
    library.update_availability(book_selector, new_availability)

    print("====================================")
    print("Book updated! Here is a list of all books in store:")
    for book in library.books:
        print(f'{library.books.index(book)}. Title: {book.title} | Availability: {book.availability}')
    print("====================================")

else:
    print("Invalid choice")