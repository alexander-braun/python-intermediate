# simple multiplication
result = 5 * 5
print(result)

# to the power of
result = 2 ** 5
print(result)

# create list of 10 elemetns
zeros = [0, 2] * 10
print(zeros)

# args and kwargs
def foo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
    
  for key in kwargs:
    print(kwargs[key])
foo(1, 2, 3, 4, c = 5, d = 6)

# unpacking
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning)
print(last)

my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
new_list = [*my_tuple, *my_list]
print(new_list)

d1 = { "a": 1 }
d2 = { "b": 2 }
d3 = { **d1, **d2 }
print(d3)