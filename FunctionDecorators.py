from SupportFunctions import HEADER, LINK
from random import random, randint, choice


LINK("https://realpython.com/primer-on-python-decorators/")
HEADER("Creating custom decorator")


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper


@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))


foo("Hi")

# ----------------------------------------------
HEADER("Decorating build in functions")


def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper


random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

random()
randint(3, 8)
choice([4, 5, 6])

# ----------------------------------------------
HEADER("Decorator as argument test")


def argument_test_natural_number(func):
    def helper(x):
        try:
            if not isinstance(x, int):
                raise TypeError()
            if x < 0:
                raise ValueError()
            return func(x)
        except TypeError:
            raise TypeError("Argument must be an integer!")
        except ValueError:
            raise ValueError("Argument must be >= 0")
    return helper


@argument_test_natural_number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


for i in range(10):
    print(i, factorial(i))
try:
    print(factorial("Ahoj"))
except Exception as e:
    print("Chyba zachycena:", e)

# ----------------------------------------------
HEADER("Decorator as function call counter")


def call_counter(func):
    def counter(*args, **kwargs):
        counter.call_count += 1
        return func(*args, **kwargs)

    counter.call_count = 0
    return counter


@call_counter
def inc(x):
    return x + 1


x = 0
print("Call count", inc.call_count)
for i in range(10):
    x = inc(x)
    print(x)
print("Call count", inc.call_count)

# ----------------------------------------------
HEADER("Decorator with parameter")


def greetings(expression):
    def greeting_decorator(func):
        def function_wrapper(x):
            """ Greeting decorator doc string"""
            print(expression + ", " + func.__name__, "returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


@greetings("Ahoj")
def foo(x):
    print(x)


foo(42)

# ----------------------------------------------
HEADER("Dealing with attribution deleting when using decorators")


def atr_del1(x):
    """ Some random function"""
    return x + 2


print("\nName:", atr_del1.__name__)
print("Doc:", atr_del1.__doc__)


@greetings("Hi")
def atr_del2(x):
    """ Some random function with decorator"""
    return x + 2


print("\nName:", atr_del2.__name__)
print("Doc:", atr_del2.__doc__)


def greetings_without_args_deletion(expression):
    def greeting_decorator(func):
        def function_wrapper(x):
            """ Greeting decorator doc string"""
            print(expression + ", " + func.__name__, "returns:")
            return func(x)
        function_wrapper.__name__ = func.__name__
        function_wrapper.__doc__ = func.__doc__
        return function_wrapper
    return greeting_decorator


@greetings_without_args_deletion("Hi")
def atr_del3(x):
    """ Some random function with decorator"""
    return x + 2


print("\nName:", atr_del3.__name__)
print("Doc:", atr_del3.__doc__)


# ----------------------------------------------
HEADER("Using build-in tool to handle attr deletion when using decorators")
from functools import wraps


def greetings_with_build_in_args_wrap(func):
    @wraps(func)
    def function_wrapper(x):
        """ Greeting decorator doc string"""
        print("Calling" + func.__name__, "returns:")
        return func(x)
    return function_wrapper


@greetings_with_build_in_args_wrap
def atr_del4(x):
    """ Some random function with decorator"""
    return x + 2


print("\nName:", atr_del3.__name__)
print("Doc:", atr_del3.__doc__)
