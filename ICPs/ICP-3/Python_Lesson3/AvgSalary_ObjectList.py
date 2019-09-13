class Employee:

    avg_salary = 0
    total_salary = 0


    # List is a class so I am creating an object for class
    mylist = list()

    def __init__(self, name=None, family=None, salary=None, department=None):
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        self.data_counter = 0


        # Append is a method in the list class so calling using list object
        # Storing all the salaries into list
        self.mylist.append(self.empsalary)


    def avg_salary(self,EmpList=[],*args):
        data_counter=0
        for i in  EmpList:
            data_counter+=1
            Employee.total_salary = Employee.total_salary + i.empsalary
            Employee.avg_salary = Employee.total_salary / data_counter
        return Employee.total_salary


# This is a derived class 'FulltimeEmployee' inheriting base class 'employee'
class FulltimeEmployee(Employee):
    maxsalary =0
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def highestsalary(self):
        #Access base class list object
            list1= Employee.mylist
        # Finding Max salary
            maxsalary = max(list1)
            return maxsalary

if __name__ == '__main__':

    moredata= "y"
    EmployeeList = []

    while moredata.lower() == 'y':
        name = input("Enter First Name: ")
        family = input("Enter Last Name:")
        salary = int(input("Enter Salary:"))
        department = input("Enter Department:")
        f1 = FulltimeEmployee(name, family, salary, department)
        EmployeeList.append(f1)
        moredata=input("Do you want to add  Employee(Y/N):")
        a=f1.avg_salary(EmployeeList)
        # Access base class method

    print("Average Salary:", Employee.avg_salary)
    f1.highestsalary()

    #Access Derived class method
    print("Highest Salary:",f1.highestsalary())