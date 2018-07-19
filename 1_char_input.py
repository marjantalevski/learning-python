import datetime
#importing time, so I can run this program using the current year anytime
#defining current time, so I can use the current year later

now = datetime.date.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name + ", you will turn 100 in the year of " + str((now.year - age + 100)) + ".")