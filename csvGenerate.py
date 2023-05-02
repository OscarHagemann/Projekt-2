# -*- coding: utf-8 -*-
"""
Created on Mon May  1 18:47:40 2023

@author: Morten Deurell - s206073
"""
import csv
import random
import time

# Extended lists of realistic Danish first and last names
first_names = [
    "Emil", "Frederik", "Magnus", "Oliver", "Oscar", "Sophia", "Emma", "Ida", "Clara", "Anna",
    "Liam", "Noah", "William", "Lucas", "Mason", "Ella", "Isabella", "Mia", "Emily", "Lily",
    "Benjamin", "Daniel", "Alexander", "Sebastian", "Victor", "Amelia", "Hannah", "Olivia", "Ava", "Sophie",
    "Jonas", "Mikkel", "Nikolaj", "Tobias", "Mathias", "Sara", "Naja", "Camilla", "Louise", "Maria",
    "Jacob", "David", "Elias", "Adam", "Simon", "Luna", "Lea", "Alma", "Viktoria", "Isabel",
]

last_names = [
    "Jensen", "Nielsen", "Hansen", "Pedersen", "Andersen", "Christensen", "Larsen", "Sørensen", "Rasmussen", "Jørgensen",
    "Madsen", "Kristensen", "Olsen", "Thomsen", "Møller", "Christiansen", "Poulsen", "Johansen", "Knudsen", "Mortensen",
    "Schmidt", "Lauridsen", "Vestergaard", "Jakobsen", "Petersen", "Iversen", "Bach", "Bertelsen", "Carstensen", "Dahl",
    "Eriksen", "Espersen", "Friis", "Gregersen", "Hermansen", "Hjorth", "Holm", "Kjeldsen", "Krogh", "Laursen",
]

def generate_student_id():
    # Generates a unique student ID with the format sXXYYYY
    return f"s{random.randint(19, 23)}{random.randint(1000, 9999)}"

def generate_realistic_danish_name():
    # Generates a realistic Danish name by combining a random first name and last name
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_grades(n, m):
    # Generates grades for n rows and m columns with a normal distribution
    grades = []
    allowed_integers = [-3, 0, 2, 4, 7, 10, 12]
    
    for _ in range(n):
        row = [random.choice(allowed_integers) if random.random() > 0.05 else "" for _ in range(m)]
        grades.append(row)
        
    return grades

def generate_csv(n, m):
    if not (20 <= n <= 1000) or not (5 <= m <= 40):
        raise ValueError("n and m should be between 5 and 100")

    filename = f"GradesStudents_{int(time.time())}.csv"
    headers = ["StudentID", "Name"] + [f"Assignment{i}" for i in range(1, m - 1)]  # Updated to m - 1 columns
    
    
    student_ids = set()
    names = set()
    rows = []
    
    for _ in range(n):
        student_id = generate_student_id()
        while student_id in student_ids:
            student_id = generate_student_id()
        
        name = generate_realistic_danish_name()
        while name in names:
            name = generate_realistic_danish_name()

        student_ids.add(student_id)
        names.add(name)

        rows.append([student_id, name] + generate_grades(1, m - 2)[0])

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

if __name__ == "__main__":
    n = random.randint(20, 1000)  # Number of rows (between 5 and 100)
    m = random.randint(5, 40)  # Number of columns (between 5 and 100)
    generate_csv(n, m) 