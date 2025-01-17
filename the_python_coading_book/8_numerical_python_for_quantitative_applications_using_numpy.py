marks = [25, 42, 33, 23, 14, 22]
print(marks * 2)
#print(marks * 1.5)
#Indeed, multiplication of lists only works if you multiply by an integer. If you try to multiply by a non-integer, an error is raised:

print("\n----1-----\n")

new_marks = []
for mark in marks:
    new_marks.append(mark * 2)
print(new_marks)

#print(new_marks + 10)
#The TypeError states that a list cannot be concatenated with an integer but only with another list. This error lets you know that, when used with lists, the + sign adds the elements of a list to the end of the other list:
list1 = [2, 4, 3]
list2 = [4, 6, 3]
print(list1 + list2)

print("\n----2-----\n")
# add 10 marks to each marks:-
new_marks =[]
for marks in marks:
    new_marks.append(marks + 10)
print(new_marks)

print("\n----3-----\n")
# USING LISt COMPREHENSION:

marks = [25, 42, 33, 23, 14, 22]
print([mark + 10 for mark in marks])
print([mark * 10 for mark in marks])
print([mark * 10 + 10 for mark in marks])