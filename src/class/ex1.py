class Student:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f'My name is {self.name}')


studenta = Student('Sam')
studentb = Student('Bob')

print (studenta.name)   # Sam
print (studentb.name)   # Bob

studenta.introduce()    # My name is Sam
studentb.introduce()    # My name is Bob

