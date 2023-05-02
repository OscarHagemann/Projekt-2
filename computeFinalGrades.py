# -*- coding: utf-8 -*-
"""
Created on Mon April 25 19:42:41 2023
This code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365 
"""
#################
# Imports
#################
import numpy as np
from roundGrades import roundGrade

#################
# Functions
#################

def computeFinalGrades(grades):
    gradesFinal = [None]*len(grades)
    for i in range(len(grades)):
        if -3 in grades[i]:
            grades[i] = [-3] * len(grades[i])
    if len(grades[0]) == 1:
        grades = [item for sublist in grades for item in sublist]
        gradesFinal = roundGrade(grades)
    elif len(grades[0]) > 1:
        grades = np.array(grades)
        Min = np.argmin(grades, axis=1)
        grades = np.array([np.delete(row, idx) for row, idx in zip(grades, Min)])
        grades = np.transpose(grades)
        grades = np.mean(grades, axis=0)
        gradesFinal = roundGrade(grades)
    return gradesFinal     
            
            



#################
# Test and debugging
#################

array = [[4, 2, 0, 12, 7, 10, 0, 7, 12, 12, 7, 10, -3, 2], [0, -3, -3, -3, 2, 12, 10, 4, 12, 7, 7, 7, 12, 4], [4, 10, 2, 12, 12, 2, 7, 10, 12, 7, 10, 10, 10, 2], [0, 7, 12, 10, 4, 4, 0, 12, 12, 0, 10, 12, 12, 12], [0, -3, 4, 12, 12, 4, 0, 0, 0, 10, 2, 4, 12, 2], [4, 0, 4, 2, 2, 0, 12, 4, 0, 7, -3, 12, 7, 7], [2, 7, -3, 0, 4, 4, 7, 0, 7, 2, 2, 10, 0, 12], [2, 12, 2, 4, 7, 10, 7, 10, 4, 4, 12, 12, 2, -3], [4, 12, -3, 12, 4, 2, 10, 0, 10, -3, 7, -3, 2, -3], [2, 12, 7, 7, 2, -3, 0, 4, 10, -3, 10, 2, -3, 0], [10, 10, 12, 0, 0, 10, 4, 7, 0, 7, 10, 10, 2, 10], [2, 4, 12, 12, 10, 10, -3, -3, 4, -3, 10, -3, 7, -3], [-3, 2, 7, 2, 2, 12, 10, -3, 0, 4, 2, 2, 2, 10], [2, 10, 4, 2, 10, 0, 7, 4, -3, 7, 0, 7, 0, 0], [7, 12, 0, 10, 2, 0, -3, 4, -3, 2, 12, 7, 12, -3], [-3, 7, 10, 10, 12, 0, 10, 7, 2, 4, 12, 7, 0, 12], [4, 2, 2, -3, 2, 12, 0, 4, 0, 7, 2, 0, -3, -3], [4, 12, 10, -3, 2, -3, 10, 4, 4, 4, 12, 4, 12, 10], [12, 2, -3, 7, -3, 10, 2, -3, 4, -3, -3, -3, 10, 12], [-3, -3, 0, 2, 2, 0, 2, 10, 10, 12, 7, -3, 2, 10], [0, 2, 0, 4, 4, 4, 7, 10, 2, -3, 7, -3, 4, -3], [10, -3, -3, 4, 0, 7, 7, 0, -3, 0, -3, 12, 10, 4], [4, 0, 7, 12, 12, 0, 12, 12, 0, 12, 12, 12, 4, 4], [2, 7, 2, 10, 10, 0, 2, 4, 10, 10, 12, 7, 2, 10], [10, 10, 2, 10, 0, 12, -3, 4, 12, 7, 0, 10, 4, 12]]
print(computeFinalGrades(array))