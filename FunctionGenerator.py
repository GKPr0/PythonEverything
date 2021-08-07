def greeting_func_gen(lang):
    def customized_greeting(name):
        if lang == "de":   # German
            phrase = "Guten Morgen "
        elif lang == "fr": # French
            phrase = "Bonjour "
        elif lang == "it": # Italian
            phrase = "Buongiorno "
        elif lang == "tr": # Turkish
            phrase = "Günaydın "
        elif lang == "gr": # Greek
            phrase = "Καλημερα "
        elif lang == "cz":
            phrase = "Ahoj "
        else:
            phrase = "Hi "
        return phrase + name + "!"
    return customized_greeting

say_hi = greeting_func_gen("cz")
print(say_hi("Ondra"))


def args_test(func):
    def test(*args):
        if len(args) == 0:
            raise AttributeError("Musí mít argumenty")
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Arguments must be integers")
        return func(*args)
    return test


@args_test
def polynomial_generator(*args):
    def polynomial(x):
        catch = 0
        for index, arg in enumerate(args[::-1]):
            catch += arg * x ** index
        return catch
    return polynomial


x = 5

pol2 = polynomial_generator(1, 2, 3)
pol3 = polynomial_generator(2, 3, 2, 4)

print(pol2(x))

