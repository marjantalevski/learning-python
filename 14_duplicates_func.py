#using loops
def remove_duplicate(any_list):
    new_list = []
    for i in any_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

#using sets
def remove_duplicate_set(any_list):
    return list(set(any_list))

the_list = [0, 0, 1, 1, 5]
print(the_list)

result1 = remove_duplicate(the_list)
print(result1)

result2 = remove_duplicate_set(the_list)
print(result2)