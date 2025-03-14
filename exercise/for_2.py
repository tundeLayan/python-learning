"""
After flipping a coin 10 times you got this result,

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

Using for loop figure out how many times you got heads

Print square of all numbers between 1 to 10 except even numbers
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
"""

# result = [
#     "heads",
#     "tails",
#     "tails",
#     "heads",
#     "tails",
#     "heads",
#     "heads",
#     "tails",
#     "tails",
#     "tails",
# ]

# count = 0

# for word in result:
#     if word == "heads":
#         count += 1

# print(f"We got heads {count} times")

# for i in range(10):
#     if i % 2 == 0:
#         print(i**2)


"""
Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message

"""

for i in range(5):
    if i == 4:
        print("Congratulations on finishing your race")
        break
    # answer = input("are you tired?")
    # if answer == "yes":
    #     print("you didn't finish the race")
    #     break
    # elif answer == "no":
    #     continue

print(i)
