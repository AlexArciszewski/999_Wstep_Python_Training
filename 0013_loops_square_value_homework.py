#Homework
# Square values from 1 to 100. Is there only one way to complete the task?

print("Option 1")
newlist = [i**2 for i in range(1, 100)]
print(newlist)

print("Option 2")
squares1 = []
for x in range(100):
    squares1.append(x**2)
print(squares1)

print("Option 3")
squares = list(map(lambda x: x**2, range(100)))
print(squares)
