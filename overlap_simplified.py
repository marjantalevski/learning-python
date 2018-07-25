def isprime(number):
    all_numbers = range(1, number + 1)
    divisors = []
    for element in all_numbers: 
        if (number % element == 0):
            divisors.append(element)
    if len(divisors) == 2:
        return True
    else:
        return False

def ishappy(number):
    i = 0
    check = number
    while i < 10:
        digits_num = [int(d) for d in str(check)]
        new_num = 0
        for el in digits_num:
            new_num += el*el
        check = new_num
        i += 1
    if check == 1:
        return True
    else:
        return False


numero = int(input("Enter the number to check: "))
print(isprime(numero))
print(ishappy(numero))