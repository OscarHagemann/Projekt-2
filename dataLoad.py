#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DATALOAD FUNCTION
Created on Mon May 1 18:59:57 2023
    Morten Deurell  - s206073
Workload equally distributed.  

This function loads the data from the txt file as a numpy array called raw_data
    check if errors are present, if so outputs the type of error and the line 
    in the console, then returns a numpy array clean_data containing only the 
    lines without errors
"""
#################
#imports
#################
import numpy as np

#################
# dataLoad function
# Loads the chosen datafile (.csv) with student grades
#################
def dataLoad(filename):
    
    # loading the data 
    raw_data = np.loadtxt(filename)
    
    
    # initializing the array for the clean data
    clean_data = []

    # checking the data, outputting error messages/lines removed, and filling clean_data
    print("")
    for i, row in enumerate(raw_data):
        
        # check on temperature 
        if row[0]<10 or row[0]>60:
            print(f"Line {i}: Temperature out of range.")
            counter+=1
        
        #check on growth rate
        elif row[1] < 0:
            print(f"Line {i}: Negative growth-rate.")
            counter+=1
        
        # check on bacteria variant 
        elif row[2] not in bacteriaVariant:
            print(f"Line {i}: Bacteria variant out of range.")
            counter+=1
        
        else:
            clean_data.append(raw_data[i, :])
            
    clean_data = np.asarray(clean_data)
    print(counter, f"faulty lines have been deleted from the loaded dataset of {(i+1)} lines.")
    print("")
    return clean_data


    