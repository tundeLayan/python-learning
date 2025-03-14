class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_name(self):
        print(f"My name is {self.name}")

    def display_employee_detail(self):
        print(f"ID: {self.id} \nName: {self.name}")


employee1 = Employee(30, "Jamal")
employee1.display_employee_detail()

del employee1.id

# print(employee1.id)

try:
    print(employee1.id)
# except AttributeError as err:
except AttributeError as err:
    print(err)

del employee1

try:
    employee1.display_employee_detail()
except NameError as err:
    print(err)
