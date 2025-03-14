# li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# s_li = sorted(li, reverse=True)

# print("Sorted Variable: \t", s_li)

# li.sort()

# print("Original Variable: \t", li)

# tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# s_tup = sorted(tup)

# print(s_tup)

# di = {"name": "Corey", "job": "programming"}
# s_di = sorted(di)
# print(s_di)


# def func(val):
#     return val % 2


# li = [-6, -5, -4, 1, 2, 3]
# s_li = sorted(li, key=func)


# print(s_li)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name}, {self.age}, ${self.salary})"


e1 = Employee("Jamal", 27, 90000)
e2 = Employee("Yemi", 23, 60000)
e3 = Employee("Mide", 30, 120000)
e4 = Employee("Miracle", 25, 80000)

employees = [e1, e2, e3, e4]


def e_sort(emp):
    return emp.age


s_employees = sorted(employees, key=e_sort)

print(s_employees)
