print("Program: break and continue with for loop if the number given is lower than zero program will be stopped")

score = 0
for i in range (3):
    x = int(input("Please give me the number: "))
    if (x > 0):
        score += x
    else:
        print("number is lower than 0. program will be stopped")
        break
    
print("Final score is: ", score)

