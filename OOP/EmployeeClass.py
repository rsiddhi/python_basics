class Employee:
    def __init__(self, name, department, email, age):
        self.name = name
        self.department = department
        self.email = email
        self.age = age

    def displayInformation(self):
        info = self.name + "\n" + self.department + "\n"  + self.email + "\n"  + str(self.age)
        print(info)

employee1 = Employee('Adam', 'IT', 'adma@xyz.com', 30)
employee1.displayInformation()
print('Employee.__doc__:', Employee.__doc__)
print('Employee.__name__:', Employee.__name__)

print('Employee.__module__:', Employee.__module__)
        


