# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:03:02 2023
his code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""
#################
# Functions
#################
# Grade rounding function
# This function rounds the grade to the nearest grade on the 7-step-scale
def roundGrade(grades):
    gradesRounded = []
    
    for grade in grades:
        if grade == None:
            gradesRounded.append(None)
        else:
            if grade >= 11.0:
                gradesRounded.append(12)
            elif grade >= 8.5 and grade < 11.0:
                gradesRounded.append(10)
            elif grade >= 5.5 and grade < 8.5:
                gradesRounded.append(7)
            elif grade >= 3.0 and grade < 5.5:
                gradesRounded.append(4)
            elif grade >= 1.0 and grade < 3.0:
                gradesRounded.append(2)
            elif grade >= -1.5 and grade < 1.0:
                gradesRounded.append(0)
            elif grade >= -3.0 and grade < -1.5:
                gradesRounded.append(-3)
    return gradesRounded

#################
# Test and debugging
# Should be commented out when not used
#################

print(roundGrade([None, 10.5,3.4, 4.6, 10.3, 0.3, 9.5, 11.1, 8.9, 9.4, -0.2, 2.7, -2.9, -2.9])) 