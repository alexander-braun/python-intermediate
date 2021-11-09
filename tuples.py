# Tuple: ordered, immutable, allows duplicate elements

# create tuple
mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple_without_parentesis = "Sam", 25, "Boston"
print(mytuple_without_parentesis)

# only 1 element not recognized as a tuple
mysmalltuple1 = ("Max")
print(type(mysmalltuple1))

# only 1 element with comma!
mysmalltuple2 = ("Max",)
print(type(mysmalltuple2))

# create from list
mytuple1 = tuple([1, 2, 3])
print(mytuple1)

# access elements like lists
print(mytuple1[1])

# last item
print(mytuple1[-1])

# change elements in tuple not possible -> immutable

# iterate over tuple
for i in mytuple1:
  print("iterate over tuple: ", i)


# check if element is in tuple
if 1 in mytuple1:
  print("Yes 1 is in tuple")
else:
  print("No 1 is not in tuple")

# usefull methods
my_tuple = ('a', 'p', 'p', 'l', 'e')

# length
print(len(my_tuple))

# count
print(my_tuple.count('p'))

# first index of element
print(my_tuple.index('p'))

# tuple to list
my_list = list(my_tuple)
print(my_list)

# list to tuple
my_tuple2 = tuple(my_list)
print(my_tuple2)

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[:3]
print(b)

# slicing with step
c = a[::2]
print(c)

# unpack
d = "Max", 28, "Boston"
name, age, city = d
print(name, age, city)

# unpack different amount then original tuple
c = 0, 1, 2, 3, 4
i1, *i2, i3 = c
print(i1, i2, i3)

# compare tuple and list
# tuples can be more efficient specially with large data
import sys
my_list1 = [0, 1, 2, "hello", True, 12, 13, 14]
my_tuple1 = (0, 1, 2, "hello", True, 12, 13, 14)
print(sys.getsizeof(my_list1), "bytes")
print(sys.getsizeof(my_tuple1), "bytes")

# also faster -> 100mio times create list vs tuple (8.5s vs 1.34s)
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=100000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=100000000))