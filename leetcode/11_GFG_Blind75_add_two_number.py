def add_two_numbers(a: int, b: int) -> int:
    while b != 0:
        sum_without_carry = a ^ b
        carry = (a & b) << 1
        a = sum_without_carry
        b = carry
    return a


if __name__ == "__main__":
    a = 12
    b = 8
    print(add_two_numbers(a, b))
