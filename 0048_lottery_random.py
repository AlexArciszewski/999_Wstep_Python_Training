 #choice - zwraca losowy element
#choices - zwraca listę elementów i ma większe możliwości

songList = ["Title 1", "Title 2",  "Title 3",  "Title 4",  "Title 5", "Title 6", "Title 7", "Title 8", "Title 9"]

#random song choice
import random
print(random.choice(songList))

#choices lista elementów plus ustalenie prawdopodob. wystapienia

lottery = [ "boat", "car", "home", "happyMeal", "100millionDollars" ]
print(random.choices(lottery)) #same chances for every position
print(random.choices(lottery, k =50)) #same chances for every position k times
# to see the chances
from collections import Counter
print(Counter(random.choices(lottery, k = 100)))
#modify the chances for positions in list [1, 1, 1, 30, 1] x times srednia wazona
print(Counter(random.choices(lottery, [1, 1, 1, 30, 1], k = 100)))
#modify the chances for positions in list [0.8, 1.2, 0.05, 0.01, 10] x times srednia wazona ułamki inny zapis
print(Counter(random.choices(lottery, [0.8, 1.2, 0.05, 0.01, 10], k = 100)))