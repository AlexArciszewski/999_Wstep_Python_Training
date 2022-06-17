
import requests
import json
import webbrowser
from pprint import pprint


print("This program shows some random information about cats or dogs")
print("\n")
choose =input("""Choose cat or dog: 
For a cat press 'c'.
For a dog press 'd'.""")
if (choose == 'c'):
    print("The random information about the cats was chosen")
    params ={
        "amount" : 10,
        "animal_type" : "cat"
        
    }
    b = requests.get("https://cat-fact.herokuapp.com/facts/random", params)
    try:
        content = b.json()
    except json.decoder.JSONDecodeError:
        print("Wrong data format or data error")
    else:
        
        pprint(content)
    for cat in content:
        print(cat["text"])
    
elif (choose =='d'):
    print("The random information about the dogs was chosen")
    params ={
            "amount" : 10,
            "animal_type" : "dog"
        
    }
    a = requests.get("https://cat-fact.herokuapp.com/facts/random", params)
    try:
        content =a.json()
    except json.decoder.JSONDecodeError:
        print("Wrong data format or data error")
    else:
        pprint(content)
        for dog in content:
            print(dog["text"])
else:
    print("Operation not allowed!")