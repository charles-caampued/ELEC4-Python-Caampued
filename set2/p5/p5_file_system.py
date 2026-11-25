# Charles Caampued | IV-BSIT-A | P5 | 11-21-2026

import csv
from pathlib import Path

DATA = Path(__file__).with_name("students.txt")


def load():
    try:
        with open(DATA, newline="", encoding="utf-8") as source:
            return [row for row in csv.reader(source) if len(row) == 4]
    except FileNotFoundError:
        return []


def save(records):
    temporary = DATA.with_suffix(".tmp")
    with open(temporary, "w", newline="", encoding="utf-8") as target:
        csv.writer(target).writerows(records)
    temporary.replace(DATA)


def field(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required.")


def details(student_id):
    name = field("Full name: ")
    section = field("Course/section: ")
    while True:
        try:
            average = float(input("General average: "))
            if 0 <= average <= 100:
                return [student_id, name, section, str(average)]
        except ValueError:
            pass
        print("Enter a number from 0 to 100.")


def find(records, student_id):
    for record in records:
        if record[0].casefold() == student_id.casefold():
            return record
    return None


records = load()
while True:
    choice = input("1 Add | 2 Display | 3 Search | 4 Update | 5 Exit: ")
    if choice == "5":
        break
    if choice == "2":
        print("ID | Full name | Course/section | General average")
        for record in records:
            print(" | ".join(record))
        print("Total:", len(records))
        continue
    if choice not in ("1", "3", "4"):
        print("Invalid menu choice.")
        continue

    student_id = field("Student ID: ")
    record = find(records, student_id)
    if choice == "1" and record:
        print("ID already exists.")
    elif choice == "1":
        records.append(details(student_id))
        save(records)
        print("Student saved.")
    elif record is None:
        print("ID not found.")
    elif choice == "3":
        print(" | ".join(record))
    else:
        records[records.index(record)] = details(record[0])
        save(records)
        print("Student updated.")
