# implements special container data-types
# Counter, named tuple, ordered dict, default dict, deque

from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
# counter is a container that stores the elements 
# as dictionary keys and counts as dictonary values

a = "aaaaabbbccc"
my_counter = Counter(a) # keys letters and theire count as numeric values
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.most_common(2)) # 2 most comment elements
print(list(my_counter.elements())) # all elements as list

# namedtuple is lightweight similar to struct
Point = namedtuple("Point", "x,y")
pt = Point(1, 2)
print(pt)
print(pt.x, pt.y)

# ordered dict like regular dict but remembers order items were inserted
# with nowadays python the dict remembers that order allready so this is
# not really neccessary

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)

# defaultdict is similar to usual dict but with default value when key not set
d = defaultdict(int) # also works with float, list, etc
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["c"]) # -> ["c"] doesnt exist so default value 0 i returned

# deque -> double ended que -> used to remove/add elements from both ends
deq = deque()
deq.append(1)
deq.append(2)
deq.appendleft(0)
deq.appendleft(-1)
deq.pop()
deq.popleft()
print(deq)
deq.clear() # removes all elements
deq.extend([1, 2, 3, 4, 5, 6]) # add all elements to right side
deq.extendleft([0, -1 , -2, -3, -4, -5, -6])
print(deq)
deq.rotate(1) # rotate all elements 1 place to the right
print(deq)
deq.rotate(-1) # rotate to the left 1 place
print(deq)