#Python wyciaganie danych petlami


people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }
"""
[('IcFDG2bO9AYDF651DoyH', {'name': 'John', 'age': 27, 'sex': 'Male'}),
 ('KcD9ntE6IRM59vkVta1k', {'name': 'Marie', 'age': 22, 'sex': 'Female'}),
 ('yDlgcn99xPc19mYXcRmy', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('cpQh6GiAbBdGv35NDoTk', {'name': 'Nabeel', 'age': 17, 'sex': 'Male'}),
 ('12BifzWxCQySKgLhgahC', {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'}),
 ('QLnmg0pzlLj9x7c7DlLv', {'name': 'Ruby', 'age': 55, 'sex': 'Female'}),
 ('To47urX0DUznWmOxGZ6H', {'name': 'Lori', 'age': 27, 'sex': 'Male'}),
 ('KQ4bir3y4tlkbG69I7zq', {'name': 'Marie', 'age': 42, 'sex': 'Female'}),
 ('94cp4hsyZP2BnCh4D34z', {'name': 'Agness', 'age': 25, 'sex': 'Female'}),
 ('Vr4wRdkljeEs46Czxo54', {'name': 'Chiara', 'age': 17, 'sex': 'Male'})]

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]


for name, age, sex in ppllist2:
    print(name)

"""

for id, dictionary in people.items():
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])


people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]
#key to w kazdym wierszu to id
#people lista ze slownikami
#value 25 np
people3 = ["Arkadiusz",
           "Wiola",
           "Kuba"
          ]


ratings1 = {
            "Arkadiusz": (2,1,2,3,2,3),
            "Agness": (4,2,1,3,4)           
           }    
ratings2 = [
        {'name': "Arkadiusz", 'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        {'name': "Agness", 'ratings': (4,2,1,3,4), 'behaviour': 2}
    ]

ratings3 = {
        "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behaviour': 4},
        "Agness:": {'ratings': (4,2,1,3,4), 'behaviour': 2}
    }

#1.wyciaganie :Arkadiusz i AGNES" z ratings1 imiona sa key

for key in ratings1:
    print (key)

#2 wyciaganie ocen z ratings1 musimy wydrukować ratings1 oceny key(czyli uczniow) key w nawiasie kwadratowym
for key in ratings1:   #petladziała tylerazy ile jest kluczy ratings1 czyli imiona
    print(ratings1[key])
#2a to samo tylko ze lepiej. klucz to"Arkadiusz" ratings1 to pojemnik z danymi
for key in ratings1:
    print(key, "oceny otrzymane: ", ratings1[key])
#3a people 3 wypisanie samych wartosci z listy
for value in people3:
    print(value)
#4 wypisuje słowniki z listy[] people 2 czyli te 3 wiersze
for value in people2:
    print(value)
#4a wypisuje słowniki z list[]people 2 czyli te 3 wiersze

#petladziała tylerazy ile jest kluczy wpeople czyli imionaw słowniku i to garnia slownik
#for key in people2:
#    print(people2[key])

for value in people2: # to wypisuje słowniki z listky[] czyli to lista
    print(value)

for value in people2:
    for value in people2: 
        print(value)
    
for record in people2:   #dla każdego rekordu czyli słownika w liscie[]people2(pojemniku)czyli ta petla wykona się 3 razy
    for key in record:   #dla klucza(name sex age itp) w rekordach czyli słwonikach
        print(key, value[key]) #wypisuj klucze i wartości przypisane do kluczy
"""poniżej tłumaczenie tego co w zielonym:

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},           #record1
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},        #record2
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}        #record3           
        ]
"""


#5.Wypisac dane ze słownika w słownika poniżej:

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }

#5.1 wypisujemy co zawiera ten słownik print(people) i smietnik pokazuje
#print(people)
 #{'IcFDG2bO9AYDF651DoyH': {'name': 'John', 'age': 27, 'sex': 'Male'},
 #'KcD9ntE6IRM59vkVta1k': {'name': 'Marie', 'age': 22, 'sex': 'Female'},
 #'yDlgcn99xPc19mYXcRmy': {'name': 'Agness', 'age': 25, 'sex': 'Female'},
 #'cpQh6GiAbBdGv35NDoTk': {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
 #'12BifzWxCQySKgLhgahC': {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
 #'QLnmg0pzlLj9x7c7DlLv': {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
 #'To47urX0DUznWmOxGZ6H': {'name': 'Lori', 'age': 27, 'sex': 'Male'},
 #'KQ4bir3y4tlkbG69I7zq': {'name': 'Marie', 'age': 42, 'sex': 'Female'},
 #'94cp4hsyZP2BnCh4D34z': {'name': 'Agness', 'age': 25, 'sex': 'Female'},
 #'Vr4wRdkljeEs46Czxo54': {'name': 'Chiara', 'age': 17, 'sex': 'Male'}}

print("5.2", people['IcFDG2bO9AYDF651DoyH'])



#for key in record:   #dla klucza(name sex age itp) w rekordach czyli słwonikach
#        print(key, value[key]) #wypisuj klucze i wartości przypisane do kluczy


        

#for value in people2:
#    for key in value:
#        print(key, value[key])
    

"""
print(people["IcFDG2bO9AYDF651DoyH"])

for key in people:
    print("ID:", key)
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])


for key in ratings1:
    print(key, "oceny", ratings1[key])


for dictionary in people2:
    for key in dictionary:
        print(key, ":", dictionary[key])
        
 """








