# gradebook.py
# Name: [Your Name]
# Date: 27 Oct 2025
# Title: GradeBook Analyzer

import csv
import statistics

def print_welcome():
    print("\n==== Welcome to GradeBook Analyzer ====")
    print("Choose input mode:")
    print("1. Manual Entry")
    print("2. CSV Import\n")

def manual_entry():
    data = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Student {i+1} Name: ")
        marks = float(input(f"{name}'s Marks: "))
        data[name] = marks
    return data

def csv_entry(filename):
    data = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if present
        for row in reader:
            if len(row) >= 2:
                name = row[0]
                try:
                    marks = float(row[1])
                    data[name] = marks
                except ValueError:
                    print(f"Invalid marks for {name}: {row[1]}, skipping.")
    return data

def calculate_average(marks_dict):
    return round(sum(marks_dict.values())/len(marks_dict), 2)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    max_student = max(marks_dict, key=marks_dict.get)
    return max_student, marks_dict[max_student]

def find_min_score(marks_dict):
    min_student = min(marks_dict, key=marks_dict.get)
    return min_student, marks_dict[min_student]

def assign_grades(marks_dict):
    grades_dict = {}
    for name, marks in marks_dict.items():
        if marks >= 90:
            grades_dict[name] = 'A'
        elif marks >= 80:
            grades_dict[name] = 'B'
        elif marks >= 70:
            grades_dict[name] = 'C'
        elif marks >= 60:
            grades_dict[name] = 'D'
        else:
            grades_dict[name] = 'F'
    return grades_dict

def grade_distribution(grades_dict):
    dist = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0}
    for grade in grades_dict.values():
        dist[grade] += 1
    return dist

def pass_fail_lists(marks_dict):
    passed_students = [name for name, marks in marks_dict.items() if marks >= 40]
    failed_students = [name for name, marks in marks_dict.items() if marks < 40]
    return passed_students, failed_students

def print_results_table(marks_dict, grades_dict):
    print("\nName\tMarks\tGrade")
    print("-----------------------------")
    for name, marks in marks_dict.items():
        print(f"{name}\t{marks}\t{grades_dict[name]}")

def main():
    while True:
        print_welcome()
        choice = input("Enter 1 for Manual, 2 for CSV, q to quit: ")
        if choice == '1':
            marks_dict = manual_entry()
        elif choice == '2':
            filename = input("Enter CSV filename: ")
            marks_dict = csv_entry(filename)
        elif choice.lower() == 'q':
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        average = calculate_average(marks_dict)
        median = calculate_median(marks_dict)
        max_student, max_score = find_max_score(marks_dict)
        min_student, min_score = find_min_score(marks_dict)
        grades_dict = assign_grades(marks_dict)
        dist = grade_distribution(grades_dict)
        passed_students, failed_students = pass_fail_lists(marks_dict)

        print("\n--- Analysis Summary ---")
        print(f"Average marks: {average}")
        print(f"Median marks: {median}")
        print(f"Top student: {max_student} with {max_score}")
        print(f"Lowest student: {min_student} with {min_score}")
        print("\nGrade Distribution:")
        for grade, count in dist.items():
            print(f"{grade}: {count}")
        print(f"\nPassed: {len(passed_students)} ({', '.join(passed_students)})")
        print(f"Failed: {len(failed_students)} ({', '.join(failed_students)})")

        print_results_table(marks_dict, grades_dict)

        again = input("\nRun another analysis? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using GradeBook Analyzer.")
            break

if __name__ == "__main__":
    main()