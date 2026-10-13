##task 1:

class student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def displayGraduateStudent(self):
        print("name :",self.name )
        print("age :",self.age )
        print("course:",self.course )
##task2
class GraduateStudent(student):
    def __init__(self, name, age, course, research):
        super().__init__(name,age,course)
        self.name =name
        self.age =age
        self.course =course
        self.research =research

g1=GraduateStudent("Jazzi", 20 ,"Math", "Marketing" )
print("Student 1: ")
g1.displayGraduateStudent()

g2=GraduateStudent("ALi", 20 ,"English", "Teaching" )
print("Student 2: ")
g2.displayGraduateStudent()



