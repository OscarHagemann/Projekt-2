import numpy as np

def computeFinalGrades(grades):
# Insert your code here
    gradesFinal = [None]*len(grades)
    for i in range(len(grades)):
        if -3 in grades[i]:
            grades[i] = [-3] * len(grades[i])
    if len(grades[0]) == 1:
        gradesFinal = [item for sublist in grades for item in sublist]  
    elif len(grades[0]) > 1:
        grades = np.array(grades)
        Min = np.argmin(grades, axis=1)
        #grades = np.delete(grades, Min, axis = 1)
        grades = np.array([np.delete(row, idx) for row, idx in zip(grades, Min)])
        grades = np.transpose(grades)
        gradesFinal = np.mean(grades, axis=0)
    return gradesFinal
