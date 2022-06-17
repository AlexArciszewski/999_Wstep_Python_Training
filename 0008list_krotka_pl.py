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
#w liscie kazdy elemeent nie jest wartoscią a listą listaw  wliscie nie trzeba robic zmiennych
    #listGosci[0][0] to Aleksander
listaGosci =[
                ["Aleksander", 38, "mężczyzna"],
                ["Aleksandra", 30, "kobieta"],
                ["Olo", 38, "mężczyzna"]
            ]
#Zmiany sa możliwe np podajemy listę do tego położenie i po znaku równości nowe dane
listaGosci[0][0] = "Tomek"
#krotka szybsza nawiasy zwykle dodawanie nowych elementow lista[nawias krotka( nizej przykład
listaGosci2 = [
                ("Aleksander", 38, "mężczyzna"),
                ("Aleksandra", 30, "kobieta"),
                ("Olo", 38, "mężczyzna")
               ]
#dodanie do krotki
listaGosci2.append(("Jurek", 35, "meżczyzna"))

#krotka w krotce szybciej

listaGosci3 = (
                ("Aleksander", 38, "mężczyzna"),
                ("Aleksandra", 30, "kobieta"),
                ("Olo", 38, "mężczyzna")
               )


#dodanie add
#dodanie listy do listy "|" unikalne wartosci wypisuje czyli powtarzajace sie nie sa 2 razy
listaGosci4 = {
                ("Aleksander", 38, "mężczyzna"),
                ("Aleksandra", 30, "kobieta"),
                ("Olo", 38, "mężczyzna")
               }


listaGosci5 = {
                ("Alek", 38, "mężczyzna"),
                ("Toma", 30, "kobieta"),
                ("Wlodek", 32, "mężczyzna")
               }

listaGosci6 = listaGosci4 | listaGosci5
#dodanie listy do listy "|" unikalne wartosci wypisuje czyli powtarzajace sie nie sa 2 razy


#Czy ktoś sie podwójnie nie zapisał!! "&"
listaGosci7 = {
                ("Aleksander", 38, "mężczyzna"),
                ("Aleksandra", 30, "kobieta"),
                ("Olo", 38, "mężczyzna")
               }


listaGosci8 = {
                ("Aleksander", 38, "mężczyzna"),
                ("Toma", 30, "kobieta"),
                ("Wlodek", 32, "mężczyzna")
               }

#łaczenie dwóch list
listaGosci9 = listaGosci7 & listaGosci8



listaGosci11 = {
                ("Alek", 38, "mężczyzna"),
                ("Toma", 30, "kobieta"),
                ("Wlodek", 32, "mężczyzna")
               }


listaGosci12 = {
                ("Alek", 38, "mężczyzna"),
                ("Toma", 30, "kobieta"),
                ("Wlodek", 32, "mężczyzna")
               }

listaGosci13 = listaGosci11 & listaGosci12
print(listaGosci13)






