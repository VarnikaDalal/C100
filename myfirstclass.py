class Student(object):
    def __init__(self, name, age, grades=None):
        self.name=name
        self.age=age
        self.grades=grades or {}
    def setgrade(self, course, grades):
        self.grades[course]=grades
    def setgrade(self,course):
        return self.grades[course]

Liv=Student("Liv", 15, 9)
