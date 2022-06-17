"Dictionary transformation data--->dictionary" #wyrażenie słownikowe skracamy zamiast robić pętli jak w wyrażeniach listowych
names = { 'Alex',  'Barbara', 'Cecil', 'Dorothy',  'Eve' }
numbers = [1,7,10,13,23,25,36,49]
Celsius = { 't1':-50,  't2': -20,  't3': 0,  't4': 25,  't5': 40, 't6': 80 } 
namesLength ={                                                                           # 1.co jest kluczem. 2 skąd wyberamy elementy pętla for zazwyczaj
name :len(name)
for name in names   
} 
print(namesLength)