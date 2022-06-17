import sys
print('Generator vs list')
"""
EvenNumbersInRange1000000 = [ number
                                                    for number in range(10000)
                                                    if (number %2 ==0)
                                                    ]
print(EvenNumbersInRange1000000)
"""
EvenNumbersInRange1000000generator = ( number2
                                                                    for number2 in range(10000)
                                                                    if (number2  % 2 == 0)
                                                                    )
print(EvenNumbersInRange1000000generator)
"""
print(sys.getsizeof(EvenNumbersInRange1000000))
"""
print(sys.getsizeof(EvenNumbersInRange1000000generator))
"""
for numbers in EvenNumbersInRange1000000generator:
    print(numbers)
""" 