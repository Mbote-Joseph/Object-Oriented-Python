#Encapsulation is the process of wrapping the data and code together to form an object.
#Hiding the data and code from the user.

class SoftwareEngineer:
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level
        self.__salary= None
        self.__num_bugs_solved = 0

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def calculate_salary(self):
        if self.__num_bugs_solved < 10:
            return self.__salary
        elif self.__num_bugs_solved < 20:
            return self.__salary * 1.1
        else:
            return self.__salary * 1.2

    def get_num_bugs_solved(self):
        return self.__num_bugs_solved
    
    def set_num_bugs_solved(self, num_bugs_solved):
        self.__num_bugs_solved = num_bugs_solved

se= SoftwareEngineer("John", 30, "Junior")
se.set_salary(100000)
se.set_num_bugs_solved(45)
se.calculate_salary()
print(se.name, se.age, se.level, se.get_salary(), se.get_num_bugs_solved())
        

    