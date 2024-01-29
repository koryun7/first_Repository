# ● Dictionary Merge:
# ○ Given two dictionaries, merge them into a new dictionary, excluding any keys
# that start with an underscore.
def merge_dictionaries(dict1, dict2):

    merge_dict = {k: v for k, v in {**dict1, **dict2}.items() if k[0] != '_'}

    return merge_dict


dict1 = {'apple': 5, 'banana': 6, '_orange': 8}
dict2 = {'grape': 5, 'kiwi': 3, '_pear': 4}
result = merge_dictionaries(dict1, dict2)

print("Merged Dictionary:", result)
