print('Program will select even numbers from the list below')
 
numbers = [ 1, 10, 15, 23, 25, 36 ]
evenNumbers =[]
for number in numbers:
    if (number % 2 ==0):
        evenNumbers.append(number)
print(numbers)
   
print('Option number 2. Easier way to select even numbers')  
numbers2 = [ 1, 10, 15, 23, 25, 36 ]
evenNumbers2  =  [ number 
                                for number in numbers2
                                if (number  % 2 == 0)
                                ]
print(numbers2)