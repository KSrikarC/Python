from Custom_Func import cls
cls()

#Basic Inheritance
'''
class Book():
    def __init__(self,name):
        self.name = name

class NewsPaper():
    def __init__(self,name):
        self.name = name            
        

b = Book('Harry porter : Goblet of fire')
n = NewsPaper('Times of India')

print(b.__class__.__name__, n.__class__.__name__)

print(type(b) == type(n))

print(isinstance(n, object))   '''


# Parent - Child inheritance

'''
class Student():
    def __init__(self, name,id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    def get_student_details(self):
        return f"The student {self.name} with roll no({self.id}) secured {self.cgpa}%"

class Department(Student):
    def __init__(self, name, id, cgpa,dept_name):
        super().__init__(name, id, cgpa)
        self.dept_name = dept_name

    def get_dept_details(self):
        return f'The student {self.name} with roll no({self.id}) belongs to {self.dept_name}'    

s = Student('Srikar', 9026, 9.1)
d = Department('Srikar', 9026, 9.1,'ECE')
print(d.get_student_details(),'\n\n',d.get_dept_details(),'\n\n')'''

#Multiple inheritance

class Python():
    def HasPy(self):
        print('Has Python')

class SQL():
    def HasSQL(self):
        print("Has SQL")        

class Linux():
    def HasLINUX(self):
        print("Has LINUX")

class AWS():
    def HasAWS(self):
        print("Has AWS")

class Skilled_Person(Python,SQL,Linux,AWS):
    def checkSkills(self):
        self.HasPy()
        self.HasLINUX()
        self.HasAWS()
        self.HasSQL()

class Intermediate_Person(Python,Linux,SQL):
    def checkSkills(self):
        self.HasLINUX()
        self.HasPy()
        self.HasSQL()

class Rookie_Person(Linux):
    def checkSkills(self):
        self.HasLINUX()        

a = Skilled_Person()
b = Intermediate_Person()
c = Rookie_Person()

#print(a.checkSkills())

#print(b.checkSkills())

print(c.checkSkills())




































