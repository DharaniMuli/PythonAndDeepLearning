class availableBooks:                                                                  # Class to check availability of books
    booklist = {
        "Book1": 1, "Book2": 2, "Book3": 4
    }
    def bookAvailability(self):
        count=0
        print("""
        You choose to list all available books and Here is the list: 
        S.No  Book_Name  BookCount
        --------------------------""")

        for item in self.booklist:
            count = count+1
            print(count, ".", item,self.booklist[item])
class checkOutBook(availableBooks):                                                    # Class for checking out books which inherits
    def requestBook(self):                                                             # properties of "availableBooks" Class(Child Class)
        bookchoice=input("Please enter name of the book:")
        booksCount = availableBooks.booklist[bookchoice]-1
        availableBooks.booklist.update({bookchoice:booksCount})
        print("You book has been issued sucessfully")
class BookReturn:                                                                       # Class Book Returns
    def returnBook(self):
        bookchoice = input("Please enter name of the book that you wanted to return:")
        booksCount = availableBooks.booklist[bookchoice] + 1
        availableBooks.booklist.update({bookchoice: booksCount})                        # Accessing and Updating the other class variables
        print("You choose to return ", bookchoice, "and it is sucessfull")


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
