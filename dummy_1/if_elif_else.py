import datetime

now = datetime.datetime.now()
current_hour = now.hour

# these are our greetings!
# puchi puchi
if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good Afternoon!")
elif 17 <= current_hour < 20:
    print("Good Evening!")
else:
    print("Good Night!")

