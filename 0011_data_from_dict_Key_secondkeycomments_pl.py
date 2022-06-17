#Practice:Get the data from the dictionary


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

#5.1 wypisujemy co zawiera ten słownik print(people) i pokazuje
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
#5.2
print("5.2", people['IcFDG2bO9AYDF651DoyH'])

# wyswietla: 5.2 {'name': 'John', 'age': 27, 'sex': 'Male'}

#5.3
for key in people: #dla klucza do slownika wydrukuj klucz
    print(key)

#wyswietla
#IcFDG2bO9AYDF651DoyH
#KcD9ntE6IRM59vkVta1k
#yDlgcn99xPc19mYXcRmy
#cpQh6GiAbBdGv35NDoTk
#12BifzWxCQySKgLhgahC
#QLnmg0pzlLj9x7c7DlLv
#To47urX0DUznWmOxGZ6H
#KQ4bir3y4tlkbG69I7zq
#94cp4hsyZP2BnCh4D34z
#Vr4wRdkljeEs46Czxo54

for key in people:
    print("ID: ", key)
    for secondaryKey in people[key]:
        print(secondaryKey, people[key][secondaryKey])
    
