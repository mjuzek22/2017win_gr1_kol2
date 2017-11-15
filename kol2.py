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

class Class:
	def __init__(self, name):
		self.name = name
        self.attendance = 0
        self.scores = [] 

	def add_attendance(self, attendance):
		self.attendance = attendance

	def add_score(self, score):
		self.scores.append(score)

	def get_average_score(self):
		sum = 0
		for i in self.average.scores:
			sum += i
		return sum/len(self.average.scores)

	def get_attendance(self):
		sum = 0
		for i in self.average.scores:
			sum += i
		return sum/len(self.average.scores)
		

class Student:
	def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.classes = []

	def add_class(self, class_name):
		class_1 = Class(class_name)
		self.classes.append(class_1)

	def get_average_score_in_class(self, class_name):
		total_sum = 0
		for i in range(len(self.classes)):
			if self.classes[i].name == class_name:
				total_sum += self.classes[i].get_average_score()
		return total_sum/len(self.classes)
	
		
		
class Diary:
	def __init__(self, group_name):
        self.group_name = group_name
		self.students = []
        
	def add_student(self, student_name, student_surname):
		student_1 = Student(student_name, student_surname)
		self.students.append(student_1)
        
	def get_average_scores_in_class(self, class_name):
		total_sum = 0
		for i in range(len(self.students)):
			total_sum += self.students[i].get_average_score_in_class(class_name)
		return total_sum/len(self.students)

	def get_total_average_score_of_student(self, student_name, student_surname):
		total_sum = 0
		for i in range(len(self.students)):
			if self.students[i].name == student_name && self.students[i].surname == student_surname:
				for j in range(self.students[i].classes)
					total_sum += elf.students[i].classes[j].get_average_score()
				return total_sum/len(self.students[i].classes)
