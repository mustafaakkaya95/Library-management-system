class Library:
    def __init__(self, file_name): # The constructor method initializes the Library object.
        self.file_name = file_name
        self.file = open(self.file_name, "a+")  # It opens the library file in "a+" mode.

        self.history_file = open("history.txt", "a+")  # It also opens the history file with "a+" mode.

    def __del__(self):  # The destructor method closes the file.
        self.file.close()
        self.history_file.close()

    def list_books(self):  # Method to list all the books in the file.
        self.file.seek(0)  # Move cursor to the beginning of the file.
        books = self.file.read().splitlines()  # Read all lines from the file and split with stliplines() method into lines
        if not books:
            print("No books available.")
        else:
            print("*** List of Books ***")
            for book in books:
                book_info = book.split(',')  # Split each line by comma to get book details.
                print(f"Book: {book_info[0]}, Author: {book_info[1]}")
    def add_book(self):  # This method adds a new book to the library.
        title = input("Enter the title of the book: ")  # It prompts the user to enter the title of the book.
        author = input("Enter the author of the book: ")  # It prompts the user to enter the author of the book.
        release_year = input("Enter the release year of the book: ")  # It prompts the user to enter the first release year of the book.
        num_pages = input("Enter the number of pages of the book: ")  # It prompts the user to enter the number
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        self.history_file.write(f"Added book: {title}\n")  # It writes the book information to the library file and adds an entry to the history file.
        print("Book added successfully.")

    def remove_book(self):  # This method removes a book from the library.
        title = input("Enter the title of the book you want to remove: ")  # It prompts the user to enter the title of the book to be removed.
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        removed = False
        for book in books:
            if title.lower() != book.strip().split(',')[0].lower():
                new_books.append(book)
            else:
                removed = True
                self.history_file.write(f"Removed book: {title}\n")  # It adds an entry to the history file.
        if removed:
            self.file.seek(0)
            self.file.truncate()  # Clear the contents of the file
            self.file.writelines(new_books)  # It writes the updated list back to the file. 
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def view_history(self):  # This method displays the history of operations performed on the library.
        self.history_file.seek(0)
        history = self.history_file.read()  # It reads the history file and prints its contents.
        print("---- History ----")
        print(history)

    def search_book(self):  # This method searches for a book in the library by title.
        title = input("Enter the title of the book you want to search: ")  # It prompts the user to enter the title of the book to be searched.
        self.file.seek(0)
        books = self.file.readlines()
        found = False
        for book in books:
            book_info = book.strip().split(',')
            if title.lower() in book_info[0].lower():
                print(f"Book found: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Pages: {book_info[3]}")
                found = True
        if not found:
            print("Book not found.")

lib = Library("books.txt")  # Create an instance of the Library class with the specified file name.

while True:   # Display the menu and handle user input until the user chooses to quit.
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search Book")
    print("5) View History")
    print("Q) Quit")

    choice = input("Enter your choice: ").upper()  # Convert choice to uppercase.

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.search_book()
    elif choice == "5":
        lib.view_history()
    elif choice == "Q":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")