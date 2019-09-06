class Employee:
    data_counter = 0
    total_avg_salary=0
    total_salary=0
    def __init__(self, name, family, salary, department):
        self.empname= name
        self.empfamily= family
        self.empsalary = salary
        self.empdepartment= department
        Employee.total_salary = Employee.total_salary + self.empsalary
        self.datamemberdefination()

    def datamemberdefination(self):

        __class__.data_counter = __class__.data_counter+1

    def avg_salary(self):

        Employee.total_avg_salary= Employee.total_salary/Employee.data_counter

e = Employee("Rani","single", 2, "Developer")
print(Employee.total_salary)
e1 = Employee("Nani","single",3, "DataScientist")
print(Employee.total_salary)
print(Employee.data_counter)
# e2 = Employee("Nani","single",400, "DataScientist")
e1.avg_salary()
print(Employee.total_avg_salary)




