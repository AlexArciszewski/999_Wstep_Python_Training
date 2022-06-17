


print(" Guess the number. If it's lower or higher the program will give you a feedback. You have 7 chances. Ready Stedy GO!")
secretNumber = int(13)
i = 0
for i in range (7):
    x = int(input("Please give the number: "))
    """if x = str:
        print("Please give numbers not letters")"""    
    if x > secretNumber:
        print("Chosen number is too high. Please try again")
    elif x < secretNumber:
        print("Chosen number is too low. Please try again")
    elif x == secretNumber:
        print("BINGO! you guessed the number. the secret number is: ",secretNumber)
        break
    else:
        print("Operation forbidden")
    

