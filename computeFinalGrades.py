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
from roundGrades import roundGrade as rG

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
        gradesFinal = rG(grades)
    elif len(grades[0]) > 1:
        grades = np.array(grades)
        Min = np.argmin(grades, axis=1)
        grades = np.array([np.delete(row, idx) for row, idx in zip(grades, Min)])
        grades = np.transpose(grades)
        grades = np.mean(grades, axis=0)
        gradesFinal = rG(grades)
    return gradesFinal

#################
# Test and debugging
#################
