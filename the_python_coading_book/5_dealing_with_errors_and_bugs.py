from typing import List, Dict

'''>>> "hello" * 2.5
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'

You get the same error message in this example. When you multiply a string by a float, Python doesn’t know what to do.
It gives you an error. You get the same error if you try to multiply a list by a float, and indeed any data type which is a sequence will give the same error:

 [34, 45, 23, 12] * 2.5
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'

The error message complains about trying to multiply by a non-integer.
That’s because sequences can be multiplied by integers:

"hello" * 2
'hellohello'

[34, 45, 23, 12] * 2
[34, 45, 23, 12, 34, 45, 23, 12]'''

items = {"Coffee": 2.2, "Tea": 1.5, "Chocolate": 2.5}

for item in items.keys():
     income = 0
     qty = input(f"How many {item}s have you sold? ")
     qty = int(qty)
     income = income + qty * items[item]
print(f"\nThe income today was £{income:0.2f}")



