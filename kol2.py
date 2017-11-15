# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class School(object):
	def __init__(self):
		self.classes = []

	def AddClass(self, clas):
		self.classes.append(clas)

	def GetAverage(self):
		Average = 0
		i = 0
		for clas in self.classes:
			if(clas.GetAverage() != None):
				Average = Average + clas.GetAverage()
				i = i + 1
		if(i > 0):
			return float(Average)/(i)
		else:
			return None

class Class(object):
	def __init__(self):
		self.Students = []

	def AddStudent(self, Student):
		self.Students.append(Student)

	def GetAverage(self):
		Average = 0
		i = 0
		for Student in self.Students:
			if(Student.GetAverage() != None):
				Average = Average + Student.GetAverage()
				i = i + 1
		if(i > 0):
			return float(Average)/(i)
		else:
			return None
			

class Student(object):
	def __init__(self, Name, Surname):
		self.Grades = []
		self.Attendance = []
		self.Name = Name
		self.Surname = Surname

	def AddGrade(self, Grade):
		self.Grades.append(float(Grade))

	def GetAverage(self):
		Average = 0
		i = 0
		for Grade in self.Grades:
			Average = Average + Grade
			i = i + 1
		if(i > 0):
			return float(Average)/(i)
		else:
			return None

	def AddAttendance(self, IsAtt):
		self.Attendance.append(IsAtt)

	def CountAttendance(self):
		Counted = 0
		i = 0
		for Att in self.Attendance:
			Counted = Counted + Att
			i = i + 1
		if(i > 0):
			return float(Counted)/(i)
		else:
			return None

if __name__ == "__main__":
	school = School()
	print("Creating school")
	class1 = Class()
	print("Creating class1")
	class2 = Class()
	print("Creating class2")
	school.AddClass(class1)
	school.AddClass(class2)
	student = Student("stu", "dent")
	student.AddGrade(3.2)
	student.AddGrade(4.1)
	student.AddAttendance(1)
	student.AddAttendance(1)
	student.AddAttendance(1)
	student.AddAttendance(0)
	grade = float(input("Podaj ocene dla studenta"))
	student.AddGrade(grade)
	student2 = Student("stus", "denst")
	student2.AddGrade(2.2)
	student2.AddGrade(6.1)
	class2.AddStudent(student2)
	print("Srednia studenta:")
	print(student.GetAverage())
	class1.AddStudent(student)
	print("Srednia szkoly:")
	print(school.GetAverage())
	print("Srednia w klasie 1:")
	print(class1.GetAverage())
	print("Frekwencja studenta:")
	print(student.CountAttendance())









