class Dog:
    def sound(self):
        print("Dog says Woof")

class Cat:
    def sound(self):
        print("Cat says Meow")


class Cow:
    def sound(self):
        print("Cow says Moo")

def animal_sound(animal):
    animal.sound()

Dog1 = Dog()
Cat1 = Cat()
Cow1 = Cow()
animal_sound(Dog1)
animal_sound(Cat1)
animal_sound(Cow1)


class UPI:
    def pay(self):
        print("Payment using UPI")


class CreditCard:
    def pay(self):
        print("Payment using Credit Card")


class Cash:
    def pay(self):
        print("Payment using Cash")

def make_payment(payment):
    payment.pay()

make_payment(UPI())
make_payment(CreditCard())
make_payment(Cash())

class Developer:
    def work(self):
        print("Developer is writing Python code")


class Manager:
    def work(self):
        print("Manager is managing the team")


class Tester:
    def work(self):
        print("Tester is testing the application")


employees = [
    Developer(),
    Manager(),
    Tester()
]

for employee in employees:
    employee.work()