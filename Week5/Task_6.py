#Task_6:
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self,title):
        self.books.append(title)
        print(f'"{title}" added to library.')
    def remove_book(self,title):
        if title in self.books:
            self.books.remove(title)
            print(f'"{title}" removed from library.')
        else:
            print(f'"{title}" not found in library.')
    def display_books(self):
        if self.books:
            print("Books in library:")
            for i,book in enumerate(self.books,1):
                print(f"{i}. {book}")
        else:
            print("Library is empty.")
library=Library()
while True:
    print("Library Menu:\n1. Add Book\n2. Remove Book\n3. Display Books\n4. Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        title=input("Enter book title to add: ")
        library.add_book(title)
    elif choice=="2":
        title=input("Enter book title to remove: ")
        library.remove_book(title)
    elif choice=="3":
        library.display_books()
    elif choice=="4":
        print("Exiting library system...")
        break
    else:
        print("Invalid choice. Try again.")
