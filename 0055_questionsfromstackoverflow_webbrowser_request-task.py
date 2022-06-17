"""
Test:
Napisz program, który wybierze pytania ze stackoverflow 
i posegreguje je w określony sposób czyli: 
a) pytania mające minimum 25pkt, 
b) pytania posegregowane malejąco,
c) pytaniapochodzą z ostatniego tygodnia, 
d) pytania dotyczą tylko kategorii Python.
"""
import json
import webbrowser  # moduł do otwierania stron www
import requests
from datetime import datetime, timedelta #dla zapisu datetime a nie datetime.datetime czy datetime.timedelta
import pprint   #aby dane jakoś wyglądały
#https://api.stackexchange.com/docs/questions#order=desc&sort=activity&filter=default&site=stackoverflow   try it tab parametry z tabeli wybierać
print(timedelta(weeks =1))
#print(timedelta(days =7, hours=13))  cas w postaci , zemożna go odejmowac od datetime.
timeBefore = timedelta(weeks =1)
print(datetime.today())

searchDate = datetime.today() - timeBefore
print("Time for search is: ", searchDate)
"""
Time stamp od 01.01.1970  pomiar czasu w sekundach. Wynik to float a searchdate floata nie przyjmie
    
    
    
 """
print("wanted time measured in seconds starting grom 1970-01-01 is: ", searchDate.timestamp())
print("wanted time measured in seconds starting grom 1970-01-01 is: ", int(searchDate.timestamp()))
params = {
    "site" : "stackoverflow",                    #strona
    "sort" : "votes",                                 #sortowanie wg głosów
    "order" : "desc",                                #rodzaj sortowania desc czyli malejące
    "fromdate" : int(searchDate.timestamp()),               #od daty t mozna dać zamiast daty"2022-06-07"  time stamp po rzutowaniu do inta int(searchDate.timestamp()))
    "tagged" : "python",                            #otagowanie
    "min" : 25                                            #  wybieramy min score wg info z discussion  This method allows you make fairly flexible queries across the entire corpus of questions on a site. For example, getting all questions asked in the the week of Jan 1st 2011 with scores of 10 or more is a single query with parameters sort=votes&min=10&fromdate=1293840000&todate=1294444800. 
}


r =requests.get("https://api.stackexchange.com/2.3/questions/", params)      #  url 2.3 to ver Questions pytania params =parametry i je trzeba wypisać wyżej w klamrze{}

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong data format")
else:
    #pprint.pprint(questions)
    for question in questions["items"]:
        pprint.pprint(question["link"]) #można odwoływac się do konkretnych kluczy w nawiasach kwadratowych dostaniemy: https://stackoverflow.com/questions/72568719/if-python-strings-are-immutable-why-does-it-keep-the-same-id-if-i-use-to-app' 'https://stackoverflow.com/questions/72596436/how-to-perform-approximate-structural-pattern-matching-for-floats-and-complex' 'https://stackoverflow.com/questions/72598852/getcacheentry-failed-cache-service-responded-with-503'
        webbrowser.open_new_tab(question["link"]) #otweiranie adresu url w przeglądarce ustawionej na główną

