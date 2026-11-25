# Charles Caampued | IV-BSIT-A | P8 | 11-21-2026

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, age {self.age}."


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def introduce(self):
        return f"{super().introduce()} I study in {self.section}."


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"{super().introduce()} I teach {self.subject}."


people = [Person("Aling Nena", 52), Student("Kikoy Pandesal", 21, "IV-BSIT-A"),
          Teacher("Sir Pidoy Tinola", 40, "Python Programming")]
for person in people:
    print(person.introduce())

# Student and Teacher inherit the common name and age setup from Person.
# Each child overrides introduce to include a detail about its own role.
# The loop makes the same method call on every object.
# Python selects the method for that object's class, demonstrating polymorphism.
