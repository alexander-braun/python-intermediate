# generators = functions that return an object that can be iterated over
# generate the items inside the object lazily -> generate only when asked for
# very memory efficient with large data sets

def mygenerator():
  yield 1
  yield 2
  yield 3
g = mygenerator()

# loop over all elements
for i in g:
  print(i)

# call "next" to get next value
g2 =  mygenerator()
value = next(g2)
print(value)
value = next(g2)
print(value)

# build in sum
g3 = mygenerator()
print("sum:", sum(g3))

# build in sort
g4 = mygenerator()
print("sorted:", sorted(g4))

# create countdown
def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1
cd = countdown(4)
value = next(cd)
print(value)
value = next(cd)
print(value)


import sys

# version without generator
def firstn(n):
  nums = []
  num = 0
  while num < n:
    nums.append(num)
    num += 1
  return nums

print(sys.getsizeof(firstn(10000000)))

# version with generator
def firstn_generator(n):
  num = 0
  while num < n:
    yield num
    num += 1

print(sys.getsizeof(firstn_generator(10000000))) # -> very memory efficient

# Practice with Fibonacci
def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

fib = fibonacci(3000)
for i in fib:
  print(i)
  
# Generator expressions

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
  print(i)
