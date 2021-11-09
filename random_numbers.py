# random module
import random

a = random.random() # random float between 0 and 1
print(a)
a = random.uniform(1, 10) # 1 to 10 inclusive float
print(a)
a = random.randint(1, 10) # 1 to 10 inclusive int
print(a)
a = random.randrange(1, 10) # 1 to 10 upper bound exclusive (never 10)
print(a)
a = random.normalvariate(0, 1) # random value from normal distribution with mean of 0 and standard deviation of 1
print(a)

mylist = list("ABCDEFGH")
random_choice = random.choice(mylist) # pick random element from list
print(random_choice)

random_sample = random.sample(mylist, 3) # pick 3 unique random elements
print(random_sample)

random_sample_2 = random.choices(mylist, k=3) # pick 3 random elements from list
print(random_sample_2)

print(mylist)
random.shuffle(mylist) # shuffle list in place
print(mylist)

# this random method is not really random - with the same seed there are the same end results in "random" numbers
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(1)
print(random.random())
print(random.randint(1, 10))

# for truly random numbers use secrets module
import secrets

a = secrets.randbelow(10) # exclusive upper bound 0 - 10 with 10 not included
print(a)

a = secrets.randbits(4) # returns integer with k random bits -> highest possible is 1111 -> 15
print(a)

mylist = list("ABCDEFGH")
a = secrets.choice(mylist) # pick random un-reproducable choice
print(a)


# for arrays use numpy
import numpy as np

a = np.random.rand(3) # 1D Array with 3 elements -> 3 random floats
print(a)

a = np.random.rand(3, 3) # 2D Array with 3 elements with each 3 a floating point numbers
print(a)

a = np.random.randint(0, 10, 3) # 1D Array with random integers
print(a)

a = np.random.randint(0, 10, (3, 4)) # 2D Array with 3 elements with each 4 random ints ranging from 0 to 10 (10 excluded)
print(a)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)  # switch elements in first axis
print(arr)

# with seed
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))