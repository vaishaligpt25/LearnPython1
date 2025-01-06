import random

'''player_name = input("What is your name? ")
print(player_name + ", can you find the goblin?")
goblin_position = 3

guessed_position = input("Can you guess where the goblin is hiding?")

is_monday = True
if is_monday:
  print("Have a great day!")

day = "Tuesday"
if day == "Monday":
    print("Have a great day!")
else:
    print("bad day")

day = "thursday"
if day == "Monday":
    print("correct 1")
elif day == "Tuesday":
    print("correct 2")
elif day == "wednesday":
    print("correct 3")
else:
    print("True")

day = "monday"
if day == "monday":
    print("correct1")
print("correct 2")

print("\n------1-----\n")

day = "Tuesday"
if day == "Monday":
  print("Have a great week")
print("Get back to work now")

print("\n------2-----\n")
a_number = 12
print(a_number)

my_number = input("enter the value")
my_value = int(my_number)
print(my_value *2)

my_number = input("enter the value")
print(my_number * 2)

print("\n------3-----\n")

print("Hey, Good morning")
my_name = input("What is your name?")
print(my_name + ",How are you?")
harry_position = 3
guessed_position = input("What is the position of harry? ")
guessed_position = int(guessed_position)
if guessed_position == harry_position:
 print("Well done")
else:
 print("not good.")

print("\n------4-----\n")
person_name = input("What is your name?")
print(person_name * 2)

print("\n------5-----\n")
my_age = input("what is your age?")
#my_age = int(my_age)
print(my_age * 2)

print("\n------6-----\n")

print("Hey, Good morning")
my_name = input("What is your name?")
print(my_name + ",How are you?")
harry_position = random.randint(1,10)
while True:
  guessed_position = input("What is the position of harry? ")
  guessed_position = int(guessed_position)
  if guessed_position == harry_position:
    print("Well done")
  else:
    print("not good.")

print("\n------7-----\n")

print("Hey, Good morning")
my_name = input("What is your name?")
print(my_name + ",How are you?")
harry_position = random.randint(1,10)

keep_trying = True

while keep_trying:
  guessed_position = input("What is the position of harry? ")
  guessed_position = int(guessed_position)

  if guessed_position == harry_position:
    print("Well done")
    keep_trying = False
  else:
    print("not good.")'''

print("\n------8-----\n")

number_of_doors = 5
print("Hey, Good morning")

my_name = input("What is your name?")
print(my_name + ",How are you?")

harry_position = random.randint(1, number_of_doors)

keep_trying = True

while keep_trying:
  guessed_position = input("What is the position of harry? ")
  guessed_position = int(guessed_position)

  if guessed_position == harry_position:
    print("Well done")
    keep_trying = False
  else:
    print("not good.")





