
# Lists: ordered, mutable, allows duplicate elements
myList = [
  "banana", "cherry", "apple", "banana", 2, True
]
print(myList)

# create new empty list with list() function
myList2 = list()
print(myList2)

# split string into list
text = "Hello There!"
myList3 = list(text)
print(myList3)

# create array from array (useless)
test2 = ["hello", "there", "hey"]
myList4 = list(test2)
print(myList4)

# get last item -> "[hey]"
print(test2[-1])

# get second last item -> "there"
print(test2[-2])

# iterate list by element
for i in test2:
  print(i)

# check if item is in list
if "Hello" in test2:
  print("Is in list")
else:
  print("Not in list")

# check how many elements in list -> 3
print(len(test2))

# append items
test2.append("Lemon")
print(test2)

# insert item at position
test2.insert(0, "Inserted")
print(test2)

# return last item and remove it
lastItem = test2.pop()
print(lastItem)
print(test2)

# remove element at index
removed = test2.remove("Inserted")
print(test2)

# reverse list
test2.reverse()
print(test2)

# sort list alphabetically -> not working if there is f.e. an array in the list
test2.sort()
print(test2)

# sort and create new list
newList = sorted(test2)
print(newList)

# remove all elements
test2.clear()
print(test2)

# create new list with 5 zeros in it
myZeroList = [0] * 5
print(myZeroList)

# concatenate lists -> [0, 0, 0, 0, 0] + ['banana', .........] = [0, 0, .... 'banana' ....]
new_list = myZeroList + myList
print(new_list)

# slice list inclusive first index, exclusive last index
someList = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
a = someList[3:6]
print(a)

# slice from start to index
someList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
b = someList2[:3]
print(b)

# slice from index to end
someList3 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
c = someList3[3:]
print(c)

# make copy from list
someList4 = someList3.copy()
print(someList4)

someList5 = list(someList3)
print(someList5)

someList6 = someList3[:]
print(someList6)

# list comprehension
someList7 = [1, 2, 3, 4, 5, 6]
someListSquared = [i*i for i in someList7]
print(someListSquared)
