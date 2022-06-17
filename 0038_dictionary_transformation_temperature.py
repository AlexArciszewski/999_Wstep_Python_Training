"Dictionary transformation data--->dictionary" #wyrażenie słownikowe skracamy zamiast robić pętli jak w wyrażeniach listowych

Celsius = { 't1':-50,  't2': -20,  't3': 0,  't4': 25,  't5': 40, 't6': 80 } 

Farenheit = {
    key: Celsius *1.8 +32
    for key, Celsius in Celsius.items()
    if Celsius  >  10  #warunek że chcę aby podawało temperatury >10 
}
print(Farenheit)
print(Celsius.items())   # -krotka