class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
         
    def drive(self):
        print(f"Mašīna {self.brand} brauc!")

car1 = Car("BMW", 2015)
car2 = Car("Audi", 2020)
car3 = Car("Toyota", 2022)

print(car1.brand, car1.year)
print(car2.brand, car2.year)
print(car3.brand, car3.year)

car1.drive()
car2.drive()
car3.drive()  

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Sveiks, {self.name}, tev ir {self.age} gadi!")

p1 = Person("Jānis", 25)

class Animal:
    def make_sound(self):
        print("Some sound...")

class Dog(Animal):
    def make_sound(self):
        print("Vau vau!")

d = Dog()
d.make_sound()

cars = [
    Car("Mercedes", 2018),
    Car("Toyota", 2021),
    Car("Tesla", 2022)
]

for c in cars:
    print(c.brand)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, x):
        self.balance += x
        print(f"Iemaksāti {x} EUR. Jaunais atlikums: {self.balance} EUR.")
        
    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x
            print(f"Izņemti {x} EUR. Jaunais atlikums: {self.balance} EUR.")
        else:
            print("Nepietiek līdzekļu!")
            
    def info(self):
        print(f"Konts: {self.owner}, atlikums: {self.balance} EUR.")

acc = BankAccount("Anna")
acc.deposit(100)
acc.withdraw(67)
acc.info()   
