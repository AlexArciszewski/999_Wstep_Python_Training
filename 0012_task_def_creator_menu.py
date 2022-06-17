"""
Napisz program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
"""
definitions = {}
while(True):
    print("""This program adds new definitions, searches for existing definitions and\
allows user to delete selected definitions""")
    print('\n')
    print('MENU:')
    print('\n')
    print('\n')
    print('\n')
    print('To add new definitions press 1 button')
    print('\n')
    print('To search for definitions press 2 button')
    print('\n')
    print('To delete a definitions press 3 button')
    print('\n')
    print('For exit press 4 button')
    print('\n')
    choice = input('What operation you want to conduct? ')
    if (choice =="1"):
        print('User, please chose to add new definition: ')
        print('\n')
        key = input('Please write the key of the definition: ')                 #aby zapisać trzeba podać key i definition definition =definitions[key] 
        definition = input('Please write the definition you want to add: ')     #bedzie naszą wprowadzoną definicją więc jest równa
        definitions[key] = definition
        print('Your definition was added succesfully')
    elif (choice == "2"):
        print("User chose to search for existing definitons")
        key =input("What are you looking for?. Please input the key for the definition: ") #aby wyszukać wpisujemy klucz. Jeśli klucz 
        if key in definitions:                                                             #jest w definicji to podaje definitions[key]
            print(definitions[key])
        else:
            print("There is no definition with such a name: " ,key)                     #w innym razie nie ma klucza wiec nie ma definicji
    elif (choice =="3"):
        print("User chose to remove selected definition.")
        key =input("Which definition do you want to remove? Write the proper key: ")               #podajemy key, jak key jest w definitions to del definitions[key]
        if key in definitions:
            del definitions[key]
            print("Selected definition was terminated", key)
    elif(choice =="4"):
        print("Program will now exit. Have a nice day.")
        break   
    else:
        print("Operation forbidden")
        

