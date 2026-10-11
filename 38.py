# OOP: Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def total_salary(self):
        return self.salary + self.bonus


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def show_details(self):                  # override
        super().show_details()
        print(f"Language: {self.language}")


# Objects
m1 = Manager("Ravi", 50000, 10000)
m2 = Manager("Sneha", 60000, 15000)
d1 = Developer("Deepak", 40000, "Python")
d2 = Developer("Anjali", 45000, "Java")

for m in (m1, m2):
    m.show_details()
    print("Total Salary:", m.total_salary())

for d in (d1, d2):
    d.show_details()