print("This program finds all divisors of a number.")
num = int(input("Enter an integer: "))
all_numbers = range(1, num)
divisors = []
for number in all_numbers: 
    if (num % number == 0):
        divisors.append(number)
print(divisors)
