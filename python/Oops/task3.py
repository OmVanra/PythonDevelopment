
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)

# class Manager(Employee):
#     def manage_team(self):
#         print("Manager manages the team")

# manager = Manager("Om", 60000)
# manager.display_info()  # Output: Name: Om, Salary: 60000
# manager.manage_team()   # Output: Manager manages the team


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        print("Course:",self.course)

Student1 = Student("OM",19,"Maths")       
Student1.display_person()
Student1.display_student()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display_info(self):
        print("Name:", self.name)
        print("salary:", self.salary)
        print("team_size:",self.team_size)

Manager1 = Manager("OM",200000,2)
Manager1.display_info()

class Employeee:
    def Work(self):
        print("Employee is working")

class Developer(Employeee):
    def Work(self):
        print("Developer is writing python code.")

class Managerr(Employeee):
    def Work(self):
        print("Manager is managing the team")

Employeee1 = Employeee()
Developer1 = Developer()
Managerr1 = Managerr()
Employeee1.Work()
Developer1.Work()
Managerr1.Work()

