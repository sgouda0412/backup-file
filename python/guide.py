class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"


dog = Dog("Bucky")
print(dog.speak())


class Person(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)


emp = Person("Santosh", 123)
emp.display()


class Person1:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display_(self):
        return f"{self.name} has a id number of: {self.id_number}"


class Employee(Person1):
    def __init__(self, name, id_number, salary, post):
        super().__init__(name, id_number)
        self.salary = salary
        self.post = post


e = Employee("Santosh", 12, 50000, "Data Engineer")
print(e.display_())


# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary


class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee
        Job.__init__(self, salary)  # Initialize Job


# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(
            self, name, salary
        )  # Explicitly initialize EmployeePersonJob
        self.department = department


# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(
            self, name, salary
        )  # Explicitly initialize EmployeePersonJob
        self.team_size = team_size


# 5. Hybrid Inheritance (Multiple + Multilevel)
class SeniorManager(
    Manager, AssistantManager
):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)  # Initialize Manager
        AssistantManager.__init__(
            self, name, salary, team_size
        )  # Initialize AssistantManager


# Creating objects to show inheritance

# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department)

# Hierarchical Inheritance
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size)

# Hybrid Inheritance
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name)
