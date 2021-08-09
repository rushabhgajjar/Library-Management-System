"""
# Library management system
Create a library class
Display books
lend books - (who owns the book if not present)
add books
return books

HarryLibrary = Library(listofbooks, library_name)
dictionary(books) = nameofperson
create a main function and run an infinite while loop asking users fo their input
"""


class Library:
    def __init__(self, dic_of_books, library_name):
        self.dic_of_books = dic_of_books
        self.library_name = library_name
        self.assigned_books = {}

    def display_books(self):
        for book, count in self.dic_of_books.items():
            print()
            print(book, ",   Qty - ", count)
        print()

    def lend_book(self):
        while True:
            name = input("\nEnter your name: ").upper()
            user_book = input("Enter name of book: ").upper()
            for book, count in self.dic_of_books.items():
                if book == user_book and count == 0:
                    print("\nThis book is not available currently as all copies have been assigned.")
                    print(f"\nBook currently assigned to below user/users:\n{self.assigned_books[user_book]}\n")
                    break
                elif user_book in self.assigned_books.keys() and count != 0:
                    self.assigned_books[user_book].append(name)
                    self.dic_of_books[user_book] -= 1
                    print(f"\nLender-Book database updated(app).\n\n'{user_book}' lend successfully to {name}.\n")
                    break
                elif user_book not in self.assigned_books.keys() and user_book in self.dic_of_books.keys():
                    self.assigned_books[user_book] = [name]
                    self.dic_of_books[user_book] -= 1
                    print(f"\nLender-Book database updated.\n\n'{user_book}' lend successfully to {name}.\n")
                    break
            else:
                print("\nThis Book not available with us. Please find somewhere else.\n")
            ask = input("Do you want any other book? (y/n): ").upper()
            if ask[0] == "N":
                print("\nThank you!\n")
                break

    def add_book(self):
        while True:
            add_book = input("\nEnter book name to add: ").upper()
            count = int(input("Enter book count: "))
            if count < 1:
                print("\nBook quantity cannot be zero.")
            else:
                self.dic_of_books[add_book] = count
                print("\nBook has been added to the book list.")
            ask = input("\nDo you want to add another book(y/n)?: ").upper()
            if ask[0] == "N":
                print()
                break

    def return_book(self):
        name = input("\nEnter your name: ").upper()
        return_book = input("\nEnter the name of the book you wish to return:\n").upper()
        for i in self.dic_of_books:
            if i == return_book:
                self.dic_of_books[return_book] += 1
        for book in self.assigned_books.keys():
            if book == return_book:
                for person_name in self.assigned_books[book]:
                    if person_name == name:
                        self.assigned_books[book].remove(person_name)
                        print(f"\nThank you for returning '{return_book}',{person_name}.\n")
                        break
            break
        else:
            print("\nThis book does not belongs to our library.\n")


if __name__ == "__main__":
    Rush_Library = Library({}, "Rushabh's Library")
    print(f"\nWelcome to {Rush_Library.library_name} Library Management System!\n")
    while True:
        user_input = int(input("What do you want to do:\n1.Display books\n2.Lend a book\n3.Add a book\n4.Return a "
                               "book\n5.Exit\nEnter number as per your choice.\n"))
        if user_input == 1:
            Rush_Library.display_books()
        elif user_input == 2:
            Rush_Library.lend_book()
        elif user_input == 3:
            Rush_Library.add_book()
        elif user_input == 4:
            Rush_Library.return_book()
        elif user_input == 5:
            break
        else:
            print("Invalid input!\n")
