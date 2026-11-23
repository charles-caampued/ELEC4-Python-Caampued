# Charles Caampued | IV-BSIT-A | P6 | 11-21-2026

from functools import lru_cache


# Base: 0! is 1. Multiply n by the factorial of the smaller number.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# Base: F(0) = 0 and F(1) = 1. Add the previous two Fibonacci numbers.
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base: an empty sum is 0. Add n to the sum through n - 1.
def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base: an empty list fails and a matching first item succeeds.
# Otherwise search the remaining items.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def read_number():
    while True:
        try:
            n = int(input("Enter a whole number from 0 to 100: "))
            if 0 <= n <= 100:
                return n
        except ValueError:
            pass
        print("Use a whole number from 0 to 100.")


def main():
    while True:
        choice = input("1 Factorial | 2 Fibonacci | 3 Sum | 4 Search | 5 Exit: ")
        if choice == "5":
            break
        if choice == "1":
            print("Factorial:", factorial(read_number()))
        elif choice == "2":
            n = read_number()
            print("Indexing starts at 0.")
            print(f"F({n}) = {fibonacci(n)}")
            print("First", n, "terms:", [fibonacci(i) for i in range(n)])
        elif choice == "3":
            print("Sum:", sum_numbers(read_number()))
        elif choice == "4":
            entry = input("Up to 100 comma-separated items: ")
            items = [item.strip() for item in entry.split(",") if item.strip()]
            if len(items) > 100:
                print("Use at most 100 items.")
                continue
            print("Found:", search(items, input("Target: ").strip()))
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
