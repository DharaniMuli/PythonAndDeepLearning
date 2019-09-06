class Employee:
    data_counter = 0
    total_avg_salary = 0
    total_salary = 0

    def __init__(self, name, family, salary, department):
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        self.datamemberdefination()
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
            list = [100,200,300]
            maxsalary = max(list)

if __name__ == '__main__':
    e = Employee("Rani", "single", 2, "Developer")
    f1 = FulltimeEmployee("Nani", "single", 3, "DataScientist")
    f1.avg_salary()
    print(Employee.total_avg_salary)
    f1.highestsalary()
    print(FulltimeEmployee.maxsalary)