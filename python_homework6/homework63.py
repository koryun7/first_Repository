#Write a program that takes a list of words and a target word as input.
#The program should find and print all words in the list that contain the
#target word. Use a for loop, the in operator, and an if statement to
#check if the target word is present in each word in the list.

list_1 = ["Hello", "America", "Sweden", "Long", "Logo"]
x = input("Enter your symbol: ")
list_2 =[]
for i in list_1:
    if x in i:
        list_2.append(i)
print(list_2)