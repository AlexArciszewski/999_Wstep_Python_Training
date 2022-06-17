print("seek,tell")
print("\n") 
with open("0051oceany.txt", "r", encoding ="UTF-8") as file: 
    print(file.readline())      #odczytuje pierwszy wiersz i czeka  kursor na drugim na poczatku
    print(file.tell())             #zwraca liczbę gdzie się zatrzymalismy po readline. Odczytalismy 1 wiersz mial 20 znakow to na 20 jest z uwzględnieniem 2 na \n
    print(file.readline())      #odczytuje pierwszy wiersz i czeka  kursor na drugimna poczatku
    print(file.tell())
    print(file.seek(4)) 
    print(file.readline())
    