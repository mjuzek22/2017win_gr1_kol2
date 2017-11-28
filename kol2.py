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

import json

class Diary:
    def __init__(self, name):
        self.class_name = name
        self.students = {}

    def add_student(self, name, surname):
        student = {'Student': str(name) + " " + str(surname), 'Classes': {}}
        self.students[str(name) + " " + str(surname)] = student

    def add_class(self, student_name, class_name):
        class_1 = {'Attendance': 0, 'Class_number': 0, 'Scores': []}
        self.students[str(student_name)]['Classes'][class_name] = class_1

    def add_student_score_in_class(self, student_name, class_name, score):
        self.students[str(student_name)]['Classes'][class_name]['Scores'].append(score)

    def add_student_attendance_in_class(self, student_name, class_name):
        self.students[str(student_name)]['Classes'][class_name]['Attendance'] += 1
        self.students[str(student_name)]['Classes'][class_name]['Class_number'] += 1

    def add_student_absence_in_class(self, student_name, class_name):
        self.students[str(student_name)]['Classes'][class_name]['Class_number'] += 1

    def get_total_average_score_in_class(self, class_name):
        sum1 = 0
        total = 0
        for key in self.students:
            sum1 += sum(self.students[key]['Classes'][class_name]['Scores'])
            total += len(self.students[key]['Classes'][class_name]['Scores'])
        return sum1/total

    def get_total_attendance_of_student(self, student_name):
        sum1 = 0
        total = 0
        for key in self.students[student_name]['Classes']:
            sum1 += self.students[student_name]['Classes'][key]['Attendance']
            total += self.students[student_name]['Classes'][key]['Class_number']
        return str((sum1*100)/total) + " %"

    def get_student_average_score_in_class(self, student_name , class_name):
        return sum(self.students[student_name]['Classes'][class_name]['Scores']) / len(self.students[student_name]['Classes'][class_name]['Scores'])

    def write_diary_to_json(self, file_name):
        with open(file_name, 'w') as f1:
            json.dump(self.students, f1)
            f1.close()




c1 = Diary("2a")
c1.add_student("Janek", "Kowalski")
c1.add_student("Ania", "Nowak")

c1.add_class("Janek Kowalski", "English")
c1.add_class("Ania Nowak", "English")
c1.add_class("Janek Kowalski", "Maths")
c1.add_class("Ania Nowak", "Maths")
c1.add_student_score_in_class("Janek Kowalski", "English", 5)
c1.add_student_score_in_class("Janek Kowalski", "English", 4)
c1.add_student_score_in_class("Janek Kowalski", "English", 3)
c1.add_student_score_in_class("Ania Nowak", "English", 5)
c1.add_student_score_in_class("Ania Nowak", "English", 5)
c1.add_student_score_in_class("Janek Kowalski", "Maths", 4)
c1.add_student_score_in_class("Janek Kowalski", "Maths", 4)
c1.add_student_score_in_class("Janek Kowalski", "Maths", 3)
c1.add_student_score_in_class("Ania Nowak", "Maths", 3)
c1.add_student_score_in_class("Ania Nowak", "Maths", 3)

c1.add_student_absence_in_class("Janek Kowalski", "Maths")
c1.add_student_absence_in_class("Janek Kowalski", "English")
c1.add_student_attendance_in_class("Janek Kowalski", "Maths")
c1.add_student_attendance_in_class("Ania Nowak", "Maths")
c1.add_student_attendance_in_class("Ania Nowak", "English")
c1.add_student_attendance_in_class("Ania Nowak", "Maths")


print("Total attendance of Janek Kowalski: ",c1.get_total_attendance_of_student("Janek Kowalski"))
print("Average score in Maths of Janek Kowalski: ", c1.get_student_average_score_in_class("Janek Kowalski", "Maths" ))
print("Average score in English: ", c1.get_total_average_score_in_class('English'))

c1.write_diary_to_json("diary1.json")
