#Operatory porównania i instrukcja warunkowa if oraz wcięcia:

a = int(input())
b = int(input())
if (a > b):
    print("PRAWDA")  # jak a ><b to wyświetli prawda a ajak nie to nic
elif (a < b):           #else if jak a.b to ok prawda a jak nie to falsz
    print("FALSZ")
else:
    print("a = b")
