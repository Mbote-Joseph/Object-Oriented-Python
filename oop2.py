#A class is a blueprint for an object
class SoftwareEngineer:
    #class attribute
    alias = "Software Engineer"
    #A constructor is a special method that is called when an object is created
    def __init__(self, name, age, level, salary):
        #Instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    #A method is a function that is associated with an object
    def print_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Level: " + self.level)
        print("Salary: " + str(self.salary))

    def code(self):
        print(f"{self.name} is coding")

    def __str__(self):
        return f"{self.name} has the age of {self.age} and is a {self.level} {self.alias}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.level == other.level and self.salary == other.salary

    def entry_salary(self,age):
        if age < 30:
            return "100000"
        elif age < 40:
            return "120000"
        elif age < 50:
            return "150000"
        else:
            return "200000"


# Instant
#An instance is an object that is created from a class
softwareEngineer1 = SoftwareEngineer("John", 30, "Junior", "100000")
softwareEngineer2 = SoftwareEngineer("Jane", 25, "Senior", "150000")
softwareEngineer3 = SoftwareEngineer("Jack", 35, "Mid-level", "120000")

softwareEngineer1.print_info()

engineers=[softwareEngineer1, softwareEngineer2, softwareEngineer3]

for engineer in engineers:
    print(engineer.__str__())
    print("===============")

softwareEngineer1.entry_salary(45)