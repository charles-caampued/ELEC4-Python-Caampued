# Charles Caampued | IV-BSIT-A | P2 | 11-21-2026

from datetime import datetime

import student_utils
from student_utils import highest, lowest

grades = []
while True:
    entry = input("Grade (Enter to print report): ").strip()
    if not entry and grades:
        break
    try:
        grade = float(entry)
        if 0 <= grade <= 100:
            grades.append(grade)
            continue
    except ValueError:
        pass
    print("Enter a number from 0 to 100.")

print("Grade report generated", datetime.now().strftime("%Y-%m-%d %H:%M"))
print(f"Average: {student_utils.average(grades):.2f}")
print("Result:", student_utils.pass_fail(grades))
print(f"Highest: {highest(grades):g} | Lowest: {lowest(grades):g}")
