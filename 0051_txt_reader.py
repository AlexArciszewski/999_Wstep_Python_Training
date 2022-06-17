
def loading(fileName):
    print("Data loading program")

dataList = []
fileName = input("Enter the name of the file you want to load: ")
with open(fileName, "r", encoding= "UTF-8") as file:
    for data in file:
        try:
            dataList.append(data.replace("\n", ""))
        except FileNotFoundError:
            print("No such file or directory")
print("Data received from a file: ", fileName, "Result:", dataList)

print(loading(fileName))