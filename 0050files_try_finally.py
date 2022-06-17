"""file = open("testujewyj.txt", "w") #handle uchwyt
file.write("sample ")

file.write("sample")

print(0/0) #program się wykonuje do error print90/00 dzielenie rpzez zero jak będzie ten wiersz miedzy sample jednym a drugim to wykona tylko tego nad nim i zapisze do pliku
file.close() 
"""
try:
    file = open("testujewyjtryfin.txt", "w") #handle uchwyt
    file.write("sample ")
    print(0/0)  #program się wykonuje do error print90/00 dzielenie rpzez zero jak będzie ten wiersz miedzy sample jednym a drugim to wykona tylko tego nad nim i zapisze do pliku
    file.write("sample")
finally:  #dzieki finally zapis do pliku jest wykonany mimo error
    file.close() 
    
    
try:
    file = open("testujewyjtryfin.txt", "w") #handle uchwyt
    file.write("sample ")
    print(0/0)  #program się wykonuje do error print90/00 dzielenie rpzez zero jak będzie ten wiersz miedzy sample jednym a drugim to wykona tylko tego nad nim i zapisze do pliku
    file.write("sample")
finally:  #dzieki finally zapis do pliku jest wykonany mimo error
    file.close() 