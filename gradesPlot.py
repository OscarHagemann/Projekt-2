# -*- coding: utf-8 -*-
"""
gradesPlot
Created on Mon April 25 17:03:02 2023
his code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""
#################
# Imports
# Various imported packages and function scripts.
#################
import numpy as np
import matplotlib.pyplot as plt
from computeFinalGrades import computeFinalGrades

#################
# Functions
#################
# This function computes the grade plots
# This function rounds the grade to the nearest grade on the 7-step-scale

def gradesPlot(grades):
    #Setting up the whole matrix as a numpy array
    AllAss = np.array(grades)
    
    #Getting the amount of coloumns required
    Coloumns = len(AllAss[0])
    
    #Setting up the plot
    fig, ax = plt.subplots()
    Mean = np.mean(AllAss, axis=0)
    x_mean = (np.arange(Coloumns)+1)
    ax.plot(x_mean, Mean, label='Mean', color='black')
    
    #This adds a random value of anywhere between -0.1 and 0.1 to the existing matrix
    Random = np.random.uniform(-0.1, 0.1, size=AllAss.shape)
    AllAss = AllAss + Random
    
    #This loop makes the x-axis as long as the number of assignments, and inputs all the values of each coloumn in their corresponding x value
    for i in range(Coloumns):
        x = [(i + 1 + np.random.uniform(-0.1, 0.1)) for _ in range(len(AllAss))]
        y = [row[i] + np.random.uniform(-0.1, 0.1) for row in AllAss]
        ax.plot(x, y, '.', markersize=1)

    ax.set_xlabel('Assignments')
    ax.set_ylabel('Grades')

    ax.legend()
    
    x_labels = list(range(1,Coloumns+1))
    plt.xticks(x_labels)
    plt.show()

    grades = computeFinalGrades(grades)
    Min_3 = 0
    Zero = 0
    Two = 0
    Four = 0
    Seven = 0
    Ten = 0
    Twelfe = 0
    i = 0
    while i < len(grades):
        if grades[i] == -3:
            Min_3 = Min_3 + 1
        elif grades[i] == 0:
            Zero = Zero + 1
        elif grades[i] == 2:
            Two = Two + 1
        elif grades[i] == 4:
            Four = Four + 1
        elif grades[i] == 7:
            Seven = Seven + 1
        elif grades[i] == 10:
            Ten = Ten + 1
        else:
            Twelfe = Twelfe + 1
        i = i + 1
    barData = {'-3': Min_3, '00': Zero, '02': Two, '4': Four, '7': Seven, '10': Ten, '12': Twelfe}
    courses = list(barData.keys())
    values = list(barData.values())
    plt.bar(courses, values, width = 0.3, color = 'red')
    plt.title('Grades')
#################
# Test and debugging
# Should be commented out when not used
#################
