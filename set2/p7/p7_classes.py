# Charles Caampued | IV-BSIT-A | P7 | 11-21-2026

class Subject:
    def __init__(self, title):
        self.title = title


class Student:
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, value):
        grade = float(value)
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be from 0 to 100.")
        self.__grade = grade

    def update_info(self, name=None, subject=None):
        if name:
            self.name = name
        if subject:
            self.subject = subject

    def display(self):
        print(f"{self.name} | {self.subject.title} | {self.get_grade():g}")


class Section:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def display(self):
        print("Section:", self.name)
        for student in self.students:
            student.display()


subject = Subject("Python Programming")
node_subject = Subject("Node.js")
students = [Student("Inday Kalamansi", subject, 85), Student("Dodong Lechon", subject, 90),
            Student("Kikay Ensaymada", subject, 88)]
section = Section("IV-BSIT-A", students)
print("Before update:")
students[0].display()
try:
    students[0].set_grade(110)
except ValueError as error:
    print("Update rejected:", error)
students[0].set_grade(92)
students[0].update_info(name="Inday K. Kalamansi", subject=node_subject)
print("After updating Inday:")
section.display()
