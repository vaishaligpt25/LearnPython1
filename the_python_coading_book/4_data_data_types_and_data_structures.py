
a_number = 5
a_value = 5.6
my_value = "Harry"
my_data = [2, 5, 7, 23, 1, 4, 10]

print(type(a_number))
print(type(a_value))
print(type(my_value))
print(type(my_data))

print("\n-----1-----\n")

#for item in a_number:
#   print(a_number)

for item in my_value:
    print(item)
print()

for item in my_data:
    print(item)

print("\n-----2----\n")

my_value = "Harry"
print(my_value[2])

print("\n-----3----\n")
my_data = [2, 5, 7, 23, 1, 4, 10]
my_data[2] = 8
print(my_data)

print("\n-----4----\n")
#my_value = "Harry"
#my_value[2] = "x"
#print(my_value)
#Strings are immutable data types. This means that once they’ve been created, you cannot make changes within the string. Immutable data types are meant for information that is unlikely to need to change once created.
#Lists are mutable, which means that they are flexible containers that can change. You can add new items to a list or replace existing ones. Mutable data types are ideal for data that is likely to change while a program is running.
#Note that even with immutable data types, you’re still allowed to overwrite the entire variable. So if I did want to change the third letter of my name to "y", I would need to do the following:
my_value = "Haxrry"
print(my_value)


print("\n-----5----\n")
#METHOD ASSOCIATED WITH DATA TYPE:

# When a function is associated with a data type and attached to it with the full stop, we call it a method.

my_data = [2, 5, 7, 23, 1, 4, 10]
my_data.append(50)
print(my_data)

my_data.remove(7)
print(my_data)

print("\n-----6----\n")
#If you want to delete a value by position within the list, instead of by value, you can use the pop() method:
my_data.pop(4)
print(my_data)

print("\n-----7----\n")

my_data = [2, 5, 7, 23, 1,2, 2, 4, 10]
print(my_data.count(2))

my_value = "Harry"
print(my_value.upper())
print(my_value.lower())
print(my_value.replace("y","e"))


print("\n-----8----\n")

# There are 3 types of data structures:
#List = A list is a sequence and an iterable, and it’s mutable.
#Tuples = Tuples, like strings, are immutable. A tuple is an immutable sequence.
#Dictionaries

# Tuples:
my_data = (2, 5, 7, 23, 1,2, 2, 4, 10)
print(type(my_data))
#Tuples are also sequences and you can use indexing and slicing on tuples in the same way as you do with lists
print(my_data[2:6])
print(my_data[-1])
#my_data[2] = 50
#print(my_data[2])

#At this point, you may be wondering why you need tuples at all. They seem to be like lists but with fewer features! However, when you want to create a sequence of items and you know that this sequence will not change in your code, creating a tuple is the safer option. It makes it less likely that your code will accidentally change a value in the tuple, as if your code tries to do so, you’ll get an error. Using a tuple when you know the data should not change means you’re less likely to introduce bugs in your code.

#Tuples are also more memory efficient than lists, but you don’t need to worry about memory issues for the time being.

my_data = 2, 5, 7, 23, 1,2, 2, 4, 10
print(type(my_data))

print("\n-----9----\n")

my_data = (2, 5, 7, 23, 1,2, 2, 4, 10)
#my_data[2] = 50
#print
#This is the same error you got when you tried to reassign a new letter into a string. Tuples, like strings, are immutable. A tuple is an immutable sequence.

#At this point, you may be wondering why you need tuples at all. They seem to be like lists but with fewer features! However, when you want to create a sequence of items and you know that this sequence will not change in your code, creating a tuple is the safer option. It makes it less likely that your code will accidentally change a value in the tuple, as if your code tries to do so, you’ll get an error. Using a tuple when you know the data should not change means you’re less likely to introduce bugs in your code.

#Tuples are also more memory efficient than lists, but you don’t need to worry about memory issues for the time being.

#Although the round brackets, or parentheses, are the type of brackets associated with tuples, you can also omit the parentheses altogether when creating tuples:

#As with lists, you can store any data type in a tuple, including other data structures:

another_tuple = (3, True, [4, 5], "hello", (0, 1, 2), 5.5)

# The order of the items in a dictionary is not important. This is different to lists, tuples, and strings, in which the order of items is a defining feature of the data structure. What matters in a dictionary is the association between the key and its value. If you try to access an item from a dictionary using the same indexing you’ve used for lists, tuples, and strings, you’ll get an error:
# Trying to access the third item in the dictionary doesn’t make sense as a dictionary is not a sequence. Instead, we can use the key to access values from within the dictionary:
student_marks = {"John": 67, "Kate": 86, "Trevor": 92, "Jane": 55, "Mark": 59, "Anne": 79}
#student_marks[2]
#print(student_marks[2])
print(student_marks["Trevor"])

# Dictionaries are a mutable data type. You’ve changed the value associated with "Kate" to 99. You can even increment the value in a dictionary:
student_marks["Jane"] = student_marks["Jane"] + 1
print(student_marks)

#print(student_marks["Harry"])
print(student_marks.keys())
print(student_marks.values())
print(student_marks.get("John"))
print(student_marks.get("Harry"))

print("\n-----10----\n")

for item in student_marks:
    print(item)

print("\n-----10----\n")

# Method 1: using zip function
keys = ["A", "B", "C", "D"]
values = [3, 4, 5, 6]
my_dict = dict(zip(keys, values))
print(my_dict)

#Method 2: using dictionary comprehension
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

# Method 3: using a traditional for loop
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print(my_dict)

print("\n-----11----\n")

word_frequency = {}
#for word in words:
    #if word not in word_frequency.keys():
     #   word_frequency[word] = 1
some_words = {'hello': 3, 'python': 9, 'bye': 1, 'computer': 2}
print(some_words.keys())
print("python" in some_words)
print("monday" in some_words)
print("monday" not in some_words)

print("\n-----12----\n")

'''word_frequency = {}
for word in word_frequency:
    if word not in word_frequency.keys():
        word_frequency[word] = 1
    else:
        word_frequency[word] = word_frequency[word] + 1
print(word_frequency)'''

word_frequency = {'hello': 3, 'python': 9, 'bye': 1, 'computer': 2}
for word in word_frequency:
    if word not in word_frequency.keys():
        word_frequency[word] = 1
    else:
        word_frequency[word] = word_frequency[word] + 1
print(word_frequency)

print("\n-----13----\n")

#Unpacking: 1

numbers = (5, 2)
First, second = numbers
print(First)
print(second)
print("\n--------\n")
#Unpacking: 2
some_words = {'hello': 3, 'python': 9, 'bye': 1, 'computer': 2}
print (some_words.items())
some_words_items = [('hello', 3), ('python', 9), ('bye', 1), ('computer', 2)]

print("\n--------\n")

for something in some_words_items:
    print(something)

Fruits = ['apple', 'grape', 'banana']
Fruit_dict = {fruit:len(fruit) for fruit in Fruits}
print(Fruit_dict)

Fruits = ['apple', 'grape', 'banana']
Cost = [5, 4, 3]
result = dict(zip(Fruits,Cost))
print(result)
print(dict(zip(Fruits,Cost)))

Fruits = ['apple', 'grape', 'banana']
result = {index: value for index, value in enumerate(Fruits)}
print(result)


float_num = 12.235
string_num = str(float_num)
print(string_num)
print(type(string_num))

float_num = "43.89"
int_num = int(float("43.89"))
print(int_num)
print(type(int_num))

print("\n----1------\n")

prices = [35, 5888, 6, 3]
print(len(prices))