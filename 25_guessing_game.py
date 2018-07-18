import math

upper_boundary = 101
lower_boundary = 0
guess = int(((upper_boundary - 1 ) + lower_boundary) / 2)
counter = 1

input("Think of a number between 0 and 100 and click any key to continue... ")

print("Is your number " + str(guess) + "?")
answer = input("y/n?: ")
while answer == "n":
    previous_guess = guess
    print("Is the number smaller than " + str(guess) + "?")
    compare = input("y/n?: ")
    if compare == "y":
        upper_boundary = guess
        guess = int(math.ceil(((lower_boundary + upper_boundary) / 2)))
    else:
        lower_boundary = guess
        guess = int(math.floor(((lower_boundary + upper_boundary) / 2)))
    print("Is your number " + str(guess) + "?")
    counter += 1
    answer = input("y/n?: ")
    if guess == previous_guess:
        answer = "y"
        counter -= 1
        print("It actually must be or you are cheating!")

print("Gotcha! Your imagined number: " + str(guess))
print("Amount of guesses it took this PC: " + str(counter))
