#checking if a number is even and a multiple of four
number = int(input("Please enter an integer: "))
if (number % 2 == 0 and number % 4 == 0):
    print("The number is even and a multiple of 4")
if (number % 2 == 0 and number % 4 != 0):
    print("The number you have entered is even.")
if (number % 2 != 0):
    print("The number you have entered is odd.")

#checking if a number is a multiple of another number
num = int(input("Please enter the first number: "))
check = int(input("Please enter another number: "))
if (check % num == 0):
    print("The second number you entered is a multiple of the first one you did.")
else:
    print("The second number you entered is not a multiple of the first one you did.")