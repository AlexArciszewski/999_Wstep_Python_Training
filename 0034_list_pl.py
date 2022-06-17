
"""
#Operations    
# in
# not in
"""

List = ["Olo", "Aleksander","Ania", "Kuba", "Tomek"]
Numbers = [1,5,10,60,4]

#czy imie jest na liście
print("Aleksander" in List) #zwraca tue czyli jest

print("Dorota" in List)

if ("Aleksander" in List): #czy imie jest wewnatrz listy
    print("Cześć Aleksander")

if (2 not in Numbers):       #czy liczba 2 nie znajduje sie w liscie numbers
    print("nie ma liczby 2")

#działania
print(3*Numbers)
print([3,10,10,0,-3] +Numbers)

    
