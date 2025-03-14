# an iterable is something that can be looped over

# an iterator is an object with a state such that it remembers where it is during iteration

# nums = [1, 2, 3]

# i_nums = nums.__iter__()
# or
# i_nums = iter(nums)
# print(i_nums)
# print(dir(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

# for num in nums:
#     print(num)


class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration

        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)
