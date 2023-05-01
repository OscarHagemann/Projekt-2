#02631 Introduction to programming and data processing
#Project 2 - Program for grading students
"""
This code was written by group 17
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""


#################
#imports
#################
#various imported packages and function scripts.
import numpy as np
import matplotlib.pyplot as plt
from dataLoad import data


#################
#functions
#################
def dataLoad(filename):
    #This function reads the data from the file
    filename = open('GradesStudents.csv', 'r')
    grades = np.loadtxt(filename, delimiter = ' ')

grades = dataLoad('GradesStudents.csv')

#Grade rounding function
def roundGrade(grades):
    gradesRounded = []
    #This function rounds the grade to the nearest grade on the 7-step-scale
    for grade in grades:
        if grade >= 11.5:
            gradesRounded.append(12)
        elif grade >= 9.5:
            gradesRounded.append(10)
        elif grade >= 6.5:
            gradesRounded.append(7)
        elif grade >= 3.5:
            gradesRounded.append(4)
        elif grade >= 1.5:
            gradesRounded.append(2)
        elif grade >= -0.5:
            gradesRounded.append(0)
        else:
            gradesRounded.append(-3)
    return gradesRounded

#Function that computes the final grade
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

#Plot function of the grades
def gradesPlot(grades):
    #Setting up the whole matrix as a numpy array
    AllAss = np.array(grades)
    #Getting the amount of coloumns required
    Coloumns = len(AllAss[0])
    #Setting up the plot
    fig, ax = plt.subplots()
    Mean = np.mean(AllAss, axis=0)
    x_mean = np.arange(Coloumns)
    ax.plot(x_mean, Mean, label='Mean', color='black')
    #This adds a random value of anywhere between -0.2 and 0.2 to the existing matrix
    #The assignemnt did say between -0.1 and 0.1, but that didn't help with the visibility, so we decided to increase the interval
    Random = np.random.uniform(-0.2, 0.2, size=AllAss.shape)
    AllAss = AllAss + Random
    #This loop makes the x-axis as long as the number of assignments and inputs all the values of each coloumn in there corresponding x value
    for i in range(Coloumns):
        x = [i] * len(AllAss)
        y = [row[i] for row in AllAss]
        ax.plot(x, y, 'o', label=f'Assignment {i+1}')

    ax.set_xlabel('Assignments')
    ax.set_ylabel('Grades')

    ax.legend()
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
    plt.bar(courses, values, width = 0.3)
    plt.title('Grades')
    
  
#Main script fra sidste projekt
"""

#Getting user input
def userInput(type, min, max, text): 
    number = 0
    while(True):
        try:
            # Handle input depending on input type
            if type == 0:
                number = int(input(text))
            elif type == 1:
                number = float(input(text))
            if number < min or number > max:
                raise ValueError()
            break
        except ValueError:
            print("\nInvalid value selected! Please try again")
    return number

#This function filters data based on the state of the filter
def filterData(data, filterState):
    filteredNames = np.array([1,2,3,4])
    # The data is filtered by the bacterias name and the growth rate range
    name = np.isin(data[:, 2], filteredNames[filterState[0:4].astype('bool')])
    growth = (data[:, 1] < filterState[5]) & (data[:, 1] > filterState[4])
    return data[growth * name]

#When the state is set to 1 it avoids that the script can be used without loading a file first 
state = 1
#This array is holding the data
data = np.array([])
#This array is holding the filtered data
filteredData = np.array([]).astype(bool)
#This array is indicating the state of the filter
filterState = np.array([True, True, True, True, -math.inf, math.inf])


while True:
    #User input for main menu
    if state == 0 :
        print("\n")
        state = userInput(0, 1, 5, "Please select one of the following options\n1: Load data\n2: Filter data\n3: Display statistics\n4: Generate plots\n5: Quit\n\nYour input: ")
    
    #Loading the file specified by the user
    if state == 1 :
        print("\n")
        while True:
            try:
                data = dataLoad(input("Input filename of data file: \nYour input: "))
                filteredData = np.copy(data)
                print("\nFile was loaded succesfully")
                break
            except Exception:
                print("\nInvalid file or path!")
        #When state = 0, the script returns to the main menu
        state = 0
    
    #User input for filter menu    
    elif state == 2:
        print("\n")
        # Getting user input for the filter
        menu = userInput(0, 1, 4, "Select from following filter options\n1: Filter bacteria type\n2: Growth rate range\n3: Clear all filters\n4: Main Menu\n\nYour input: ")
        if menu == 1:
            while(True):
                print("\n")
                #This function displays the filter status for each type of bacteria marked with X
                X = np.array([" ", " ", " ", " "])
                for i in range(4):
                    if filterState[i]:
                        X[i] = "X"
    
                #User input is needed to select which type bacteria to filter from data
                filterToggle = userInput(0, 1, 5, f"Select which type to filter from data\n1: Salmonella enterica\t[{X[0]}]\n2: Bacillus cereus  \t[{X[1]}]\n3: Listeria   \t[{X[2]}]\n4: Brochothrix thermosphacta\t[{X[3]}]\n5: Filter Menu\n\nYour input: ")
    
                if filterToggle == 5:
                    break
                #Toggle the filter status of the selected type of bacteria
                filterState[filterToggle - 1] = not filterState[filterToggle - 1]
        
        #Setting the range of the growth rate for filtering the data
        elif menu == 2:
            print("\n")
            filterState[4] = userInput(1, -math.inf, math.inf, f"Insert min growth rate\n\nYour input: ")
            print("\n")
            filterState[5] = userInput(1, filterState[4], math.inf, f"Insert max growth rate\n\nYour input: ")
            print(f"Selected Growth rate range: {filterState[4]} - {filterState[5]}")
            #Clearing of all the filters
        elif menu == 3:
            filterState = np.array([True, True, True, True, -math.inf, math.inf])
            print("The filters were cleared")
            #Apply the current state of the filter to the data and return to main menu
        elif menu == 4:
            filteredData = filterData(data, filterState)
            print("You returned to the main menu")
            state = 0
        
        
        
    elif state == 3:
        print("\n")
        #Getting user input for statistics
        menu = userInput(0, 1, 8, "Select from following statistical options\n1: Mean Temperature\n2: Mean Growth rate\n3: Std Temperature\n4: Std Growth rate\n5: Rows\n6: Mean Cold Growth rate\n7: Mean Hot Growth rate\n8: Main Menu\n\nYour input: ")
        statistic = np.array(["Mean Temperature", "Mean Growth rate", "Std Temperature", "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"])
        if menu == 8:
            #Return to the main menu if 8 is selected by the user
            state = 0
            continue
    
        try:
            print(f"The {statistic[menu - 1]} is: {dataStatistics(filteredData, statistic[menu - 1])}")
        except Exception:
            print("Unable to compute selected statistics because of applied filters or empty file")
        
    #Plotting of the data    
    elif state == 4:
        gradesPlot(filteredData)
        print("\nPlot was succesfully generated")
        state = 0
        
    #Quit the program
    elif state == 5:
        print("See you soon!")
        break
        """