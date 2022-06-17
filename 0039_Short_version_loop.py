print("Squared values of numbers in numbers list")

numbers= [ 1, 10, 15, 23, 25, 36 ]
squareValue = []
for number in numbers:  
    squareValue.append(number**2)
print(squareValue)

print("Option no. 2 Easier solution")

squareValues = [number**2
                for number in numbers]
print(squareValues)