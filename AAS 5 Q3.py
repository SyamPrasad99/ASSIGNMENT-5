class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student = Student()
student.setName("syam")
student.setRollNumber("16313")
print(student.getName())        
print(student.getRollNumber()) 
