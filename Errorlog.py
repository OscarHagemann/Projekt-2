# -*- coding: utf-8 -*-
"""
ErrorFunction
Created on Mon April 25 17:03:02 2023
his code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""

#################
# Functions
#################

# This function defines the 7-step-scale, stores IDs in a dict and stores error log in a list
def validate_data(data):
    allowed_integers = [-3, 0, 2, 4, 7, 10, 12]
    student_ids = {}
    error_log = []

    def log_error(row_number, element_number, error_message):
        error_log.append(f"Row {row_number}\nElement {element_number}: {error_message}\n")

    for i, row in enumerate(data[1:]):
        row_number = i + 2

        # Validate Student ID
        student_id = row[0]
        if not student_id or not student_id.startswith("s") or len(student_id) != 7 or not student_id[1:3].isdigit() or not student_id[3:].isdigit():
            log_error(row_number, 1, "Student ID is missing or not valid")
        else:
            if student_id in student_ids:
                student_ids[student_id].append(row_number)
            else:
                student_ids[student_id] = [row_number]

        # Validates the name of the student
        name = row[1]
        name_parts = name.split()
        if not name or len(name_parts) < 2 or any(len(part) < 2 for part in name_parts):
            log_error(row_number, 2, "Name is empty or not valid")

        # Validates if the grades are on the 7-step-scale
        for j, grade in enumerate(row[2:], start=3):
            if grade is not None and grade not in allowed_integers:
                log_error(row_number, j, "is not a grade from the 7-step-grade list (-3,0,2,4,7,10,12)")

    # Check for duplicate student IDs, it locates the error of the student ID
    for student_id, row_numbers in student_ids.items():
        if len(row_numbers) > 1:
            error_message = f"The student ID is also used in row {', '.join(map(str, row_numbers))}"
            for row_number in row_numbers:
                log_error(row_number, 1, error_message)
    
    if not error_log:
        print("\nNo errors found.\n")
    else:
        print("\nThe following errors was found in the .csv-file:\n")
    # Print errors to the console
    for error in error_log:
        print(error)
        print("-----")



#################
# Test and debugging
#################
