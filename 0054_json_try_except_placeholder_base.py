#pobieramy z jsona dane do slwonika i na dwa sposoby wyrzucamy rekordy ze slownika po user id z najwiekszymi wartosciami

import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")


try:
    tasks = r.json()
except json.decoder.JSONDecodeError: #wyjątek dla json ale trzeba zaimportować znowu json
    print("Wrong format")
else:
    completedTaskFrequencyByUser =dict()          #krok zero przejscie rpzez słownik
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] +=1 #za każdym innym razem plus jeden
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] =1 #(1sze rpzejscie)
            
        print(entry)
        print(completedTaskFrequencyByUser)
    print("Format accepted")
#powstaje słownik  z kluczami user id i liczba taskow pamietac o if try except i +=1 i =1   {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}  1krok
print(completedTaskFrequencyByUser.items()) #powstaje lista krotek para wartość dict_items([(1, 11), (2, 8), (3, 7), (4, 6), (5, 12), (6, 6), (7, 9), (8, 11), (9, 8), (10, 12)])krok 2 przez krotki rpzechodzimy petla for
userIdWithMaxCompletedAmountOfTasks = []   #lista 3 do powiekszenia
maxAmountofCompletedTask = max(completedTaskFrequencyByUser.values())
for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items(): #petla dla krotek krok 2 cd
    if (numberOfCompletedTasks == maxAmountofCompletedTask):   #krok 3 jesli numer zakonczonych zadan jet max to 
        userIdWithMaxCompletedAmountOfTasks.append(userId) # krok 3cd to powieksz liste
print(userIdWithMaxCompletedAmountOfTasks)
        




import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")
def countTaskFrequency(tasks): #przejscie przez słownik
    completedTaskFrequencyByUser =dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] +=1 #za każdym innym razem plus jeden
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] =1 #(1sze rpzejscie)
    return completedTaskFrequencyByUser
    print(entry)
    print(completedTaskFrequencyByUser)
    print("Format accepted")
#powstaje słownik  z kluczami user id i liczba taskow pamietac o if try except i +=1 i =1   {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}  1krok


def get_keys_with_top_values(my_dict):
    return    [
                key
                for (key, value) in my_dict.items()
                    if value ==max(my_dict.values())
            ]   

def users_with_top_completed_tasks(completedTaskFrequencyByUser):
    completedTaskFrequencyByUser = countTaskFrequency(tasks)
    userIdWithMaxCompletedAmountOfTasks = []   #lista 3 do powiekszenia
    maxAmountofCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTaskFrequencyByUser.items(): #petla dla krotek krok 2 cd
     if (numberOfCompletedTasks == maxAmountofCompletedTask):   #krok 3 jesli numer zakonczonych zadan jet max to 
        userIdWithMaxCompletedAmountOfTasks.append(userId) # krok 3cd to powieksz list
    return userIdWithMaxCompletedAmountOfTasks
    
 

#print(completedTaskFrequencyByUser.items()) #powstaje lista krotek para wartość dict_items([(1, 11), (2, 8), (3, 7), (4, 6), (5, 12), (6, 6), (7, 9), (8, 11), (9, 8), (10, 12)])krok 2 przez krotki rpzechodzimy petla for

    
    
    
    
    
try:
    tasks = r.json()
except json.decoder.JSONDecodeError: #wyjątek dla json ale trzeba zaimportować znowu json
    print("Wrong format")
else:
    completedTaskFrequencyByUser = countTaskFrequency(tasks)
    users_with_top_completed_tasks(completedTaskFrequencyByUser)
print( users_with_top_completed_tasks(completedTaskFrequencyByUser))