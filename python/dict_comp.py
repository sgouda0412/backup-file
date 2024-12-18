keys = ["a", "b", "c", "d", "e"]
values = [1, 2, 3, 4, 5]

res = {k: v for (k, v) in zip(keys, values)}
print(res)


d = {x: x**2 for x in range(5)}
print(d)

r = {x.upper(): x * 3 for x in "coding"}
print(r)

dic = {x: x**3 for x in range(10) if x ** 3 % 4 == 0}
print(dic)

squares = {x: x**2 for x in range(5)}
print(squares)


