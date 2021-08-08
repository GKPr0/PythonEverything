from SupportFunctions import HEADER, LINK
from time import time, sleep


LINK("https://www.geeksforgeeks.org/class-as-decorator-in-python/")
LINK("https://levelup.gitconnected.com/mastering-decorators-in-python-3-588cb34fff5e")
HEADER("Using __call__ method in class")


class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


x = A()
print("Now calling the instance:")
x(3, 4, x=11, y=10)


# ----------------------------------------------
HEADER("More practical example of using __call__ method")


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0,
                      1: 1}

    def __call__(self, n):
        if n not in self.cache:
            self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")
print("\n")

# ----------------------------------------------
HEADER("Class decorator as execution timer")


class Timer:

    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} second".format(end_time - start_time))
        return result


@Timer
def some_function(delay):
    sleep(delay)


some_function(1)


# ----------------------------------------------
HEADER("Class decorator as error checker")


class ErrorChecker:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        if any([isinstance(i, str) for i in args]):
            raise TypeError("Parameter cannot be a string !!")
        else:
            return self.function(*args)


@ErrorChecker
def add_numbers(*numbers):
    return sum(numbers)


try:
    print(add_numbers(1, 2, 3))
    print(add_numbers(1, '2', 3))
except TypeError as e:
    print(e)

# ----------------------------------------------
HEADER("Class decorator with argmunets")


class Decorator:

    def __init__(self, *args, **kwargs):
        print("Inside decorator with args {} and kwargs {}".format(args, kwargs))

    def __call__(self, func):
        print("Inside __call__() with function {}".format(func.__name__))

        def wrapped(*args, **kwargs):
            print("Inside wrapped with args {} and kwargs {}".format(args, kwargs))
            return func(*args, *kwargs)

        return wrapped


@Decorator("decorator arg 1", "decorator arg 2")
def my_function(a, b, c):
    print("Inside my_function()")


print("Finished decorating my_function()")
my_function(1, 2, 3)
print("Immediately after my_function() line")


# ----------------------------------------------
HEADER("Using class decorators to decorate class")


def time_this(func):
    def wrapped(*args, **kwargs):
        print("________timer starts________")
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print("Elapsed time = {}".format(end_time - start_time))
        return result
    return wrapped


def time_all_class_methods(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            print("__init__() called with args: {} and kwargs: {}".format(args, kwargs))
            self.decorated_object = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                x = super().__getattribute__(item)
                return x
            except AttributeError as e:
                print(e)

            x = self.decorated_object.__getattribute__(item)
            if type(x) == type(self.__init__):
                print("Attribute belonging to decorated_obj: {}".format(item))
                return time_this(x)
            else:
                return x

    return Wrapper


@time_all_class_methods
class MyClass:
    def __init__(self):
        print("entering MyClass.__init__")
        sleep(1)
        print("exiting MyClass.__init__")

    def method_x(self):
        print("entering MyClass.method_x")
        sleep(0.7)
        print("exiting MyClass.method_x")

    def method_y(self):
        print("entering MyClass.method_y")
        sleep(1.2)
        print("exiting MyClass.method_y")


print("after decoration")
instance = MyClass()
print("object created")

instance.method_x()
instance.method_y()