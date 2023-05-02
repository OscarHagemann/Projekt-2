#02631 Introduction to programming and data processing
#Project 2 - Program for grading students
"""
MAINSCRIPT
This code was written by group 17
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365
"""

#################
# Imports
# Various imported packages and function scripts.
#################
from dataLoad import dataLoad
from Errorlog import validate_data
from cleanData import cleanData
from generic_functions import textcolor
from gradesPlot import gradesPlot

# Menu dictionairy
#################
# Menu
#################
menu = {
    "1": "Load New Data",
    "2": "Check Data for Errors",
    "3": "Generate Diagrams",
    "4": "Show List of Grades",
    "H": "Help",
    "Q": "Quit"
}

#################
# Predefined Variables
#################
filepath    = ""    # Initiates the filepath as empty.

#################
# Main Script
#################
#Noter mangler
while True:
# main menu display + prompt
# if no data is loaded, only the load and quit options will be shown.
# if data is loaded, the additional options will be visible

    if ('isLoaded' not in globals()):
        print(textcolor("\nMAIN MENU:\n","orange"))
        for key, value in menu.items():
            if key in ["1", "H", "Q"]:
                print(f"{key}. {value}")      
        choice = input("\nEnter 1. or select 'Q' to quit:")
    else: 
        print(textcolor("\nMAIN MENU:","orange"))
        for key, value in menu.items():
            print(f"{key}. {value}")      
        choice = input("\nEnter your choice (1-4) or select 'Q' to quit: ")

# main menu validation
# if the selected option is not included in the menu, the program returns an error message and gives the user 
# the possibility to choose again  

    if choice not in menu:
        print(textcolor("\nInvalid choice. Please enter a menu choice.\n","red"))
        continue

    # set variable of menu choice
    selected_option = menu[choice]

# main menu - Quit.    
# if the user can choose the "quit" option, the program stops running

    if selected_option == "Quit":
        print("Program has been terminated..")
        break
    else:
        # If menu point 1-4 is selected the chosen option is shown.      
        print(textcolor("\nCurrent section:","orange") + f"  {selected_option}\n")
        
# main menu - Load new data
# prompt the user for the path to .csvfile. 
# if filepath is valid, load data and set isLoaded variable. If not, show error message to user. 

        if selected_option == "Load New Data": 
            while True:
                filepath = input("Please, enter the path of the .csv-file that you want to load or enter 'B' to return to MAIN MENU: ")

                if filepath == 'B' or filepath == 'b':
                        break
                else:
                    try: 
                        data = dataLoad(filepath)
                        isLoaded=True
                        break
                    except:
                        print(filepath, "\n Not found, please check the spelling of your file path/file name or enter 'B' to return to MAIN MENU: ")

# main menu - Check Data for Errors    
# Returns a full error report from the dataset.
 
        elif selected_option == "Check Data for Errors":
            validate_data(data)
            
# main menu - Generate Diagrams
# Show plots/diagrams

        elif selected_option == "Generate Diagrams":
            print("\nPlots are shown in the plot window. Any faulty lines will have been removed.\nIf you want to check the .csv-file for errors please choose menu item 2 in the MAIN MENU")
            cleaned_data = cleanData(data)
            gradesPlot(cleaned_data)
            
                                   
# main menu - Show List of grades
# Shows the list of grades as plots.

        elif selected_option == "Show List of grades":
            print("Endnu ikke lavet")                

# main menu - Help
        elif selected_option == "Help":
            print("********************HELP********************")
            print("")
            print("File:")
            print("This program relies on data being uploaded. Fileformat must be \".csv\".")
            print("The data must be seperated by a comma (,). Grades must be integers or floats between -3 and 12:")
            print("")
            print("Check Data for Errors:")
            print("Returns a full error report.")
            print("")
            print("Generate Diagramss:")
            print("Generates a histogram over with the grades on the x-axis and the y-axis represents the number of students with the corresponding average grade.")                      
            print("")
            print("Show List of Grades:")
            print("Creates the final list of grades for each student.")
            print("")
            print("Help:")
            print("Shows this menu.") 
            print("")
            print("Quit:")
            print("Terminates program. Data must be reloaded upon restart.")     
            print("")
            print("********************************************")
            print("")
        
        