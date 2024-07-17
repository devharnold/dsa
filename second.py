"""
Program that stores and manages details about a student:
    Department, Course, Number of units done, score for each unit, average score
Note that grade is based on the average score from 90-100(A), from 80-89(B), from 70-79(C)
60-69(D). then 0-59(FAIL)
"""


class Student:
    def __init__(self, name, department, course):
        self.name = name
        self.department = department
        self.course = course
        self.units = [] #set empty array of units

    def add_unit(self, score, unit_name):
        self.units.append((unit_name, score))

    def calculate_average(self):
        if not self.units:
            return 0
        total_score = sum(score for unit_name, score in self.units)
        return total_score / len(self.units)
    
    def find_grade(self, average_score):
        if 90 <= average_score <= 100:
            return 'A'
        elif 80 <= average_score <= 89:
            return 'B'
        elif 70 <= average_score <= 79:
            return 'C'
        elif 60 <= average_score <= 69:
            return 'D'
        else:
            return 'FAIL'
        
    def display_details(self):
        print(f"Student name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Course: {self.course}")

        for unit_name, score in self.units:
            print("f {unit_name}: {score}")
        
        average_score = self.calculate_average()
        print(f"Your average score is: {average_score:.2F}")
        print(f"Grade: {self.determine_grade(average_score)}")


student = Student("Henry Arnold", "Information Technology", "Data Structures")
student.add_unit("Arrays", 80)

student.display_details()
