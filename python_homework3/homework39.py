#Append new stringin the middle of a given (even number of characteres) string.
x = "python"
print(x)
print(len(x))
z = "new"
y = x[:3] + z + x[-3:]
print(y)
print(len(y))