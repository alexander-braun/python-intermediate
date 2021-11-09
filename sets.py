# unordered, mutable, no duplicates

# create set
myset = { 1, 2, 3, 1 } # 1 at end will be deleted
print(myset)

# create set from list
myset1 = set([1, 2, 3, "Hello"])
print(myset1)

# split string into set
myset2 = set("Hello")
print(myset2)

# Create empty set
emptyset = set()
print(emptyset)

# Add to set
myset1.add(4)
print(myset1)

# remove element from set -> ERROR if element not in set
myset1.remove(3)
print(myset1)

# remove with discard -> NO ERROR if element not in set
myset1.discard(3)

# return arbitrary value from set (unordered)
print(myset1.pop(), myset1)

# empty set
myset1.clear()
print(myset1)

# iterate over set
for i in myset:
  print(i)

# check if element in set
if 1 in myset:
  print("1 is in set")
else:
  print("1 is not in set")

# union and intersection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens) # union combines both elements without duplication
print(union)

intersection = odds.intersection(primes) # intersection will only return elements from both sets
print(intersection)

difference = evens.difference(primes) # element from 1st set that are not in 2nd set
print(difference) 

symmetric_difference = evens.symmetric_difference(odds) # elements that are in set 1 but not in set 2 and elements in set 2 that are not in set 1
print(symmetric_difference)

odds.update(evens) # update with values from other set
print(odds)

odds.intersection_update(primes) # keep only elements found in both sets
print(odds)

odds.difference_update(evens) # updates by removing elements from other set
print(odds)

odds.symmetric_difference_update(evens) # elements found in set 1 and 2 but not the elements found in both
print(odds)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setA.issubset(setB)) # all elements of first set are also in second set
print(setB.issubset(setA))

print(setA.issuperset(setB)) # first set contains all elements from second set
print(setB.issuperset(setA))

print(setA.isdisjoint(setB)) # no same elements -> null intersection

# copying
copy_set = setA.copy()
print(copy_set)
copy_set2 = set(setA)
print(copy_set2)

# frozen set -> immutable version of normal set
frozen = frozenset([1, 2, 3])
print(frozen)
