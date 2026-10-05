class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Course :", self.course)

Student1 = Student("Om", 20, "Python")
Student2 = Student("Rahul", 21, "Java")

Student1.display_info()
Student2.display_info()

class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("not sufficient balance.")
        else:
            self.balance -= amount

    def show_balance(self):
        print("Account Holder :",self.account_holder)
        print("Balance :", self.balance)

account = BankAccount("Om", 10000)

account.deposit(5000)
account.withdraw(2000)

account.show_balance()                    


class Employee():
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def increase_salary(self, percentage):
        increase = self.salary * percentage / 100
        self.salary += increase

    def display_info(self):
        print("Name :",self.name)
        print("Salary :", self.salary)
        print("department :", self.department)

employee = Employee("Om", 50000, "IT")

employee.increase_salary(10)

employee.display_info()        
        