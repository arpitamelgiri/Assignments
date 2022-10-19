class Person:    #parent class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def greet(self):
        print("Hello Person")


class Student(Person):
    def __init__(self, name, age, gender, studentid, fees):
        Person.__init__(self,name,age,gender)
        self.studentid = studentid
        self.fees = fees



    def greet(self):
        print("hello Student")

stud_obj = Student('anu', 23, 'female', 12345, 15000)
stud_obj.greet()

person1 = Person('arpita', 25, 'female')
person1.greet()
