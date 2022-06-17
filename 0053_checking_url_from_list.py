import requests

print("Web search program")
def listFromBoss(path):
    try:
        with open(path, "r", encoding ="UTF =8") as file:
            return file.read().split()
    except FileNotFoundError:
        print("No such file or directory")
fileName = input("Please give me the name of the file where the list is located: ")
listContent = listFromBoss(fileName)
print(listContent)
webListCorrect = []
webListInCorrect = []
for webs in listContent:
    webPageResponse = requests.get(webs)
    if (webPageResponse.status_code == 200):
        print("Web page: ", webs, "exists")
        print("True")
        webListCorrect.append(webs)
    elif (webPageResponse.status_code==404):
        print(" Web page",webs, "does not exist")
        print("FALSE")
        webListInCorrect.append(webs)
    else:
        print("Oooops something went wrong")
print("Summary")
print("Websites that exist: ", webListCorrect) 
print("Websites that do not exist: ", webListInCorrect) 