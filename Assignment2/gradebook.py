# Name: Manas Aggarwal
# Roll NO.: 2501730302
# Date: 23 Nov, 2025
# Title: GradeBook Analyzer
# ------------------------------------------------------
print("==================================================")
print("          Welcome to GradeBook Analyzer          ")          
print("==================================================")

print("Choose an option:")
print("1. Manual input of student marks")
print("2. Load marks from a CSV file")

import csv

def input_marks_manual():
    data = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Student name: ")
        mark = float(input("Mark: "))
        data[name] = mark
    return data

def input_marks_csv(filepath):
    data = {}
    with open(filepath, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            name, mark = row
            data[name] = float(mark)
    return data

choice = input("Enter your choice (1 or 2): ")
if choice == "1":
    marks = input_marks_manual()
elif choice == "2":
    path = input("Enter CSV file path: ")
    marks = input_marks_csv(path)
else:
    print("Invalid choice.")
    exit()

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    mid = n // 2
    if n % 2 == 0:
        return (scores[mid-1] + scores[mid]) / 2
    else:
        return scores[mid]

def find_max(marks):
    return max(marks.values())

def find_min(marks):
    return min(marks.values())

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = 'A'
        elif score >= 80:
            grades[name] = 'B'
        elif score >= 70:
            grades[name] = 'C'
        elif score >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades

def grade_distribution(grades):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades.values():
        dist[grade] += 1
    return dist

passed_students = [name for name, score in marks.items() if score >= 40]
failed_students = [name for name, score in marks.items() if score < 40]
print(f"Passed: {len(passed_students)} {passed_students}")
print(f"Failed: {len(failed_students)} {failed_students}")

def display_results(marks, grades):
    print(f"{'Name':<10}{'Marks':<10}{'Grade'}")
    print("-" * 30)
    for name in marks:
        print(f"{name:<10}{marks[name]:<10}{grades[name]}")

while True:
    display_results(marks, assign_grades(marks))
    again = input("Run analysis again? (y/n): ")
    if again.lower() != 'y':
        break


