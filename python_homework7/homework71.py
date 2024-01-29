# Arrange string characters such that
# lowercase letters should come first.\

word  = "PyNaTive"
lower = ""
upper = ""
for i in word:
    if i.islower():
        lower += i
    else:
        upper += i
print(lower + upper)

