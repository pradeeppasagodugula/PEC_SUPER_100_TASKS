class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        else:
            print("Book is already borrowed.")
            return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        else:
            print("Cannot return a book that is not borrowed.")
            return False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}' successfully.")
        else:
            print(f"{self.name} couldn't borrow '{book.title}'.")

    def return_book(self, book):
        if book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}' successfully.")
        else:
            print(f"{self.name} couldn't return '{book.title}'.")

    def __str__(self):
        borrowed_books_info = ", ".join([book.title for book in self.borrowed_books])
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_books_info}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' by {author} added to the library.")

    def add_member(self):
        name = input("Enter the name of the member: ")
        member_id = int(input("Enter the member ID: "))
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' with ID {member_id} added to the library.")

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print(book)

    def display_members(self):
        print("Library Members:")
        for member in self.members:
            print(member)

    def borrow_book(self):
        member_id = int(input("Enter the member ID: "))
        book_title = input("Enter the title of the book to borrow: ")

        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if member and book:
            member.borrow_book(book)
        else:
            print("Member or book not found.")

    def return_book(self):
        member_id = int(input("Enter the member ID: "))
        book_title = input("Enter the title of the book to return: ")

        member = next((m for m in self.members if m.member_id == member_id), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if member and book:
            member.return_book(book)
        else:
            print("Member or book not found.")

library = Library()

while True:
    print("\nOptions:")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Members")
    print("0. Exit")

    choice = input("Enter your choice (0-6): ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.add_member()
    elif choice == "3":
        library.borrow_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        library.display_members()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please enter a number between 0 and 6.")
