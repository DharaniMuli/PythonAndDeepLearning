from termcolor import colored, cprint


class availableBooks:                                                                  # Class to check availability of books
    booklist = {
        "Book1": 1,
        "Book2": 2,
        "Book3": 4,
        "Book4":5
    }
# This Dictionary is default storage of books with no changes when books issued are returned,
# This helps us to check whether books has been really issued or not
    bookStore = {
        "Book1": 1,
        "Book2": 2,
        "Book3": 4,
        "Book4": 5
    }
    def bookAvailability(self):
        count=0
        print("""You choose to list all available books and Here is the list:""")
        print("""S.No | Book_Name | No._Of_Books""")
        print("""--------------------------""")
        for item in self.booklist:
            count = count+1
            print(count,"\t \t", item,"\t \t",self.booklist[item])
class checkOutBook(availableBooks):                                                    # Class for checking out books which inherits
    def requestBook(self):                                                             # properties of "availableBooks" Class(Child Class)
        bookchoice=input("Please enter name of the book:")
        if availableBooks.booklist[bookchoice] == 0:
            color4 = colored("Sorry we don't have the book you requested", 'red')
            print(color4)
        else:
            booksCount = availableBooks.booklist[bookchoice] - 1
            availableBooks.booklist.update({bookchoice: booksCount})
            # colored is used to display the text in the required color
            color1 = colored("You book has been issued successfully", 'green')
            print(color1)
class BookReturn(availableBooks):                                                                       # Class Book Returns
    def returnBook(self):
        bookchoice = input("Please enter name of the book that you wanted to return:")
        booksCount = availableBooks.booklist[bookchoice] + 1
        if availableBooks.bookStore[bookchoice] >= booksCount:
            availableBooks.booklist.update({bookchoice: booksCount})                        # Accessing and Updating the other class variables
            print("You choose to return ", bookchoice, "and it is successfull")
        else:
            color3= colored("Sorry we haven't issued any book with this name",'red')
            print(color3)

if __name__ == '__main__':
    decision = 'y'
while decision.lower()=='y':
    print("----Welcome Library Management System---")
    print("""
             1. List all available books
             2. Request for Book 
             3. Return a Book
          """)
    choice = int(input("Please Enter your choice:"))
    availableBooksObj = availableBooks()
    checkOutBookObj= checkOutBook()
    BookReturnObj= BookReturn()
    if choice == 1:
        availableBooksObj.bookAvailability()                                       # Accessing child class method()
    elif choice == 2:
        checkOutBookObj.requestBook()
    elif choice == 3:
        BookReturnObj.returnBook()
    decision = input("Do you want to continue(y/n):")
