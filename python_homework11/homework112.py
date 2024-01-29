# 2.Letters Count
# Write a Python function to calculate count of each letter in string
# {a: 5, b: 2, r: 2, k: 1, d: 1}
def calculate_letter(str_count):
    result = {}
    for i in str_count:
        key = result.keys()
        if i in key:
            result[i] += 1
        else:
            result[i] = 1
    return result


print(calculate_letter("abrakadabra"))
