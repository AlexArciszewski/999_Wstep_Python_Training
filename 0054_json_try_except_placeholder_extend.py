"""
JSONplaceholder - miejsce zastępcze na Twoj przyszly json

Który użytkownik robi najszybciej rzeczy z listy do zrobienia.dane w postaci identyfikatora(unikalny element ktory sie nie powtarza) z json.add()Identyfikator użytkownika i zadania i treść zadania.
4 wartości klucz wartość:
identyfikator zadania ad1 identyfikator uzytkownika ad2 informacja tresc i informacja czy wykonane
r = requests.get("https://jsonplaceholder.typicode.com/todos") strona do testów


import requests


r = requests.get("https://jsonplaceholder.typicode.com/todos")
"""

import requests
import json
r = requests.get("https://jsonplaceholder.typicode.com/todos")

def   completed_TasksNumber_ByUser(tasks): #tworzymy słownik i wybieramy tego user'a który ma najwiecej completed
    completedTasksNumberByUser = dict() #tworzymy słownik i wybieramy tego user'a który ma najwiecej completed
    for entry in tasks:
        if(entry ["completed"] == True):
           try:                                                                                                                                                                                        #FUNKCJA nr2
               completedTasksNumberByUser [entry["userId"]] +=1
           except KeyError:
               completedTasksNumberByUser [entry["userId"]] =1               # za pierwszym razem wykona się to i rpzypisze jedynkę w kolejnych ma być +=1
    return completedTasksNumberByUser
def get_keys_wtih_top_values(dict):
    return[                      #funkcja do zwracania kluczy z najwyzszych wartosci
        key
        for(key, value)in dict.items()
        if value == max(dict.values())
    ]


def users_With_Top_Taask_score(completed_TasksNumber_ByUser):      #FUNKCJA NR 3
    
    usersIdWithmaxCompletedAmountOfTasks =[]  # lista na tych userów,którzy mają najwiecej tasków
    maxAmountofCompletedTask =max(completedTasksNumberByUser.values()) #zmienna z najwyzszą liczbą wykonanych tasków  Z TEGO FUNKCJA NR 3!
    for userId, numberOfCompletedTask in completedTasksNumberByUser.items():
        if(numberOfCompletedTask == maxAmountofCompletedTask):   #jak liczba wykonanych tasków równa sie najwyzszej liczbie wykonanych tasków to print user ID ktory laduje w liscie
            print(userId)
            usersIdWithmaxCompletedAmountOfTasks.append(userId) #dodajemy dane usera do bazy"""
    return usersIdWithmaxCompletedAmountOfTasks

print(r.text)
tasks = json.loads(r.text) #otrzymujemy tablice ze slownikami w srodku można np odczytać tasks[0]
print(tasks[0])
print(tasks[2])
print(tasks[10:22])
tasks2 =r.json() #wtedy nie trzeba importować json'a
print(tasks2[0])
print(tasks[0])

try:
    tasks = r.json()
except json.decoder.JSONDecodeError: #wyjątek dla json ale trzeba zaimportować znowu json
    print("Wrong format")
else:
    completedTasksNumberByUser = completed_TasksNumber_ByUser(tasks)  # zdef nr 2
    top_Users = (users_With_Top_Taask_score(completed_TasksNumber_ByUser))
    print(users_With_Top_Taask_score(completed_TasksNumber_ByUser))
    print(top_Users, "Get cookie")
    
    
    print("Format accepted")
    print(tasks2[0])
    print(tasks[0])
    #przetwarzamy interesujące nas dane teraz
    #3dajemy nagrodę tej osobie,która wykonała najwięcej zadań
    #słownik klucze user id klucz
    #sprawdzamy co jest w rekordach w tasks co tam faktycznie jest.add()
    """completedTasksNumberByUser = dict() #tworzymy słownik i wybieramy tego user'a który ma najwiecej completed
    for entry in tasks:
        if(entry ["completed"] == True):
           try:                                                                                                                                                                                        Z TEGO FUNKCJĘ NR2!
               completedTasksNumberByUser [entry["userId"]] +=1
           except KeyError:
               completedTasksNumberByUser [entry["userId"]] =1               # za pierwszym razem wykona się to i rpzypisze jedynkę w kolejnych ma być +=1"""
print(completedTasksNumberByUser)       #{1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12} wynik..
#print(completedTasksNumberByUser.items()) #lista z krotek user id liczba tasków
##print(completedTasksNumberByUser.values())    #wypsujemy wartości
#print(max(completedTasksNumberByUser.values())) #znajdujemy najwiekszaliczbe zrealizowanych taskow
"""usersIdWithmaxCompletedAmountOfTasks =[]  # lista na tych userów,którzy mają najwiecej tasków
maxAmountofCompletedTask =max(completedTasksNumberByUser.values()) #zmienna z najwyzszą liczbą wykonanych tasków  Z TEGO FUNKCJA NR 3!
for userId, numberOfCompletedTask in completedTasksNumberByUser.items():
    if(numberOfCompletedTask == maxAmountofCompletedTask):   #jak liczba wykonanych tasków równa sie najwyzszej liczbie wykonanych tasków to print user ID ktory laduje w liscie
            print(userId)
            usersIdWithmaxCompletedAmountOfTasks.append(userId) #dodajemy dane usera do bazy"""
        
    



"""
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print("Wszystko jest ok")
    print(tasks[0])

    
"""
