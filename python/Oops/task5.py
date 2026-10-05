class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than 0")
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Test
account = BankAccount(10000)
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())   # 12000



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        self.set_salary(salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be greater than 0")
        self.__salary = salary


# Test 1: valid salary
employee = Employee("Ravi", 30000)
employee.set_salary(50000)
print(employee.get_salary())   # 50000

# Test 2: invalid salary
employee.set_salary(-1000)     # raises ValueError


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = 18          # safe default
        self.age = age           # goes through the setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 18:
            self.__age = value
        else:
            print("Invalid age")


# Test
student = Student("Asha", 20)

student.age = 22
print(student.age)    # 22

student.age = 15      # prints: Invalid age
print(student.age)    # 22 (unchanged)