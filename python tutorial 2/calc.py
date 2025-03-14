def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    # try:
    #     if y == 0:
    #         raise ValueError("Cannot divide by zero")
    # except ValueError as e:
    #     if e == "Cannot divide by zero":
    #         raise ValueError("Cannot divide by zero")
    #     # print("e", e)
    # else:
    #     return x / y
    if y == 0:
        raise ValueError("Cannot divide by zero")

    return x / y


# print(divide(10, 0))
