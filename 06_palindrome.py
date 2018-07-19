text = input("Enter something and find out if it's a palindrome: ")

#this is a build in function to reverse a list/string
reversedtext = text[::-1] 
if text == reversedtext:
    print("It is! Backwards it reads " + reversedtext + " as well.")
else:
    print("It is not a palindrome. Backwards it reads " + reversedtext + ".")