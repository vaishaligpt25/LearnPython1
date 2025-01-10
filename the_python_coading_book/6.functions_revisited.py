#Functions can be used as input arguments for other functions

'''def do_something():
    print("This function is not the most interesting one you will ever write!")


def repeat_five_times(function_name):
    for count in range(5):
        print(f"Function call {count + 1}")
        function_name()'''


some_number = [4, 6, 34, 1, 5]
output = some_number.append(100)
print(output)
print(some_number.append(100))

Name = "harry"
print(Name.upper())

print("\n-------1------\n")
contacts = [
    {
        "First Name": "Clark",
        "Last Name": "Kent",
        "Email": "super@superman.com",
        "Superpowers": ["Flight", "Super Strength", "Super Speed"],
    },
    {
        "First Name": "Sherlock",
        "Last Name": "Holmes",
        "Email": "elementary@holmes.com",
        "Colleague": "Dr Watson",
    },
    {
        "First Name": "Yoda",
        "Last Name": None,
        "Email": "my_email_this_is@jedi.com",
        "Colour": "green",
    },
]


def add_person(first name, Last name):
   contacts.append({"First Name": first name, "Last Name": Last name)