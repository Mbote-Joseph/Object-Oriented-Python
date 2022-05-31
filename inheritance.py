class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def getEmail(self):
        print(f"{self.first.lower()}.{self.last.lower()}@company.com")

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def works(self):
        print(f"{self.first} is working")


#Software Engineer class inherits from Employee class
class SoftwareEngineer(Employee):
    #Overriding the init method
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def print_info(self):
        print(f"{self.first} {self.last} makes {self.pay} a year and uses {self.prog_lang}")

    def code(self):
        print(f"{self.first} is coding")

    def work(self):
        self.code()



#Designer Class inherits from Employee class
class Designer(Employee):
    def work(self):
        print(f"{self.first} is designing")

    def draw(self):
        print(f"{self.first} is drawing")

emp=SoftwareEngineer('John', 'Smith', 50000, 'Python')
print(emp.fullname())
emp.getEmail()
emp.print_info()
emp.code()