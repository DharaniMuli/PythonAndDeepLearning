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

        # append is a method in the list class so calling using list object
        self.mylist.append(self.empsalary)
        Employee.total_salary = Employee.total_salary + self.empsalary

    def datamemberdefination(self):
        Employee.data_counter = Employee.data_counter + 1

    def avg_salary(self):
        Employee.total_avg_salary = Employee.total_salary / Employee.data_counter


class FulltimeEmployee(Employee):
    maxsalary =0
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def highestsalary(self):
        #This "mylist' is a list object in base class 'Employee'
            list1= Employee.mylist
            maxsalary = max(list1)
            return maxsalary

if __name__ == '__main__':
    e = Employee("Rani", "single", 2, "Developer")
    f1 = FulltimeEmployee("Nani", "single", 3, "DataScientist")

    #Access base class method
    f1.avg_salary()
    print("Average of Salary:",Employee.total_avg_salary)
    f1.highestsalary()

    #Access Derived class method
    print("Highest Salary:",f1.highestsalary())