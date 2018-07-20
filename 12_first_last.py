import random

#function that generates a random list
#r1 is the range of the values in the list
#l1 is the length of the randomly generated list
def random_list_generator(r1, l1): 
    the_list = random.sample(range(r1), l1)
    return the_list

#function which makes a new list with first and last element of any list
def first_last(any_list):
    new_list = [any_list[0], any_list[len(any_list)-1]]
    return new_list

#passing values to the generator function and returning the generated list
#can't access the generated list directly, have to define the returned value 
the_list = random_list_generator(10, 5) 
print(the_list)

#passing values to the cutting function and returning a two element list
#can't access the generated list directly, have to define the returned value
new_list = first_last(the_list) 
print(new_list)

