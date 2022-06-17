
import requests

response = requests.get("http://videokurs.pl/")
print(response)  #<Response [200]> to znaczy że ciagnął jak nie znajdzie to <Response [404]-page not found
#zwracamy obiekt czyli cos co ma okreslone wlasciwosci
response.status_code  #pokazuje czy nalazł czy nie
#print(response.text)