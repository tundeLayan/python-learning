# def calculate_area(base, height, shape_type="triangle"):
#     if shape_type == "rectangle":
#         return base * height
#     elif shape_type == "triangle":
#         return (base * height) / 2
#     else:
#         print("Error: Shape is neither triangle nor rectangle")
#         return None


# area = calculate_area(2, 2, "rectangle")
# print(area)


def print_pattern(no_of_lines=5):
    for i in range(no_of_lines + 1):
        for j in range(i):
            print("*", end="")
        print(end="\n")


print_pattern(10)
