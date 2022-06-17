#program ma sumowa� pierwsze 4 liczby pobrane od u�ytownika:
# = int(input("podaj liczb�: "))
#wynik = 0     #podajemy zero bo kazda liczba ma sie zapisywac poczynaj�c od zera....0-pusto...dodajemy liczby kt�re tu bed� zapisane
#wynik += x    



#1. wynik = 0 zmienna opisuj�ca gdzie zapisujemy wynik wynik poczatkowy jest zero aby tu przechowywac liczby podane przez uzytkownika czyli x zero jest neutralne obliczeniowo
#2. i = 0      tworzymy zmienn� okreslaj�ca liczb� pot�rze� p�tli. Jest na pocz�tku 0 a ma by� max 4 bo maj� by� 4 razy podane liczby
#3. tworzymy p�tle cia�o p�tli:
    #while i < 4:                      3a czy i<4 tak bo i=0
    #x = int(input("Podaj liczb�: "))  3b u�ytkownik podaje liczb�(input)
    #wynik += x                        3c warto�� wyniku jest powiekszana o liczb� X
    #i += 1                            3d liczba i=0 teraz jest i=0+1 i<4 to p�tla jest powtarzana.

wynik = 0 
i = 0      
while i < 4:
    x = int(input("Podaj liczbe: ")) 
    wynik += x  
    i += 1    
print("Wynik dodawania liczb to: ", wynik)
 
