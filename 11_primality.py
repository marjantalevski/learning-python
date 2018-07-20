def check_primality(n):
    all_numbers = range(1, n+1)
    divisors = []
    for element in all_numbers: 
        if (n % element == 0):
            divisors.append(element)
    if len(divisors) == 2:
        print("The number you entered has only two divisors, therefore it is a prime number.")
        print("These are the divisors: " + str(divisors))
    else: 
        print("The number you entered has more than two divisors, therefore it is not a prime number.")
        print("These are the divisors: " + str(divisors))

number = int(input("Enter an integer: "))
check_primality(number)