#generating random lists and printing them
import random
l1_range = range(50)
l2_range = range(50)
l1_length = 20
l2_length = 20
a = random.sample(l1_range, l1_length)
b = random.sample(l2_range, l2_length)
print(sorted(a))
print(sorted(b))

#finding overlaping elements and printing them
c = []
c = [el1 for el1 in a for el2 in b if el1 == el2 and el1 not in c]
print(sorted(c))