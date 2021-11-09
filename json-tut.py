import json

# convert python dict to json -> serialization 
person = { 
  "name": "John", 
  "age": 30, 
  "city": "New York", 
  "hasChildren": False, 
  "titles": ["engineer", "programmer"]
}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# create json file from person dict
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4)

# JSON to python object -> deserialization
personNoJSON = json.loads(personJSON)
print(personNoJSON)

# convert/decode from file
personNoJSON2 = {}
with open('example.json', 'r') as file:
  personNoJSON2 = json.load(file)
print(personNoJSON2)

# with custom class
class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age
user = User('Max', 27)
def encode_user(o):
  if isinstance(o, User):
    return { 'name': o.name, 'age': o.age, o.__class__.__name__: True }
  else:
    raise TypeError('Wrong format')
userJSON = json.dumps(encode_user(user))
print(userJSON)

# second way to encode class
from json import JSONEncoder
class UserEncoder(JSONEncoder):
  def default(self, o):
      if isinstance(o, User):
        return { 'name': o.name, 'age': o.age, o.__class__.__name__: True }
      else:
        raise TypeError('Wrong format')
userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)
# or
userJSON = UserEncoder().encode(user)
print(userJSON)

# DECODE back
from json import JSONDecoder
def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])
  else:
    return dct
user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)