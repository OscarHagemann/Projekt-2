#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DATALOAD FUNCTION
Created on Mon May 1 18:59:57 2023
This code was written by group 17
Morten Deurell - s206073
Oscar Max Hagemann - s214356
Tobias Canger Lund - s214365  
"""
#################
# Imports
# Various imported packages and function scripts.
#################
import csv
from cleanData import cleanData


#################
# dataLoad function
# Loads the chosen datafile (.csv) with student grades. filename is the path to the file
# Returns N x M array containing the rows and columns from the .csv-file
#################
def dataLoad(filename):

    # Open the .csv-file for reading with utf-8 encoding
    with open(filename, 'r', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        
# Read rows from the CSV file and store them in the data list using a nested list comprehension
        data = [row for row in reader]

 # Convert numeric values in columns 3 to m and rows 2 to n to float
    for i in range(1, len(data)):
        for j in range(2, len(data[i])):
            if data[i][j]:
                data[i][j] = int(data[i][j])

    # Returns the N x M array containing the data from the .csv-file
    return data


#################
# Test and debugging
# Should be commented out when not used
#################

filename = "GradesStudents_1682975120.csv" 
data = dataLoad(filename)
#for row in data:
    #formatted_row = [str(x) if not isinstance(x, float) else f"{x:.1f}" for x in row]
    #print(", ".join(formatted_row))

#cleaned_data = cleanData(data)
#print(cleaned_data)