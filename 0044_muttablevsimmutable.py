"""
    obiekt to zmienna, która ma więcej możliwości,
    można wywołać na nim "funkcje"
    może mieć więcej niż 1 wartość
    
    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmmienne
    mutable - zmienny

    = ZMIANA miejsca wskazywania na nowy adres, na inny obiekt
"""
a =4 #to jest obiekt będący zmienną a jest obiektem typu int i jest immutable niezmienny
# a. (ctrl+spacja) to mamy menu funkcji przypisanych do obiektu funkcja wywołana z kropką to metoda
print(a.bit_length())

listSample = [1, 4, 512, 24]
listSample2 = listSample
listSample2.append(465)
print(listSample)            #---->[1.4.512, 24,465]

print(listSample2)           #---->[1.4.512, 24,465]

listSample = [1, 4, 512, 24]
print(id(listSample))

b = 4 
print(id(a)) #id jest takie samo wszedzie 2814325154048
c = b
print(id(a))
c = 7
print(id(a))
print(b, c)
c = b           #id jest  różne dla c=b i c=7 2690139816272 i 2690139816368
print(id(c))
c = 7       #przy immutable jak liczby
print(id(c)) # znak =  zmiana miejsca przypisania miejsce wskazywania na nowy adres czyli na inny obiekt.
                  # append nie zmienia miejsca wskazywania na nowy adres


listSample3 = [2,5,7,13,25,46]
listSample4 = listSample3         #to są mutalble obiekty znak równosci tworzy nowe powiazanie

print(id(listSample3))
listSample4[0] =33

print(id(listSample4),"brak zmiany po zmianie elementu")

k = 4
print(id(k))
h = 4
print(id(h), "hk")
j = 5
print(id(j))
def add(j,  amount = 1):
    print(id(j))
    j = j + amount
    print(id(j)) # tu jest inna wartość
add(j)
print(j)

x = 4
y = x
print(id(y))
y = 7
print(id(y))
print(y)

e =5
print(id(e))
def add7(e, amount = 1):
    print(id(e))
    e = e +amount
    print(id(e))
print(add7(e))

def append_element_to_list(listka, element):
    print(id(listka), "listka3")
    listka.append(element)
    print(id(listka),"listka2")

print(id(listSample),"listka1")
print(append_element_to_list(listSample,5))

def append_element_to_list2(listka2, element):
    print(id(listka2), "listka3")
    listka2 = [2, 4, 20]
    print(id(listka2),"listka2")

print(id(listSample),"listka1")
print(append_element_to_list2(listSample,5))