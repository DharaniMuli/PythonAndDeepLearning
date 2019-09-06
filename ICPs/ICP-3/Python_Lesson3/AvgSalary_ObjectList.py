class Employee:
    data_counter = 0
    total_avg_salary = 0
    total_salary = 0

    # List is a class so I am creating an object for class
    mylist = list()

    def __init__(self, name, family, salary, department):
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        self.datamemberdefination()

        # Append is a method in the list class so calling using list object
        # Storing all the salaries into list
        self.mylist.append(self.empsalary)
        Employee.total_salary = Employee.total_salary + self.empsalary

    def datamemberdefination(self):
        Employee.data_counter = Employee.data_counter + 1

    def avg_salary(self):
        Employee.total_avg_salary = Employee.total_salary / Employee.data_counter

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

    while moredata.lower() == 'y':
        name = input("Enter First Name: ")
        family = input("Enter Last Name:")
        salary = int(input("Enter Salary:"))
        department = input("Enter Department:")
        f1 = FulltimeEmployee(name, family, salary, department)
        moredata=input("Do you want to add  Employee(Y/N):")
        # Access base class method
    f1.avg_salary()
    print("Average Salary:", Employee.total_avg_salary)
    f1.highestsalary()

    #Access Derived class method
    print("Highest Salary:",f1.highestsalary())
