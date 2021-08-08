from SupportFunctions import HEADER, LINK
from SupportFunctions import timeit


LINK("https://realpython.com/python-f-strings/")
HEADER("Simple example of f-Strings")

name = "Ondra"
age = 22

print(f"Hello {name}. You are {age}")


# ----------------------------------------------
HEADER("Using expressions in f-Strings")
def to_lowercase(_input: str) -> str:
    return _input.lower()

name = "Ondrej Yann"
print(f"{to_lowercase(name)}")


# ----------------------------------------------
HEADER("Using f-string with __str__ and __repr__ methods")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} is {self.age}. Surprise"

    def __str__(self):
        return f"{self.name} is {self.age}."


me = Person("Ondra", 22)
print(me)  # calls __str__
print(f"{me}")  # calls __str__
print(f"{me!r}")  # calls __repr_


# ----------------------------------------------
HEADER("Speed comparison with old methods")
@timeit(number=100000)
def old_format(name, age):
    return "%s is %s" % (name, age)


@timeit(number=100000)
def newer_format(name, age):
    return "{} is {}".format(name, age)


@timeit(number=100000)
def new_format(name, age):
    return f"{name} is {age}"


name = "Ondra"
age = 22

old_format(name, age)
newer_format(name, age)
new_format(name, age)

