#Write a program that prompts the user to enter a word and checks if it is
#a palindrome. A palindrome is a word that reads the same backward as
#forward. Use string slicing and an if-else statement to compare the
#original word with its reverse.

word = input("Write your word: ")
n = len(word)//2
n_1 = word[n:]
n_2 = word[n+1:]
if word[:n] == n_1[::-1]:
    print("It's a palindrome!")
elif word[:n] == n_2[::-1]:
    print("It's a palindrome!")
else:
    print("It's a not palindrome!")
