from enum import IntEnum

Menu_Crypto = IntEnum( 'Menu_Crypto', 'Bitcoin , Ethereum , Solana , Cardano , Chia , Polygon , Harmony , DogeCoin ')
print(list(Menu_Crypto))
print('\n')
print("Enumeration training. Not a financial advice. Program made for training and fun. Enjoy")
print('\n')
Choose = int(input(""""Choose your favourite Crypto:
                   
1. Bitcoin
 
2. Ethereum

3. Solana
 
4. Cardano

5. Chia
 
6. Polygon

7. Harmony

8.DogeCoin
"""))
if (Choose == Menu_Crypto.Bitcoin):
    print("Just Buy The Dip and HODL")
elif(Choose ==Menu_Crypto.Ethereum):
    print(" Still waiting for POS? What a nice gas fee you got here")
elif (Choose == Menu_Crypto.Solana):
    print("Check if you still have your Crypto")            
elif ( Choose == Menu_Crypto.Cardano):
    print("HAHAHAHAHA")
elif(Choose == Menu_Crypto.Chia ):
    print("You lost money on hard drives didn't you? Supply and Demand just remember that") 
elif(Choose == Menu_Crypto.Polygon):
    print(" Nice project but it won't hit the 5 USD")
elif (Choose == Menu_Crypto.Harmony):
    print("Nice but where is the moon? 20 cents per coin HA!")
elif(Choose == Menu_Crypto.DogeCoin):
    print("To the moon was not about the rocket. Still sending Tweets to Elon?")   
else:
     print("Operation forbidden. Program will now end") 