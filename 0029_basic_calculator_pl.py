
print("Witaj!To jest prosty kalkulator napisany w PYTHON")
print("po podaniu liczb wybierzesz działanie, które chcesz przeprowadzić. ")
                                             #tu odwołujemy się do stringów nie integer!!!
a = int(input( "Podaj pierwszą liczbę: "))
b = int(input( "Podaj drugą liczbę: "))

wybór =input("Wybierz działanie, które chcesz wykonać: \
+.Dodawanie -.Odejmowanie *.Monożenie /.Dzielenie: ")
if (wybór == '+'):
    print("Wybrałeś dodawanie! Twój wynik to:" , ( a + b ))
elif (wybór == '-'):
    print("Wybrałeś odejmowanie! Twój wynik to:" , ( a - b ))
elif (wybór == '*'):
    print("Wybrałeś mnożenie! Twój wynik to:" , ( a * b ))
elif (wybór == '/'):
    if (b == 0):        #warunek na dzielenie przez 0 jak druga liczba to zero jest ostrzezenie else nie ma ostrzezenia i wynik
        print("nie dzielimy przez 0")
    else:
        print("Wybrałeś dzielenie! Twój wynik to:" , ( a / b ))
else:
    print("Nie dokonałeś prawidłowego wyboru")
    
