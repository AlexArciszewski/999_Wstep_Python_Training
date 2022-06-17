import requests
import json
import webbrowser
from pprint import pprint

params={
    "attach_bread" : "aege",
    "limit" : 3
    
}




r=requests.get("https://api.thecatapi.com/v1/images/search?breed_ids=",params)
try:
    content=r.json()
except json.decoder.JSONDecodeError:
    print("Wrong data format")
else:
    pprint(content)
    for catpics in content:
        pprint(catpics["url"])
        webbrowser.open_new_tab(catpics["url"])
input("press anything to end")

