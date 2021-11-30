# copy elements with build in copy module


# assignment operator
org = 5
cpy = org # -> only creates new variable with same reference to where 5 is saved
cpy = 6 # -> creates new variable 
print(org, cpy)

org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = 10
print(org, cpy) # -> also original has value 10


# copy module
import copy

# shallow copy: only 1 level deep, only references of nested child objects
# deep copy: full independent copy
org = [0, 1, 2, 3, 4]
cpy = copy.copy(org)
cpy[0] = 10
print(org, cpy)

# deep copy works for build in types and custom objects
nested = [[1, 2, 3], [4, 5, 6, 7]]
cpy_deep = copy.deepcopy(nested)
cpy_deep[0][0] = 1000
print(cpy, 'nested:', nested)
print(cpy_deep, 'nested:', nested)
