class Student:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f'My name is {self.name}')


studenta = Student('Sam')
studentb = Student('Bob')

print (studenta.name)
print (studentb.name)

studenta.introduce()
studentb.introduce()

''' Result:
Sam
Bob
My name is Sam
My name is Bob
'''
