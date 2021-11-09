# Errors and Exceptions

# Syntax err

# a = 5 print(a)                      -> no new line started

# a = 5
# print(a))                           -> too many brackets

# a = 5 + '10'                        -> TypeError

# import someModuleThatDoesNotExist   -> ModuleNotFoundError

# b = c                               -> NameError

# f = open('someFile.txt')            -> FileNotFoundError

# a = [1, 2, 3]
# a.remove(4)                         -> ValueError

# a = [1, 2, 3]
# print(a[10])                        -> IndexError

# my_dict = { 'name': 'Max' }
# print(my_dict['age'])               -> KeyError

# ExceptionError
# if x negative -> Exception is raised
x = 5
if x < 0:
  raise Exception("X should be positive")

# AssertionError
# if x < 0 Assertion error is raised
y = 5
assert (y >= 0), 'x is not positive'

# Handle Exceptions
z = -5
try: 
  a = 5 / 0
  b = 5 + '10'
except ZeroDivisionError:
  print("Zero division err")
except TypeError as e:
  print("Type Error:", e)
except Exception as e:
  print("Code continues here, exception was:", e)
else:
  print("All good...!")
finally:
  print("Here put cleanup operations")

# Create own error
class ValueTooHighError(Exception):
  pass
class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value
    
def test_value(x):
  if x > 100:
    raise ValueTooHighError('Value is too high')
  if x < 5:
    raise ValueTooSmallError('Value is too small', x)

try:
  test_value(4)
except ValueTooHighError as e:
  print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)

