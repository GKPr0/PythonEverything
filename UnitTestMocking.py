from SupportFunctions import HEADER, LINK
from subprocess import Popen, PIPE
import unittest.mock as mock

HEADER("MOCK description")
print(mock.Mock.__doc__)


HEADER("MagicMock description")
print(mock.MagicMock.__doc__)


HEADER("MagicMock has implemented all dunder(magic) methods ")
magic_mock = mock.MagicMock()
my_mock = mock.Mock()

try:
	int(magic_mock)
	int(my_mock)
except Exception as e:
	print(e)


HEADER("Calling a method on Mock object dynamically creates called method")
print(my_mock.foo("test"))
print(my_mock.bar())
print(my_mock.bar(1, 2, 3))

my_mock()
my_mock()

print(f"{my_mock.foo.called=}")
print(f"{my_mock.bar.call_count=}")
print(f"{my_mock.method_calls=}")

print(f"{my_mock.mock_calls=}")


HEADER("Make assertion on method usage")
try:
	my_mock.bar.assert_called_with(1, 2, 3)
	my_mock.bar.assert_called_with(1, 2)
except Exception as e:
	print(e)

try:
	my_mock.assert_called()
	my_mock.foo.assert_called_once()
	my_mock.bar.assert_called_once()
except Exception as e:
	print(e)


HEADER("How to return value when called")
my_mock = mock.MagicMock(return_value="Mock called")
my_mock.bar = mock.MagicMock(return_value="Bar called")
my_mock.foo.return_value = "Foo called"
my_mock.__int__.return_value = 666

print(my_mock())
print(my_mock.bar())
print(my_mock.foo("hi", 150))
print(int(my_mock))


HEADER("Creating mock object that has same API as some useful object")
def function(a, b, c):
	pass

mock_function = mock.create_autospec(function, return_value="foo")

try:
	print(mock_function(1, 2, 3))
	mock_function.assert_called_once_with(1, 2, 3)
	mock_function("wrong argument", "count")
except Exception as e:
	print(e)


HEADER("Adding side effect to mock call")
def side_effect_():
	print("side effect called")

my_mock = mock.MagicMock(side_effect = side_effect_)
my_mock()

try:
	my_mock = mock.MagicMock(side_effect=TypeError("int expected"))
	my_mock()
except Exception as e:
	print(e)


HEADER("Using patch decorator to assign mock object")
class MyClass():
	def __init__(self):
		self.counter = 0

	def my_method(self, a, b):
		print("Useful method")
		return 100

	def real_method(self):
		return self.sub_method("Ondra")

	def sub_method(self, name):
		self.counter += 1
		return f"Hi {name}"


@mock.patch("time.time")
@mock.patch.object(MyClass, "my_method", return_value=666)
@mock.patch.object(MyClass, "sub_method")
def mock_using_patch(sub_method, my_method, time):
	my_class = MyClass()
	print(my_class)
	print(my_class.real_method)
	print(my_class.my_method)
	print(my_class.sub_method)

	result = my_class.my_method("Test")
	my_method.assert_called_with("Test")
	assert result == 666

	my_class.real_method()
	my_class.sub_method.assert_called_with("Ondra")

	time()
	time.assert_called_once()


mock_using_patch()


HEADER("Using mocking with a context manager / Using side effect and return_value together")
with mock.patch.object(MyClass, "sub_method", return_value="Hi", autospec=True) as mock_method:
	my_class = MyClass()
	print(my_class)
	print(my_class.sub_method)

	def fake_counter(self, name):
		my_class.counter += 1
		return mock.DEFAULT

	mock_method.side_effect = fake_counter

	return_val = my_class.real_method()

	mock_method.assert_called_once_with(my_class, "Ondra")
	assert return_val == "Hi"
	assert my_class.counter == 1

