# Charles Caampued | IV-BSIT-A | P2 | 11-21-2026

def average(grades):
    return sum(grades) / len(grades)


def pass_fail(grades):
    return "Pass" if average(grades) >= 75 else "Fail"


def highest(grades):
    return max(grades)


def lowest(grades):
    return min(grades)
