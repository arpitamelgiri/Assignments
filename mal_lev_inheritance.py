class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def PersonInfo(self):
        print('Name : {}'.format(self.name))
        print('Age : {}'.format(self.age))
        print('Gender : {}'.format(self.gender))



class employee(Person):
    def __init__(self, name, age, gender, empid, salary):
        Person.__init__(self, name,age,gender)
        self.empid = empid
        self.salary = salary


    def EmployeeInfo(self):
        print('Emp ID : {}'.format(self.empid))
        print('salary : {}'.format(self.salary))
        
class Fulltime(employee):
    def __init__(self, name, age, gender, empid, salary, workexperience):
        employee.__init__(self, name, age, gender, empid, salary)
        self.workexperience = workexperience

    def FulltimeInfo(self):
        print('work Experience : {}'.format(self.workexperience))

class contractual(employee):
    def __init__(self, name, age, gender, empid, salary,contractexpiry):
        employee.__init__(self, name, age, gender, empid, salary)
        self.contractexpiry = contractexpiry

    def contractInfo(self):
        print('contract expiry : {}'.format(self.contractexpiry))
            
print('contractual employee details:')
print("***************************************************")
contr_obj = contractual('arpita', 25, 'female', 12345, 70000, '31-12-2022')
contr_obj. PersonInfo()
contr_obj.EmployeeInfo()
contr_obj.contractInfo()


print('Fulltime  employee Details:')
print("***************************************************")

full_obj = Fulltime("pooja", 25,'female', 12456, 70000, 5)
full_obj.PersonInfo()
full_obj.EmployeeInfo()
full_obj.FulltimeInfo()














        
    
