# -*- coding: utf-8 -*-
"""
GRADE LIST FUNCTION
Created on Mon May 1 18:59:57 2023
This code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365  
"""
#################
# Imports
#################
from cleanData import cleanData
from computeFinalGrades import computeFinalGrades
from dataLoad import dataLoad
#################
# Functions
#################
def gradeList(data):
    # Add a new column called "Final Grade"
  
    # Create a cleaned_data array from cleanData(data)
    cleaned_data = cleanData(data)

    # Compute finalGrades using the cleaned_data
    finalGrades = computeFinalGrades(cleaned_data)

    for row in data:
        row.append(None)
    data[0][-1] = "Final Grade"


    # Substitute cleaned_data values back into the original data array
    for i, row in enumerate(cleaned_data):
        for j, value in enumerate(row[2:]):
            data[i+1][j+2] = value

    # Fill the "Final Grade" column with finalGrades
    for i, grade in enumerate(finalGrades):
        data[i+1][-1] = grade
     
    # Rearrange the whole dataset alphabetically by Student name
    data[1:] = sorted(data[1:], key=lambda row: row[1])
    
    # Replace "Assignment" with "A" in the first row
    data[0] = [elem.replace("Assignment", "A") if "Assignment" in elem else elem for elem in data[0]]
    return data

    

#################
# Test and debugging
#################
# Load the data using the dataLoad function
filename = "GradesStudents_1683045916.csv" 
data = dataLoad(filename)

# Call the gradeList function
modified_data = gradeList(data)

#Print the dataset as a table
student_id_width = 15
name_width = 20
#print(modified_data)
for row in modified_data:
    formatted_row = [str(row[0]).ljust(student_id_width), row[1].ljust(name_width)] + [str(elem) for elem in row[2:]]
    print("\t".join(formatted_row))