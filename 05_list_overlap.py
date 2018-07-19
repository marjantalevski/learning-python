#importing the library
import random

#defininig variables for lists length and range of values
list_length1 = 20
list_length2 = 20
values_range1 = range(40)
values_range2 = range(40)

#generating random lists and declaring c which will store the overlaping values
a = random.sample(values_range1, list_length1)
b = random.sample(values_range2, list_length2)
c = []

#just so I can compare them visually
print(sorted(a))
print(sorted(b))

#checks for same elements and appends them to c if they aren't there already
for element1 in a:
    for element2 in b:
        if element1 == element2 and element1 not in c:
            c.append(element1)

#prints the overlaping values list
print(sorted(c))
            
