"""
napisz program, który wyświetli liczby od 1 do 100 oraz kwadraty tych liczb. Kwadrad liczby jest bezpośrednio pod daną liczbą(np dla liczby 2 
liczba) będzie w wierszu niżej. Czas 10 minut
"""
liczba=0
for liczba in range(101):
    print(liczba)
    liczba2=(liczba**2)
    print(liczba2)



x_list=[]
i = 0
while i<100:
    x_list.append(i)
    i += 1
    print(i)
    j = (i**2)
    print(j)
