"""
  LEGB
  Local, Enclosing, Global, Built-in
"""

import builtins

# print(dir(builtins))

x = "global x"


# def test():
#     global x
#     x = "local x"
#     print(x)

# test()
# print(x)


def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "inner x"
        print(x)

    inner()
    print(x)


outer()
