#ACTIVITY 1
#IS THAT A BUS

class Vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

School_bus=Bus("School volvo",180,12)
print("Vehicle Name:",School_bus.name,"Speed",School_bus.max_speed,"Mileage:",School_bus.mileage)

#ACTIVITY 2
#EMPLOYYEE INHERITANCE
class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person.__init__(self,name,idnumber)

a = Employee('Rahul',886012,200000,"Intern")
a.display()


#ACTIVITY 3
#SUPER PENGUIN
class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
#object creation
peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()