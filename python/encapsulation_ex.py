class Public:
    def __init__(self):
        self.name = "John"

    def display(self):
        print(self.name)


if __name__ == "__main__":
    obj = Public()
    obj.display()
    print(obj.name)


class Protected:
    def __init__(self):
        self._age = 30


class Subclass(Protected):
    def display(self):
        return self._age


obj = Subclass()
print(obj.display())


class Private:
    def __init__(self):
        self.__salary = 50000

    def display_salary(self):
        return self.__salary


obj = Private()
print(obj.display_salary())
print(obj.__salary)
