n1 = input("Enter first player's name: ")
n2 = input("Enter second player's name: ")
e1 = input(n1 + " choose rock, papper or scissors: ")
e2 = input(n2 + " choose rock, papper or scissorss: ")

#working with functions
def compare(name1, name2, entry1, entry2):
    if entry1 == entry2:
        return("It's a tie!") 
    elif entry1 == "rock": 
        if entry2 == "papper":
            return(name2 + " wins the game!")
        elif entry2 == "scissors":
            return(name1 + " wins the game!")
    elif entry1 == "papper":
        if entry2 == "scissors":
            return(name2 + " wins the game!")
        elif entry2 == "rock":
            return(name1 + " wins the game!")
    elif entry1 == "scissors":
        if entry2 == "papper":
            return(name1 + " wins the game!")
        elif entry2 == "rock":
            return(name2 + " wins the game!")
    else:
        return("Invalid input from at least one of the users! Try again.")

print(compare(n1, n2, e1, e2))