from termcolor import colored, cprint
class ManageLibrary():

    booklist = {
        'Book1':{
            'id': 1,
            'count': 4,
        },
        'Book2': {
            'id': 2,
            'count': 5,
        },
        'Book3': {
            'id': 3,
            'count': 2,
        },
        'Book4': {
            'id': 4,
            'count': 8,
        }

    }

    bookStore = {
        'Book1': {
            'id': 1,
            'count': 4,
        },
        'Book2': {
            'id': 2,
            'count': 5,
        },
        'Book3': {
            'id': 3,
            'count': 2,
        },
        'Book4': {
            'id': 4,
            'count': 8,
        }

    }

    # Method to check availability of books
    def availableBooks(self):

        print("""You choose to list all available books and Here is the list:""")
        print("""BID | Book_Name | No._Of_Books""")
        print("""---------------------------------""")
        for item in self.booklist:
            print(self.booklist[item]['id'],"\t \t",item,"\t \t",self.booklist[item]['count'])

    # Method for checking out books
    def checkOutBook(self):
        studentOrFaculty = input("Are you Student or Faculty:")
        username = input("Please enter your name:")
        bookchoice = input("Please enter name of the book:")
        validatioCheck = Members(studentOrFaculty,username)
        if validatioCheck.memberValidation() == True:
            if self.booklist[bookchoice]['count'] == 0:
                color4 = colored("Sorry we don't have the book you requested", 'red')
                print(color4)

            else:
                booksCount = self.booklist[bookchoice]['count'] - 1
                self.booklist[bookchoice].update({'count': booksCount})
                # colored is used to display the text in the required color
                color1 = colored("You book has been issued successfully", 'green')
                print(color1)
        else:
            color4 = colored("We couldn't find any user with this name or Member type", 'red')
            print(color4)

    # Method Book Returns
    def returnBook(self):
        studentOrFaculty = input("Are you Student or Faculty:")
        username = input("Please enter your name:")
        bookchoice = input("Please enter name of the book that you wanted to return:")
        booksCount = self.booklist[bookchoice]['count'] + 1
        validatioCheck = Members(studentOrFaculty, username)

        # Performing member validation if user exists or not
        # Calling Member calss for validation but it internally calls either Student class to Faculty class for validation
        if validatioCheck.memberValidation() == True:
            if self.bookStore[bookchoice]['count'] >= booksCount:
                self.booklist[bookchoice].update(
                    {'count': booksCount})  # Accessing and Updating the other class variables
                print("You choose to return ", bookchoice, "and it is successfull")

            else:
                color3 = colored("Sorry we haven't issued any book with this name", 'red')
                print(color3)
        else:
            color4 = colored("We couldn't find any user with this name or Member type", 'red')
            print(color4)


# This is the base class which has Student and Faculty as Child classed
class Members():
    memberlist = {
        "name": {
            "id": '',
            "name": '',
            "dept": '',
        }
    }
    def __init__(self, member, name):
        self.member = member
        self.name = name

    # Method to validate member
    def memberValidation(self):
        if self.member == 'Student':
            studentClass = Student(self.name)
            value = studentClass.memberValidation()
            return value
        elif self.member == 'Faculty':
            facultyClass = Faculty(self.name)
            value = facultyClass.memberValidation()
            return value

# Inheriting Member class variables and methods
class Student(Members):
    def __init__(self,name):
        self.stdname = name

    #Acess Memberlist object from Member class
    Members.memberlist = {
        'Dharani':{
                "id": '1',
                "name": 'Dharani',
                "dept": 'CSE',
            },
         'Pavan':   {
                "id": '2',
                "name": 'Pavan',
                "dept": 'CSE',
            }
}
    def issuedBooks(self):
        booksIssed= {
            "totalBooksCount":'',
            "issuedDate":'',
            "bookName":'',
            "studentID":'',
        }

    def returnedBooks(self):
        booksIssed = {
            "totalBooksCount": '',
            "returnDate": '',
            "bookName": '',
            "studentID": '',
        }

   # Overwriting Member class method
    def memberValidation(self):
        for user in self.memberlist:
            if user == self.stdname:
                return True


class Faculty(Members):
    FacultyList = {
        'Teja': {
            "id": '1',
            "name": 'Teja',
            "dept": 'CSE',
        },
        'Ugandhar': {
            "id": '2',
            "name": 'Ugandhar',
            "dept": 'CSE',
        }
    }
    def __init__(self,name):
        self.fcName = name

    def issuedBooks(self):
        booksIssed= {
            "totalBooksCount":'',
            "issuedDate":'',
            "bookName":'',
            "studentID":'',
        }

    def returnedBooks(self):
        booksIssed = {
            "totalBooksCount": '',
            "returnDate": '',
            "bookName": '',
            "studentID": '',
        }

    def memberValidation(self):
        for user in self.FacultyList:
            if user == self.fcName:
                return True


if __name__ == '__main__':

    # This Dictionary is default storage of books with no changes when books issued are returned,
    # This helps us to check whether books has been really issued or not

    decision = 'y'
    while decision.lower()=='y':
        print("----Welcome Library Management System---")
        print("""
                     1. List all available books
                     2. Request for Book 
                     3. Return a Book
                  """)
        choice = int(input("Please Enter your choice:"))
        library = ManageLibrary()
        if choice == 1:
            library.availableBooks()
        elif choice == 2:
            library.checkOutBook()
        elif choice == 3:
            library.returnBook()
        decision = input("Do you want to continue(y/n):")
