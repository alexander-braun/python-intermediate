# ordered, immutable, text representation

my_string = 'Hello There! I\'m an escape character!'
print(my_string)

my_multiline_string = """Hello
there!
I'm a multi-line \
string""" # no newline here with \
print(my_multiline_string)

# access
char = my_string[0] # -> H
print(char)

last_char = my_string[-1]
print(last_char)

# slicing
substring = my_string[1:5]
print(substring)

substring_step_1 = my_string[::1]
print(substring_step_1)
substring_step_2 = my_string[::2]
print(substring_step_2)

# concat
my_string_a = "Tom"
my_string_b = "and Jerry"
sentence = my_string_a + " " + my_string_b
print(sentence)

# iterate
for i in my_string_a:
  print(i)

# check if substr in string
if "om" in my_string_a:
  print("om in Tom")
else:
  print("om not in Tom")

# Trim
my_string_1 = '        Hello World    '
my_string_1_trim = my_string_1.strip()
print(my_string_1_trim)

# upper/lower case
print(my_string_1.upper())
print(my_string_1.lower())

# check string for properties
print(my_string_1.startswith(" "))
print(my_string_1.endswith(" "))

# find index of substr
print(my_string_1.index("He"))
print(my_string_1.find("ello"))

# count substrings
print(my_string_1.count("l"))

# replace
print(my_string_1.replace("World","Universe"))

# lists and strings
my_string_2 = "how are you doing"
as_list = my_string_2.split(" ")
print(as_list)
list_to_string = ' '.join(as_list) # ' ' -> means put space between each element
print(list_to_string)
list_to_string_2 = '#'.join(as_list)
print(list_to_string_2)

my_list_1 = ['a'] * 6
print(my_list_1)
my_list_4 =  ''.join(my_list_1)
print(my_list_4)

# formatting string with %, format(), f-Strings
# %
some_var = "Tom"
some_string = "the variable is %s" %some_var # placeholder with string
print(some_string)

some_var_num = 3
some_string_num = "the variable is %d" %some_var_num
print(some_string_num)

# -> floating point = %f
# -> specify digits = %.2f -> 2 digits after decimal point

# format()
some_string_2 = "the variable {} is {:.2f}".format(some_var, some_var_num)
print(some_string_2)

# f-strings
some_string_3 = f"the variable {some_var} is {some_var_num:.4f}"
print(some_string_3)