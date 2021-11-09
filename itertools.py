# product, permutations, combinations, accumulations, groupby, and infinite iterators
# data types that can be used in a for loop
# most common - list
# itertools offer advanced tools

from itertools import count, cycle, repeat, groupby, accumulate, product, repeat, permutations, combinations, combinations_with_replacement
import operator

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b) # combines all elements together
print(list(prod))

# permutations = returns all possible orderings
c = [1, 2, 3]
perm = permutations(c)
print(list(perm))

# combinations makes all possible combinations with specified length
d = [1, 2, 3, 4]
comb = combinations(d, 2)
print(list(comb))

comb_replace = combinations_with_replacement(d, 2)
print(list(comb_replace))

# accumulation -> makes iterative that returns accumulative sums
e = [1, 2, 3, 4] # -> 1, 3, 6, 10
acc = accumulate(e)
print(list(acc))

# with operator multiply
f = [1, 2, 3, 4, 5]
acc = accumulate(f, func=operator.mul) # multiplicate instead of add
print(list(acc))

# with operator max
g = [1, 2, 10, 4, 5, 6, 7, 1000, 8, 9]
acc = accumulate(g, func=max) # max until next max
print(list(acc))

# groupby
def smaller_than_3(x):
  return x < 3

h = [1, 2, 3, 4]
group_obj = groupby(h, key=smaller_than_3)
for key, value in group_obj:
  print(key, list(value))

# with lambda func
group_obj1 = groupby(h, key=lambda x: x < 3)
for key, value in group_obj1:
  print(key, list(value))

# count
for i in count(10): # makes infinite loop starting at 10 and then adds 1 to each repetition
  print(i)
  if i == 15:
    break

# cycle -> cycle infinitly through iterable
a = [1, 2, 3]
stop = 0
for i in cycle(a):
  print(i)
  stop += 1
  if stop == 5:
    break

# repeat 
for i in repeat(1, 4): # infinitly repeat 1 (4 times)
  print(i)