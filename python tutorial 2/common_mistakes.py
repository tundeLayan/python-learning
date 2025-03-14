nums = [11, 30, 44, 54]
nums2 = [1, 2, 3, 4]

# nums3 = nums.extend(nums2)

identities = zip(nums, nums2)

print(list(identities))

for identity in identities:
    print("{} is actually {}!".format(identity[0], identity[1]))
