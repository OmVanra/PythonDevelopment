from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI ({self.upi_id})")


class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        last4 = self.card_number[-4:]
        print(f"Paid ₹{amount} using Credit Card ending in {last4}")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash")


# Test
payments = [UPI("asha@upi"), CreditCard("1234567812345678"), Cash()]

for p in payments:
    p.pay(1500)

# Payment()  # TypeError: Can't instantiate abstract class Payment


from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key or push button")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick or self-start")


# Test
vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()



from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours * self.hourly_rate


# Test: one loop, different behaviour per object
employees = [
    FullTimeEmployee("Asha", 50000),
    PartTimeEmployee("Ravi", 80, 250),
    FullTimeEmployee("Meera", 65000),
    PartTimeEmployee("Kiran", 60, 300),
]

for employee in employees:
    print(f"{employee.name}: ₹{employee.calculate_salary()}")
