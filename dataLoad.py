#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DATALOAD FUNCTION
Created on Mon May 1 18:59:57 2023
    Morten Deurell  - s206073
Workload equally distributed.  

    Reads a CSV file and returns an N x M array containing the data.

    Argumentss:
        filename (str): The relative path to the CSV file.

    Returns:
        data (list of lists): An N x M array containing the rows and columns from the CSV file.
    """
#################
#imports
#################
import csv

#################
# dataLoad function
# Loads the chosen datafile (.csv) with student grades
#################
def dataLoad(filename):

    # Open the CSV file for reading with utf-8 encoding
    with open(filename, 'r', encoding='utf-8') as csvfile:
        # Create a CSV reader object
        reader = csv.reader(csvfile)
        
        # Read rows from the CSV file and store them in the data list using a list comprehension
        data = [row for row in reader]

    # Return the N x M array containing the data
    return data