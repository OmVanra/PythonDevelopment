class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Name :", self.name)
        print("Age :", self.age)

    @classmethod
    def change_school(cls, changed_name):
        cls.school = changed_name

    @staticmethod
    def is_valid_age(age):
        if age > 0:
            return "valid"

Student1 = Student("OM", 20)

Student1.display_info()
Student.change_school("Shreeji Vidhyalaya")
print(Student.school)
print(Student.is_valid_age(20))


class Employee:
    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, changed_company):
        cls.company = changed_company

Employee1 = Employee("OM", 25000)
Employee1.change_company("Om Company")
print(Employee1.company)


class Employe:

    @staticmethod
    def is_valid_salary(salary):
        if salary > 0:
            return True
        else:
            return False

print(Employe.is_valid_salary(50000))
print(Employe.is_valid_salary(-1000))