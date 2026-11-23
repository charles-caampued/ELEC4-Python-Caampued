# Charles Caampued | IV-BSIT-A | P3 | 11-21-2026

def add(names, keys):
    name = " ".join(input("Full name: ").split())
    if not name:
        print("Enter a name.")
    elif name.casefold() in keys:
        print("Already registered.")
    else:
        names.append(name)
        keys.add(name.casefold())
        print("Added", name)


def remove(names, keys):
    key = " ".join(input("Full name to remove: ").split()).casefold()
    for name in names:
        if name.casefold() == key:
            names.remove(name)
            keys.remove(key)
            print("Removed", name)
            return
    print("Name not found.")


def search(names):
    term = " ".join(input("Part of a name: ").split()).casefold()
    matches = [name for name in names if term in name.casefold()]
    if matches:
        display(matches)
    else:
        print("No student matches that search.")


def display(names):
    for number, name in enumerate(sorted(names, key=str.casefold), start=1):
        print(f"{number}. {name}")
    print("Total:", len(names))


names = []
keys = set()
while True:
    choice = input("1 Add | 2 Remove | 3 Search | 4 Display | 5 Exit: ")
    if choice == "1":
        add(names, keys)
    elif choice == "2":
        remove(names, keys)
    elif choice == "3":
        search(names)
    elif choice == "4":
        display(names)
    elif choice == "5":
        break
    else:
        print("Choose 1 to 5.")

# A list keeps order and allows repeated entries.
# Our names list keeps the spelling entered for each student.
# A set holds unique values, so keys stores each case-folded name once.
# Checking the set before adding a name prevents duplicates in the list.
