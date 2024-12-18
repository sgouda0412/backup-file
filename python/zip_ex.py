names = ["John", "Alice", "Bob", "Lucy"]
scores = [85, 90, 78, 92]
res = zip(names, scores)
print(list(res))  # list of tuples

# syntax

# zip(*iterables) [tuples, list, strings, dictionary]

res1 = zip(scores)
print(list(res1))

a = [("Apple", 10), ("Banana", 20), ("Orange", 30)]
fruits, quantity = zip(*a)
print(f"Fruits: {fruits}")
print(f"Quantities: {quantity}")


d = {"name": "Alice", "age": 25, "grade": "A"}
keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))

names = ["sravan", "bobby", "ojaswi", "rohith", "gnanesh"]
# create a list of subjects
subjects = ["java", "python", "R", "cpp", "bigdata"]
# create a list of marks
marks = [78, 100, 97, 89, 80]

for i, (names, subjects, marks) in enumerate(zip(names, subjects, marks)):
    print(f"Index: {i} {names} {subjects} {marks}")

l1 = [[1, 2], [3, 4], [5, 6]]
l2 = [[7, 8], [9, 10], [11, 12]]

# Zipping list
res = [(a, b) for a, b in zip(l1, l2)]
print(res)


import itertools

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8], [9, 10]]

# Zipping with padding
res = list(itertools.zip_longest(a, b, fillvalue=[]))
print(res)


list1 = ["geeks", "for", "geeks"]
list2 = [3, 2, 1]

zipped = list(zip(list1, list2))
res = sorted(zipped, key=lambda x: x[0])
print(res)


