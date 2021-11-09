from functools import reduce

# expression without a name
# lambda arguments: expression

add10 = lambda x : x + 10
print(add10(10))

# multiple arguments
mult = lambda x, y : x * y
print(mult(10, 10))

# sort
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x : x[1]) # sort by y index
print(points2D_sorted)

  # sort by sum of each tuple
points2D_sorted_sum_of_tuple = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D_sorted_sum_of_tuple)


# map transforms each element with function
a = [1, 2, 3, 4, 5]
times3 = map(lambda x: x * 3, a) # times 3 each element
print(a)
print(list(times3))

c = [x * 3 for x in a] # -> easier
print(c)

# filter
b = [1, 2, 3, 4, 45, 6, 7]
filtered = filter(lambda x : x < 4, b) # filter by values smaller 4
print(list(filtered))

  # filter even numbers
c = [1, 2, 3, 4, 5, 6]
filtered_even = filter(lambda x: x % 2 == 0, c)
print(list(filtered_even))

filtered_even_easier = [x for x in c if x % 2 == 0]
print(filtered_even_easier)

# reduce
r = [1, 2, 3, 4, 5, 6]
reduced_list = reduce(lambda x, y: x * y, r) # 1 * 2 * 3 * 4 * 5 * 6
print(reduced_list)