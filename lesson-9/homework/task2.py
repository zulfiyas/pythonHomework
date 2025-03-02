import csv
import os

def create_grades_file(filename):
    """Creates grades.csv if it doesn't exist"""
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Subject", "Grade"])
            writer.writerow(["Alice", "Math", 85])
            writer.writerow(["Bob", "Science", 78])
            writer.writerow(["Carol", "Math", 92])
            writer.writerow(["Dave", "History", 74])

def read_grades(filename):
    """Reads the grades from a CSV file and returns a list of dictionaries."""
    grades = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])  
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    """Calculates the average grade for each subject."""
    subject_totals = {}
    subject_counts = {}
    
    for entry in grades:
        subject = entry['Subject']
        grade = entry['Grade']
        
        if subject in subject_totals:
            subject_totals[subject] += grade
            subject_counts[subject] += 1
        else:
            subject_totals[subject] = grade
            subject_counts[subject] = 1
    
    averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}
    return averages

def write_average_grades(filename, averages):
    """Writes the average grades to a new CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

grades_filename = "grades.csv"
averages_filename = "average_grades.csv"

create_grades_file(grades_filename) 
grades = read_grades(grades_filename)  
averages = calculate_average_grades(grades) 
write_average_grades(averages_filename, averages)  

print("Average grades saved to", averages_filename)
