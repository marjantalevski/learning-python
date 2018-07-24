import random

#generating a random, sorted list
def generate_list(span, length):
    the_list = sorted(random.sample(range(span), length))
    return the_list

#linear search
def find_element(any_list, sought_element): 
    for element in any_list:
        if element == sought_element:
            the_index = any_list.index(element) 
            return the_index
    return False

#binary search
def binary_search(any_list, sought_element):
    start_index = 0 
    end_index = len(any_list) - 1
    while(start_index <= end_index):
        middle_index = int((start_index + end_index) / 2)
        if any_list[middle_index] == sought_element:
            return middle_index
        else:
            if sought_element < any_list[middle_index]:
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1
    return False

#if it is not imported!
if __name__=="__main__":
    which_element = int(input("Please enter an element to look for: "))
    
    a = generate_list(60, 20)
    print(a)

    if find_element(a, which_element) == False:
        print("The element is not there.")
    else:
        print("Index of the element: " + str(find_element(a, which_element)))
    
    if binary_search(a, which_element) == False:
        print("The element is not there.")
    else:
        print("Index of the element: " + str(binary_search(a, which_element)))