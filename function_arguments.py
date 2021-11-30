def func(parameter):
  print(parameter)
  
func('argument')

# positional- and keyword- arguments:
def foo(a, b, c, d = 4): # -> with default argument ( always at end of func parameters )
  print(a, b, c, d)

foo(1, 2, 3) # -> positional arguments
foo(a = 1, c = 3, b = 2) # -> keyword arguments
foo(1, b = 3, c = 2) # -> no positional argument after keyword argument


# 1 star -> pass any number of positional arguments
# 2 star -> pass any number of keyword arguments
def foo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:  # -> tuple
    print(arg)
  for key in kwargs: # -> dictionary
    print(key, kwargs[key])
    
foo(1, 2, 3, 4, 5, ten = 10, eleven = 11)

# force keyword args after star
def test(a, b, *, c, d): # -> every parameter after star must be keyword arguments
  print(a, b, c, d)
test(1, 2, c = 3, d = 4)

# unpacking arguments
def bar(a, b, c):
  print(a, b, c)
my_list = [0, 1, 2] # -> also works with tuple
bar(*my_list) # -> length of container must match number of parameters
my_dict = { "a": 1, "b": 2, "c": 3}
bar(**my_dict) # -> for dictionary unpack with 2 stars, keys must match parameter names


# local vs global variables
def foobar():
  global global_number # -> to be able to edit global_number
  x = global_number
  global_number = 3
  print('number inside function:', x)
global_number = 0
foobar()
print(global_number)


# immutable objects can't be changed but mutable ones can be changed ( just int won't work but a list f.e. would work )
def barfoo(a_list):
  a_list.append(4)
my_list = [1, 2, 3]
barfoo(my_list)
print(my_list)
