# MOVE AN ELEMENT IN THE LIST
# Your program should move the last element of the list to the beginning,
# meaning the last element of the list should become the first.
# The sequence of other elements should remain unchanged.
# An empty list or a list with only one element should remain unchanged.
# The number of elements in the list can be any – zero or more!

list_of_numbers = [12, 3, 4, 10, 8]
print("Initial list: " + str(list_of_numbers))

if 0 <= len(list_of_numbers) <= 1:
    print(list_of_numbers)
else:
    list_of_numbers.insert(0, list_of_numbers.pop())
    print("Changed list: " + str(list_of_numbers))


# First attempt using second list
# new_list_of_numbers = []
# if 0 <= len(list_of_numbers) <= 1:
#     print(list_of_numbers)
# else:
#     new_list_of_numbers.insert(0, list_of_numbers[-1])
#     list_of_numbers.remove(list_of_numbers[-1])
#     new_list_of_numbers.extend(list_of_numbers)
#     print(new_list_of_numbers)
