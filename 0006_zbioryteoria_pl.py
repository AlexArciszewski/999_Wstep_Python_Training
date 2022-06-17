"""Zbiory"""
A = {1, 4, 20, -4, 20}
B = {2, 1, 25, 40, 20}

'''
A.add(7) #dodaj 7 unikalny element
print(A)
print(set(A))'''#jak na liscie chce miec unikalne wartosci czyli bez zduplikowanych. korzystamy z funkcji set

print(A&B) #czyli wspólne elementy
print(A|B)#wszystkie el unikalne bez powtórzeń tych samych 
print(A - B) #te co w A po odjęciu tych co w B
print(B -A)   #te co w B po odjęciu tych co w A
print(A^B)  #alternatywa wykluczajaca od wszystkich to co wspolne
#A.discard(1)-usuniecie pierwszej wartości tzn 2 od zera
#A.remove(24)-error jak nie ma tej wartosći
print(A.issubset(B))             #czy jeden zbiór-A jest podzbiorem-B 2 zbioru

"""Typy zagnieżdżone"""
imie = "Aleksander"
wiek = 38
płec = "mężczyzna"

imie = "Aleksandra"
wiek = 30
płec = "kobieta"

imie = "Olo"
wiek = 40
płec = "mężczyzna"

#krotka lub lista pozwala aby tego nie mieć ciagle w zmiennych

osoba1 =("Aleksander", 38, "mężczyzna")
osoba2 =("Aleksandra", 30, "kobieta")
osoba3 =("Olo", 38, "mężczyzna")

listaGosci =[
                ["Aleksander", 38, "mężczyzna"],
                ["Aleksandra", 30, "kobieta"],
                ["Olo", 38, "mężczyzna"]
            ]
