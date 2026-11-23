# Charles Caampued | IV-BSIT-A | P1 | 11-21-2026

PASS_MARK = 75


def collect_grades():
    grades = []
    while True:
        entry = input("Grade (Enter to finish): ").strip()
        if not entry and grades:
            return grades
        try:
            grade = float(entry)
            if 0 <= grade <= 100:
                grades.append(grade)
                continue
        except ValueError:
            pass
        print("Enter a number from 0 to 100.")


def average(grades):
    return sum(grades) / len(grades)


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)


def pass_fail(grades):
    return "Pass" if average(grades) >= PASS_MARK else "Fail"


def main():
    grades = []
    while True:
        choice = input("1 Enter grades | 2 View results | 3 Exit: ")
        if choice == "1":
            grades = collect_grades()
        elif choice == "2":
            if grades:
                print(f"Average: {average(grades):.2f}")
                print(f"Highest: {highest(grades):g} | Lowest: {lowest(grades):g}")
                print("Result:", pass_fail(grades))
            else:
                print("Enter grades first.")
        elif choice == "3":
            break
        else:
            print("Choose 1, 2 or 3.")


if __name__ == "__main__":
    main()

# PASS_MARK has global scope because it is defined outside the functions.
# The pass_fail function can read that value when it checks the average.
# The grades list inside collect_grades is local to that function.
# Returning the list lets main store it in its own local variable.
