class Student:
    stuCount = 0
    
    def __init__(self, fname, lname, gender, age):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.age = age
        Student.stuCount += 1

    def displayInfo(self):
        print('First Name: ' + self.fname +
              'Last Name: ' + self.lname +
              'Gender: ' + self.gender +
              'Age: ' + str(self.age)
              )


print('Student Information System')
print('''Menu
1. Add
2. Dispaly
3. Total student
4. Exit''')

while True:
    choice = int(input('Enter your choice:'))
    if choice >= 1 and choice <=4:
    
        if choice == 4:
            break

        if choice == 1:
            fname = input('First Name:')
            lname = input('Last Name:')
            gender = input('Gender:')
            age = input('Age:')
            student = Student(fname,lname,gender,age)
        elif choice == 2:
            student.displayInfo()
        elif choice == 3:
            print('Total Students' + str(Student.stuCount))
    else:
        print('Invalid choice!!')
    
