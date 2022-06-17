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
    print("Formataccepted")
    print(tasks2[0])
    print(tasks[0])








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
