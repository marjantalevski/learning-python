import random

game = "yes"
guess = -1

while(game == "yes"):
    try:
        counter = 0 #counter is here so it resets each new game
        a = random.randint(1, int(numbersrange)) 
        while guess != a:
            guess = input("Your guess: ")
            if guess == "quit":
                break
            counter += 1
            if int(guess) == a:
                print("Congrats! You have guessed it!")
                print("Number of guesses you took: " + str(counter))
                print("Hope you had fun playing!")
                break
            elif int(guess) > a:
                print("Incorrect, try a smaller number.")
            elif int(guess) < a:
                print("Incorrect, try a larger number.")
    except:
        print("Invalid input! Start over if you'd like.")
    game = input("Another game - yes or no: ")
print("Hope you had fun playing this game!")