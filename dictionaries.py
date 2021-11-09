# Key-value pairs, unordered, mutable

# Create dictionary
mydict = {
  "name": "Max",
  "age": 28,
  "gender": "male",
  "country": "Germany",
  "city": "New York"
}
print(mydict)

# create without quotes
mydict2 = dict(name="Mary", age=27, city="London")
print(mydict2)

# access values
value = mydict["name"];
print(value)

# add value
mydict["email"] = "test@test.de";
print(mydict)

# delete
del mydict["name"]
print(mydict)

# del with pop
mydict.pop("age")
print(mydict)

# del with popitem -> removes last inserted pair
mydict.popitem()
print(mydict)

# check if value in dictonaty
if "city" in mydict:
  print(mydict["city"])
else:
  print("Not in dictionary")

# loop throuth keys
for key in mydict:
  print(key)

for key in mydict.keys():
  print(key)


# loop through values
for value in mydict.values():
  print(value)

# loop through both key and values
for value, key in mydict.items():
  print(key, value)

# copy dictonary
mydict_copy = dict(mydict)
print(mydict_copy)

mydict_copy2 = mydict.copy()
print(mydict_copy2)

# merge 2 dictonaries
dict1 = { 1: 1, 2: 2, 3: 4}
dict2 = { 3: 3, 4: 4, 1: 2}
dict1.update(dict2)
print(dict1)

# tuple as key
mytuple = (8, 7)
mydict1 = {
  mytuple: 15
}
print(mydict1[(8, 7)])