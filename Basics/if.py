time = input("What's the time? ")

if int(time) < 12:
    print("Good morning!")

elif int(time) < 18:
    print("Good afternoon!")
else:
    print("Good evening!")


