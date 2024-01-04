
# s1 = "aaaaabbc"
# num_left = len(s1)

# count = Counter(list(s1))
# print(count) # Counter({'a': 5, 'b': 2, 'c': 1})

# most_freq = max(count, key=count.get) # a
# print(most_freq)

# num_left = num_left - count[most_freq]
# # check if the len(most_freq) <= rest + 1

# if count[most_freq] <= num_left + 1:
#     print("true")
# else:
#     print("not possible")

# most_common_keys = count.most_common() # [('a', 5), ('b', 2), ('c', 1)]
# print(most_common_keys)

# print(most_common_keys.pop(0))
# print("Now: ")
# print(most_common_keys)

# # Extract keys from the tuples:
# keys_in_order_of_frequency = [key for key, _ in most_common_keys] 
# print(keys_in_order_of_frequency) # ['a', 'b', 'c']
