# Charles Caampued | IV-BSIT-A | P4 | 11-21-2026

def divide():
    try:
        first = float(input("Dividend: "))
        second = float(input("Divisor: "))
        result = first / second
    except ValueError:
        print("Enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Quotient:", result)
    finally:
        print("Returning to the menu.")


def display_file():
    filename = input("Text file path: ").strip()
    try:
        with open(filename, encoding="utf-8") as source:
            print(source.read())
    except FileNotFoundError:
        print("File not found.")
    except (OSError, UnicodeError, ValueError) as error:
        print("Could not read file:", error)


while True:
    choice = input("1 Divide | 2 Read file | 3 Exit: ")
    if choice == "1":
        divide()
    elif choice == "2":
        display_file()
    elif choice == "3":
        break
    else:
        print("Invalid menu choice.")
