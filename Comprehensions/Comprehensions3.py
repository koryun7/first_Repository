# ● Vowels in a Word:
# ○ Create a list of vowels present in a given word.
def vowels_in_word(word):
    return [char for char in word if char.lower() in 'aeiou']


input = "hello"
result = vowels_in_word(input)

print(result)
