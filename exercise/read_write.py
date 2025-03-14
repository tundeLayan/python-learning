import csv

"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
You have to read this file in your python program and find out words with maximum occurrence.
"""

# hash_map = {}
# with open("poem.txt", "r") as f:
#     words = f.read().split()
#     for word in words:
#         if hash_map.get(word):
#             hash_map[word] += 1
#         else:
#             hash_map[word] = 1
#         pass

# # print(hash_map)
# word_occurrences = list(hash_map.values())
# max_count = max(word_occurrences)
# print("Max occurrences of any word is:", max_count)


# print("Words with max occurrences are: ")
# for word, count in hash_map.items():
#     if count == max_count:
#         print(word)
#######################################################################

"""
stocks.csv contains stock price, earnings per share and book value. 
You are writing a stock market application that will process this file and 
create a new file with financial metrics such as pe ratio and price to book ratio. 
These are calculated as,
"""
with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
    out.write("Company Name,PE Ratio, PB Ratio\n")
    next(f)
    for line in f:
        tokens = line.split(",")
        stock = tokens[0]
        price = float(tokens[1])
        earning_per_share = float(tokens[2])
        book_value = float(tokens[3])
        pe_ratio = round(price / earning_per_share)
        price_to_book = round(price / book_value)
        out.write(f"{stock},{pe_ratio},{price_to_book}\n")
