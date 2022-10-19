# PYTHON CLASSES  - EXAMPLE 2

import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, phone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
        self.email = email


    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
            return age

        
person = Person('Arpita', 'anu', datetime.date(1998, 4, 9),
                'no. 12 Random street, Golflinks villa, Hyderdabad',' 1234567890', 'arpita.gmail.com')

print(person.name)
print(person.email)
print(person.age())
