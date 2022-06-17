#  1    Sum numbers from 1 to 5 and show the score:15 3 different ways

def sum_numbers(number):
    
    sum = 0
    
    for number in range(1, 6):
        sum = sum + number
        
    return(sum)
print(sum_numbers(5))


# # Sum numbers from 1 to 5 and show the score:15 3 different ways but if you need to change the number as example 300

def sum2_numbers2(number2):
    
    sum2 = 0
    
    for number2 in range(1, number2 + 1):
        sum2 = sum2 + number2
        
    return(sum2)
print(sum2_numbers2(5))

# 2      2nd Option 

def sum3_numbers3(number3):
    return sum([number3 for number3 in range(1, number3 +1)]) #generator number3 w petli a później zwraca sumę 
print(sum3_numbers3(5))

#3              #3rd Option

def sum4_numbers4(number4):
   return(1+ number4) / 2 * number4       #suma ciagu arytmetycznego (a1 +a2)*n/2
print(sum4_numbers4(5))
    
    
"""   
    sum3 = 0
    for number3 in range(1, number3 + 1):
        sum3 = sum3 + number3
        
    return(sum3)
print(sum3_numbers3(5))
"""






