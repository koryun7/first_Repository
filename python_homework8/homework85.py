# You are given three lists, list1, list2, and list3. Your task is to implement a
# program that takes these lists and prints the following:

a = {1, 2, 3, 4, 5}
b = {1, 5, 6, 7, 8}
c = {1, 8, 9, 10}

# 1)The set of elements that are common to all three lists.
print(a & b & c)

# 2)The set of elements that are present in at least two of the three lists, but not in all three.
print((a | b | c)-(a ^ b ^ c))

# 3)The set of elements that are unique to each list (present in only one list)
print((a | b | c) - ((a | b | c) - (a ^ b ^ c)) - (a & b & c))



