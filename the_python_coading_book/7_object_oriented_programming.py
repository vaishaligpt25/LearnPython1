# Python is inherently an object-oriented programming language. However, you’ll often see Python described as a multi-paradigm language.
# This means that it’s a language that supports many different programming styles, including object-oriented programming.

items = ["Coffee", "Tea", "Chocolate", "Sandwich"]
cost_price = [1.1, 0.5, 0.9, 1.7]
selling_price = [2.5, 1.5, 1.75, 3.5]
stock = [30, 50, 35, 17]

# item_sold = input("Enter item sold: ").title()
# print(item_sold)
# print(type(item_sold))
# quantity = int(input("Enter quantity sold: "))
# item_index = items.index(item_sold)
# print(item_index)
#
# print("\n------1------\n")
#
# score = 2
# score = score + 1
# print(score)
#
# print("\n------2------\n")
#
# score = 2
# score += 2
# print(score)
#
# print("\n------3------\n")
#
# score = 3
# score -= 1
# print(score)

print("\n------4------\n")

items = ["Coffee", "Tea", "Chocolate", "Sandwich"]
cost_price = [1.1, 0.5, 0.9, 1.7]
selling_price = [2.5, 1.5, 1.75, 3.5]
stock = [30, 50, 35, 17]

item_sold = input("Enter item sold: ").title()
quantity = int(input("Enter quantity sold: "))
item_index = items.index(item_sold)
profit = quantity * (selling_price[item_index] - cost_price[item_index])
daily_income = 0
daily_income += selling_price[item_index] * quantity
stock[item_index] -= quantity
print(profit)
print(daily_income)
print(stock[item_index])
