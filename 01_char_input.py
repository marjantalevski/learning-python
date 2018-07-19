import datetime
#importing time, so I can run this program using the current year anytime
#defining current time, so I can use the current year later

now = datetime.datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
message = name + ", you will turn 100 in the year of " + str((now.year - age + 100)) + "."
print(message)