print("Math calculator ver 1.2. by Alex Arciszewski")
print("Choose numbers for calculations")

a = int(input("Please give the first number: "))

b = int(input("Please give the second number: "))
print("Chosen numbers are: ", a, "and" , b,)
Calculation = input("""Choose mathematical operation: For addition press '+'\
For substraction press '-'\
For multiplication press '*'\
For division press '/'\
For square root press 'sa' or 'sb'\
For exponentiation press 'ea'\
For exponentiation press 'eb'\
For the absolute value press'ma'\
For the absolute value press'mb'""")      #ok czy dzielenie nie powinno być z floatem? 2/4 to 0.5 do sprawdzenia,sprawdzone dodawanie i modul poprawic tekst ktory sie rozjechal,exp zła funcka
if (Calculation == '+'):
    print("Addition was chosen. Calulation result is: ", ( a + b))
elif (Calculation == '-'):
    print("Substraction was chosen. Calulation result is: ", ( a - b))
elif (Calculation == '*'):
    print("multiplication was chosen. Calulation result is: ", ( a * b))
elif (Calculation == '/'):
    if(b == 0):
        print("Operation not allowed!")
    else:
        print("Divison was chosen. Calulation result is: ", ( a / b))
elif (Calculation == 'sa'):
    if(a <0):
        print("Operation not allowed!")
    else:
        from math import sqrt
        print("square root of the first nuber was chosen. Calculation result is:", sqrt(a))
elif (Calculation == 'sb'):
    if(b <0):
        print("Operation not allowed!")
    else:
        from math import sqrt
        print("square root of the second nuber was chosen. Calculation result is:", sqrt(b))            
elif (Calculation == 'ea'):
     from math import exp
     print("exponentiation of the first number was chosen. Calculation result is:", exp(a))
elif (Calculation == 'eb'):
     from math import exp
     print("exponentiation of the second number was chosen. Calculation result is:", exp(b))
elif (Calculation == 'ma'):
    from math import fabs
    print("absolute of the first number was chosen. Calculation result is:", fabs(a))
elif (Calculation == 'mb'):
    from math import fabs
    print("absolute of the second number was chosen. Calculation result is:", fabs(b))
else:
    print("Operation not allowed!")
