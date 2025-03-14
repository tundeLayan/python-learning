"""
Create a Dictionary which contains the Binary values mapping with 
numbers found in the below integer and binary and save it in binary_dict.
"""

# integer = [0, 1, 2, 3, 4]
# binary = ["0", "1", "10", "11", "100"]
# binary_dict = {}

# for index, val in enumerate(integer):
#     binary_dict[val] = binary[index]

# print(binary_dict)

# or
# z = zip(integer, binary)
# binary_dict = {integer: binary for integer, binary in z}


"""
Create a List which contains additive inverse of a given integer list. 
An additive inverse a for an integer i is a number such that: a + i = 0

"""
# originalList = [1, -1, 2, 3, 5, 0, -7]
# additive_inverse = [-1*i for i in integer]

# or

# additive_inverse = []


# for val in originalList:
#     a = 0 - val
#     additive_inverse.append(a)

# print(additive_inverse)


"""
Create a set which only contains unique squares from a given a integer list.
"""
integer = [1, -1, 2, -2, 3, -3]
# sq_set = set()

# for val in integer:
#     sq_set.add(val**2)

# or

sq_set = {i * i for i in integer}

print(sq_set)
