#Super() builtin function that allows us to access method of base class .

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))



class Student(Person):
    def __init__(self, name, age, gender, studentid, fees):
        super().__init__(name,age,gender)
        self.studentid = studentid
        self.fees = fees


    def StudentInfo(self):
        super().PersonInfo()
        print('Student ID : {}'.format(self.studentid))
        print('Fees : {}'.format(self.fees))


stu_obj = Student('pooja', 25, 'female', 12345, 100000)
stu_obj.StudentInfo()
        
        
