
#position, name, age, level, salary
softwareEngineer1 =["Software Engineer", "John", 30, "Junior", "100000"]
softwareEngineer2 =["Software Engineer", "Jane", 25, "Senior", "150000"]
softwareEngineer3 =["Software Engineer", "Jack", 35, "Mid-level", "120000"]

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


# Instant
#An instance is an object that is created from a class
softwareEngineer1 = SoftwareEngineer("John", 30, "Junior", "100000")
softwareEngineer2 = SoftwareEngineer("Jane", 25, "Senior", "150000")
softwareEngineer3 = SoftwareEngineer("Jack", 35, "Mid-level", "120000")

softwareEngineer1.print_info()

engineers=[softwareEngineer1, softwareEngineer2, softwareEngineer3]

for engineer in engineers:
    engineer.print_info()
    print("===============")

print(f"{softwareEngineer1.name} is a {softwareEngineer1.alias}")