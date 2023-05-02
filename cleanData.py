# -*- coding: utf-8 -*-
"""
CLEAN DATA
This code was written by group 17
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""

#################
# Imports
#################



#################
# Variables
#################



#################
# Functions
#################

# This function defines the 7-step-scale, stores IDs in a set and stores data in an array
def cleanData(data):
    allowed_integers = [-3, 0, 2, 4, 7, 10, 12]
    student_ids = set()
    cleaned_data = []

# This function checks if the student ID is valid or not. It checks if it starts with s, is 7 digits long and if it gets repeated
    def is_valid_student_id(student_id):
        return (student_id and student_id.startswith("s") and len(student_id) == 7
                and student_id[1:3].isdigit() and student_id[3:].isdigit() and student_id not in student_ids)

# This function checks if the name is valid or not
    def is_valid_name(name):
        name_parts = name.split()
        return (name and len(name_parts) >= 2 and all(len(part) >= 2 for part in name_parts))
    
# This function checks if the grade is in the 7-step-scale
    def is_valid_grade(grade):
        return (grade is None or grade in allowed_integers)

    for row in data[1:]:
        # Validate Student ID
        student_id = row[0]
        if not is_valid_student_id(student_id):
            continue
        student_ids.add(student_id)

        # Validate Name
        name = row[1]
        if not is_valid_name(name):
            continue

        # Validate Grades
        grades = row[2:]
        if not all(is_valid_grade(grade) for grade in grades):
            continue

        # If all validations pass, append row to cleaned_data
        cleaned_data.append(grades)

    return cleaned_data



#################
# Script
#################



#################
# Test and debugging
#################
