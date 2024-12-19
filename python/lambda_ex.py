# syntax
# lambda args : expression


calc = lambda num: "even" if num % 2 == 0 else "odd"
print(calc(4))

s = "geeksforgeeks"
print(lambda s: s)

filter_nums = lambda s: "".join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

do_exclaim = lambda s: s + "!"
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

l = ["1", "2", "9", "0", "-1", "-2"]
filter_postive_even_no = list(
    filter((lambda x: not (int(x) % 2 == 0 and int(x)) > 0), l)
)

print(filter_postive_even_no)

my_list = [1, 2, 3, 4, 5]
filter_even = list(filter(lambda x: x % 2 == 0, my_list))
print(filter_even)

squared_no = list(map(lambda x: x**2, my_list))
print(squared_no)

