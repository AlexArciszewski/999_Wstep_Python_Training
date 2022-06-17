
def evil_function(toBeDestroyedList):
    toBeDestroyedList.clear()

myList = [1, 4, 2, 1, 52, 3]

evil_function(myList) 
print(evil_function(myList)) 
print(myList)  
print("kopia")
def evil_function2(toBeDestroyedList2):
    toBeDestroyedList2[0] =4

myList2 = [1, 4, 2, 1, 52, 3]
evil_function2(myList2)
print(myList2)

print('ID zmienne listy 2 sa kopie siebie"')
def evil_function3(toBeDestroyedList3):
    print(id(toBeDestroyedList3))

myList3 = [1, 4, 2, 1, 52, 3, 50, 69]
print(id(myList3))
evil_function3(myList3.copy())

print("czyszczenie listy")
def evil_function4(toBeDestroyedList4):
    print(id(toBeDestroyedList4))
    toBeDestroyedList4.clear()
    print(toBeDestroyedList4) #sprawdzamy czy wyczyszczono
myList4 = {1, 4, 2, 1, 52, 3, 50, 69,72}
print(id(myList4))
evil_function4(myList4.copy())
print(myList4)
#robimy kopie ID się zmienia
def evil_function7(toBeDestroyedList7):
    print(id(toBeDestroyedList7))
    toBeDestroyedList7[0] = 4
    
myList7 = [1, 4,2,1,52,3,111,121]
print(id(myList7))
evil_function7(myList7.copy())
print(myList7)

#nie robimy kopii takie samo ID
def evil_function8(toBeDestroyedList8):
    print(id(toBeDestroyedList8))
    toBeDestroyedList8[0] = 4
    
myList8 = [1, 4,2,1,52,3,111,121]
print(id(myList8))
evil_function8(myList8)
print(myList8)


#robimy kopie ID sie zmienia kopia plytka
print('robimy kopie ID się zmienia')
def evil_function7(toBeDestroyedList7):                #def funkcji(funkcja beadaca lista lub setem)
    print(id(toBeDestroyedList7))                             #drukowanie id funkcji
    toBeDestroyedList7.clear()                                   #czy [0] =999 czy clear(0 co robimy z f) 
    
myList7 = {1, 4,2,1,52,3,111,121}                         #set{} lib []lista czylit o co funkcja ma robic
print(id(myList7))                                                   #sprawdzenie id tej funkcji dotyczacej listy lu seta
evil_function7(myList7.copy())                              #funkcja z def polaczana z listą[]/setem{} opcja copy
print(myList7)
                                                            

#robimy kopie ID pojedynczego el sie nei zmienia  kopia płytka
print('robimy kopie ID poj elementu sie nie zmienia')
def evil_function11(toBeDestroyedList11):               
    print(id(toBeDestroyedList11[0]))                            
    toBeDestroyedList11.clear()                                  
    
myList11 = [1, 4,2,1,52,3,111,121]                       
print(id(myList11[0]))                                         
evil_function11(myList11.copy())                          
print(myList11)


print("int is immutable czyli dopiero zmiana adresu po zmianie elementu w liscie-płytka kopia")
def evil_function13(toBeDestroyedList13):               
    print(id(toBeDestroyedList13[0]))     #adres 1285686755568                       
    toBeDestroyedList13[0] =  666
    print(id(toBeDestroyedList13[0]))   #zmiana elementu zmiana adresu na 1285687793712
    print(toBeDestroyedList13)                                 
    
myList13 = [1, 4,2,1,52,3,111,121]                       
print(id(myList13[0]))                               #adres 1285686755568          
evil_function13(myList13.copy())                          
print(myList13)
#kopiowanie głębokie aby sie nie nadpisaly oryginal i kopia po zmianie elementu import copy
import copy

print("mutable")
def evil_function14(toBeDestroyedList14):               
    print(id(toBeDestroyedList14))     #adres nr1                       
    toBeDestroyedList14[0][0] =  666

    print(toBeDestroyedList14)                                 
    

myList14 = [[1, 4], [2, 1], [52, 3], [111, 121]]                 
print(id(myList14))                               #adres nr 2 inny on nr1          
evil_function14(copy.deepcopy(myList14))                          
print(myList14)


import copy

print("immutable kopia inny zapis")
def evil_function15(toBeDestroyedList15):               
    print(id(toBeDestroyedList15))                           
    print(toBeDestroyedList15)                           
    
myList15 = [1, 4, 2, 1, 52, 3, 111, 121]                       
print(id(myList15))                                       
evil_function15(list(myList15))                          
print(myList15)


import copy

print("immutable kopia inny zapis 2")
def evil_function16(toBeDestroyedList16):               
    print(id(toBeDestroyedList16))                           
    print(toBeDestroyedList16)                           
    
myList16 = [1, 4, 2, 1, 52, 3, 111, 121]                       
print(id(myList16))                                       
evil_function16((myList16[:]))                          #zamiast list [:] przeslanie listy jako kopie bez jej zmiany
print(myList16)
