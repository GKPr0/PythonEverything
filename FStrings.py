# Link to article about f-Strings: https://realpython.com/python-f-strings/

""" Simple example of f-Strings """
name = "Ondra"
age = 22

print(f"Hello {name}. You are {age}")


""" Using expressions in f-Strings """
def to_lowercase(_input: str) -> str:
    return _input.lower()

name = "Ondrej Yann"
print(f"{to_lowercase(name)}")


""" Using f-string with __str__ and __repr__ methods """
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


""" Speed comparison with old methods"""
import timeit

# old %
print(timeit.timeit("""name = "Eric"
age = 74
'%s is %s.' % (name, age)""", number = 10000))

# newer .format()
print(timeit.timeit("""name = "Eric"
age = 74
'{} is {}.'.format(name, age)""", number = 10000))

# new f-String
print(timeit.timeit("""name = "Eric"
age = 74
f'{name} is {age}.'""", number = 10000))

