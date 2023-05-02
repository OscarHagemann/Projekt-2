"""
GENERIC FUNCTIONS
Created on Mon May 1 18:59:57 2023
This code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365  
"""

# This function is coloring for the main script
def textcolor(str,colr):
    if colr == "orange":
        colored_string = "\033[38;2;255;165;0m" + str + "\033[0m"
    elif colr == "red":
        colored_string = "\033[1;31m" + str + "\033[0m"
    elif colr == "green":
        colored_string = "\033[1;32m" + str + "\033[0m"
    return colored_string