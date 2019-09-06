class Employee:
    data_counter = 0
    total_avg_salary=0
    total_salary=0
    def __init__(self, name, family, salary, department):
        self.empname= name
        self.empfamily= family
        self.empsalary = salary
        self.empdepartment= department
        self.datamemberdefination()
        Employee.total_salary = Employee.total_salary + self.empsalary

    def datamemberdefination(self):

        Employee.data_counter = Employee.data_counter+1


    def avg_salary(self):

        Employee.total_avg_salary= Employee.total_salary/Employee.data_counter

class FulltimeEmployee(Employee):

    def __init__(self,name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)




if __name__ == '__main__':
    e = Employee("Rani", "single", 2, "Developer")
    e1 = FulltimeEmployee("Nani", "single", 3, "DataScientist")
    e1.avg_salary()
    print(Employee.total_avg_salary)



