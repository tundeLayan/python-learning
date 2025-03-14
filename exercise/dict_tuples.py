import statistics
import math

# country_dict = {"china": 143, "india": 136, "usa": 32, "pakistan": 21}


# def dict_print(country_dict_arg):
#     for key, value in country_dict_arg.items():
#         print(f"{key}==>{value}")


# def dict_add():
#     new_country = input("Type in a country to add: ").lower()
#     if new_country in country_dict:
#         print("Country exists")
#         return
#     elif new_country not in country_dict:
#         new_country_population = input("Type in a population for the country: ").lower()
#         # new_data = {new_country: new_country_population}

#         # # how to add to dictionary
#         # country_dict[new_country] = int(new_country_population)
#         country_dict.update({new_country: int(new_country_population)})

#         print(country_dict)


# def dict_remove():
#     country_to_remove = input("Type in a country to remove: ").lower()
#     if country_to_remove in country_dict:
#         # del country_dict[country_to_remove]
#         country_dict.pop(country_to_remove)
#         dict_print(country_dict)
#         return
#     elif country_to_remove not in country_dict:
#         print("Country does not exist")
#         return


# def dict_query():
#     country_to_query = input("Type in a country to print its population: ").lower()
#     if country_to_query in country_dict:
#         print(country_dict[country_dict])
#     else:
#         print("Country does not exist!")


# def main():
#     type = input(
#         "Enter an input. It can be one of: \n -print \n -add \n -remove \n query\n"
#     ).lower()
#     if type == "print":
#         dict_print(country_dict)
#     elif type == "add":
#         dict_add()
#     elif type == "remove":
#         dict_remove()
#     elif type == "query":
#         dict_query()
#     else:
#         print("Error: Not a valid input")


# if __name__ == "__main__":
#     main()
# #######################################################################

# stock_data = {
#     "info": [600, 630, 620],
#     "ril": [1430, 1490, 1567],
#     "mtl": [234, 180, 160],
# }


# def dict_print2():
#     for key, value in stock_data.items():
#         # average_stock_prices = 0
#         # for price in value:
#         #     average_stock_prices += price
#         average_stock_prices = statistics.mean(value)

#         average_stock_prices = round(average_stock_prices / len(value), 2)
#         print(f"{key} ==> {value} ==> avg: {average_stock_prices}")


# def dict_add2():
#     new_stock = input("Enter stock ticker: ").lower()
#     price = input(f"Enter price for {new_stock}: ").lower()

#     if new_stock in stock_data:
#         stock_data[new_stock].append(price)
#     else:
#         stock_data[new_stock] = [int(price)]
#     print(stock_data)


# def main():
#     type = input("Enter an input. It can be one of: \n -print \n -add \n").lower()
#     if type == "print":
#         dict_print2()
#     elif type == "add":
#         dict_add2()
#     else:
#         print("Error: Not a valid input")


# if __name__ == "__main__":
#     main()

PI = math.pi


def circle_calc(radius):
    radius = int(input("Enter the radius: "))
    area = PI * (radius**2)
    circumference = 2 * PI * radius
    diameter = 2 * radius
    return area, circumference, diameter


if __name__ == "__main__":
    r = input("Enter a radius:")
    r = float(r)
    area, c, d = circle_calc(r)
    print(f"area {area}, circumference {c}, diameter {d}")
