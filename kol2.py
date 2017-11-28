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

import argparse
import json
import os.path
            
class School(object):
    def __init__(self):
        self.data = {}
        
    def add_class(self, name):
        self.data[name] = {}
        
    def add_student(self, class_name, student_name):
        self.data[class_name][student_name] = {"attendance": []}
        
    def add_subject(self, class_name, subject_name):
        for student in self.data[class_name]:
            self.data[class_name][student][subject_name] = []
        
    def add_grade(self, class_name, student_name, subject_name, grade):
        self.data[class_name][student_name][subject_name].append(grade)
        
    def add_attendance(self, class_name, student_name, is_attended):
        self.data[class_name][student_name]["attendance"].append(is_attended == 1)
        
    def get_attendance(self, class_name, student_name):
        sum = 0
        for attendance in self.data[class_name][student_name]["attendance"]:
            if(attendance):
                sum = sum +1
        return float(sum)/len(self.data[class_name][student_name]["attendance"])
        
    def get_class_average(self, clas):
        i = 0
        sum = 0
        for student in self.data[clas]:
            for subject in self.data[clas][student]:
                if (not subject=="attendance"):
                    for grade in self.data[clas][student][subject]:
                        i = i+1
                        sum = sum + grade
        return sum/i
        
    def get_average(self):
        i = 0
        sum = 0
        for clas in self.data:
            for student in self.data[clas]:
                for subject in self.data[clas][student]:
                    if (not subject=="attendance"):
                        for grade in self.data[clas][student][subject]:
                            i = i+1
                            sum = sum + grade
        return sum/i
                

if __name__ == "__main__":
    data = None
    if(os.path.exists('szkola.json')):
        with open('szkola.json', 'r') as fp:
            data = json.load(fp)
    print(data is not None)
    school = School()
    if(data is not None):
        print('czytanie z poprzedniego pliku...')
        school.data = data
    else:
        print("Tworzenie szkoly")
        school.add_class("1")
        school.add_student("1", "student1")
        school.add_subject("1", "python")
        school.add_grade("1", "student1", "python", 2)
        school.add_grade("1", "student1", "python", 3)
        school.add_grade("1", "student1", "python", 3.5)
        school.add_class("2")
        school.add_student("2", "student drugiej klasy")
        school.add_subject("2", "python2")
        school.add_subject("2", "jezyk polski")
        school.add_grade("2", "student drugiej klasy", "python2", 6)
        school.add_grade("2", "student drugiej klasy", "jezyk polski", 5)
        school.add_grade("2", "student drugiej klasy", "jezyk polski", 6)
        print("Srednia:")
        print(school.get_average())
        print("srednia w klasie 1:")
        print(school.get_class_average("1"))
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 0)
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 1)
        school.add_attendance("1", "student1", 1)
        print("Frekwencja studenta1: ")
        print(school.get_attendance("1", "student1"))
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-o', '--ocena', metavar='ocena', type=int,
                     help='ocena dla studenta')
    args = parser.parse_args()
    if(vars(args)['ocena'] is not None):
        print("Dodano ocene :")
        print(vars(args)['ocena'])
        school.add_grade("1", "student1", "python", vars(args)['ocena'])
        print("Srednia szkoly po dodaniu oceny dla student1: (parametr -o przy uruchamianiu)")
    else:
        print("Srednia szkoly bez dodania oceny dla student1: (parametr -o przy uruchamianiu)")
    print(school.get_average())
    print("Zapisywanie szkoly do pliku")
    with open('szkola.json', 'w') as fp:
        json.dump(school.data, fp)