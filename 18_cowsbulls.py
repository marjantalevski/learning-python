import random

print("--------------------------------------------------------")
print("This program generates a 4 digit integer.")
print("Guessing a number on a wrong location gives you 1 cow.")
print("Guessing a number on a correct location gives you 1 bull.")
print("If you guess the whole number, you win the game.")
print("--------------------------------------------------------")

cow = 0
bull = 0
d = []

a = random.randint(1000, 9999) #generate a random number
b = [int(x) for x in str(a)] #transform into a list

while d != b:   
    c = input("Enter a four digit integer: ")
    d = [int(x) for x in str(c)] #transform into a list

    for el1 in b: 
        for el2 in d: 
            if el1 == el2 and b.index(el1) != d.index(el2):
                cow += 1
            if el1 == el2 and b.index(el1) == d.index(el2):
                bull += 1 
    
    print("Bulls: " + str(bull) + "\n" + "Cows: " + str(cow))
    bull = 0
    cow = 0
    
print("Congrats you have won the game!")
