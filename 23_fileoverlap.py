#function for testing if number is prime
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

#function for testing if number is happy
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

prime_file = open("prime_numbers.txt", "w")
happy_file = open("happy_numbers.txt", "w")

numero = int(input("Enter the upper limit: "))

#writing all the primes and happies to .txt files
j = 1
while j <= numero:
    if isprime(j): prime_file.write(str(j) + "\n")
    if ishappy(j): happy_file.write(str(j) + "\n")
    j += 1

prime_file.close()
happy_file.close()

#reading from the text files and finding overlaps
primeslist = []
with open("prime_numbers.txt") as primesfile:
    line = primesfile.readline()
    while line:
        primeslist.append(int(line))
        line = primesfile.readline()

happieslist = []
with open("happy_numbers.txt") as happiesfile:
    line = happiesfile.readline()
    while line: 
        happieslist.append(int(line))
        line = happiesfile.readline()

happyprimeslist = []
for element in primeslist:
    if element in happieslist:
        happyprimeslist.append(element)

#printing all lists
print("List of the prime numbers up to " + str(numero) + ": " + str(primeslist))
print("List of the happy numbers up to " + str(numero) + ": " + str(happieslist))
print("And a list of the happy primes up to " + str(numero) + ": " + str(happyprimeslist))