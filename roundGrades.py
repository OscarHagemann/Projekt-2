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

# The function takes an array of grades as input and returns a new array with the grades rounded to the nearest grade on the 7-step-scale
# The function works by using a series of if and elif statements to determine which grade on the 7-step-scale is closest to each input grade
def roundGrade(grades):
    gradesRounded = [] 
    for i in grades:
        if i >= 11.0:
            gradesRounded.append(12)
        elif i >= 8.5 and i < 11.0:
            gradesRounded.append(10)
        elif i >= 5.5 and i < 8.5:
            gradesRounded.append(7)
        elif i >= 3.0 and i < 5.5:
            gradesRounded.append(4)
        elif i >= 1.0 and i < 3.0:
            gradesRounded.append(2)
        elif i >= -1.5 and i < 1.0:
            gradesRounded.append(0)
        elif i >= -3.0 and i < -1.5:
            gradesRounded.append(-3)
    return gradesRounded

#################
# Test and debugging
# Should be commented out when not used
#################

#print(roundGrade([10.5,3.4, 4.6, 10.3, 0.3, 9.5, 11.1, 8.9, 9.4, -0.2, 2.7, -2.9, -2.9])) 