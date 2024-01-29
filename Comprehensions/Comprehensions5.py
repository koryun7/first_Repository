# ● Filtering Word Lengths:
# ○ Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3.
def word_lengths(words):

    length_dict = {word: len(word) for word in words if len(word) > 3}

    return length_dict


word_list = ["table", "car", "computer", "Comprehension"]
result = word_lengths(word_list)

print(result)
