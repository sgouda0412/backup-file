x = [1, 2, 3, 4, 5]
squared = [i**2 for i in x]
print(squared)

x = [1, 2, 3, 4, 5]
doubled = [i * 2 for i in x]
print(doubled)

even_numbers = [i for i in x if i % 2 == 0]
print(even_numbers)

result = ["Even" if i % 2 == 0 else "Odd" for i in x]
print(result)

a = [1, 2, 3, 4, 5]
result = [
    (
        "Divisible by 2"
        if n % 2 == 0
        else "Divisible by 3" if n % 3 == 0 else "Other"
    )
    for n in a
]
print(result)


numbers = [-10, 0, 15, -3, 20]
result = [
    "Negative" if n < 0 else "Zeroes" if n == 0 else "Positive"
    for n in numbers
]
print(result)


ages = [3, 12, 17, 20, 65]
categories = [
    "Child" if age < 13 else "Tenagers" if age < 18 else "Adult"
    for age in ages
]
print(categories)

signals = ["Red", "Yellow", "Green", "Blue"]

actions = [
    (
        "Stop"
        if signal == "Red"
        else (
            "Wait "
            if signal == "Yellow"
            else ("Go" if signal == "Green" else "Unknown")
        )
    )
    for signal in signals
]
print(actions)


def segregate(arr):
    return [x for x in arr if x == 0] + [x for x in arr if x == 1]


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(segregate(arr))
