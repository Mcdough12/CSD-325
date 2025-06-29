"""
CSD-325 – Module 8: JSON Practice
Author: Reed Bunnell
"""

import json

# Define the JSON file path (same folder as script)
json_file = "student.json"

def print_students(students, title):
    """Print formatted student list with a title."""
    print(f"\n{title}")
    print("-" * len(title))
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

# --- Main Program ---
def main():
    # Load JSON data
    with open(json_file, "r", encoding="utf-8") as file:
        students = json.load(file)

    # Notify and print original list
    print("\n[INFO] Original student list loaded from file.")
    print_students(students, "Original Student List")

    # Append your own fictional student
    my_student = {
        "F_Name": "Reed",
        "L_Name": "Bunnell",
        "Student_ID": 99999,
        "Email": "rbunnell@example.com"
    }
    students.append(my_student)

    # Notify and print updated list
    print("\n[INFO] Your student record has been added.")
    print_students(students, "Updated Student List")

    # Save back to file using dump()
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    print("\n[INFO] student.json has been updated successfully.")

# Run the main function
if __name__ == "__main__":
    main()
