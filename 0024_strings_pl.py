imie = "Aleksander"

nazwisko = "Arciszewski"
#print(imie + nazwisko) pierwszy sposób za imieniem spacja #imie = "Aleksander " lub:

#print(imie + " " + nazwisko) ew dodać 3 zmienna suma tych dwóch czyli pełne = imie + nazwisko

pelne = imie + " " + nazwisko

print(pelne) 


długistring = "asdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbgjklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafklsdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbgjklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafklsdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbgjklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafklsdghasdklgkl"
#dlugistring = "asdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhb\
#gjklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklg\
#hafklsdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbg\
#jklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafkl\
#sdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbgjklashbvg\
#ajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafklsdghasdklgkl"

print(długistring)

abrakadabrastring = """asdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhb
gjklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklg
hafklsdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbg
jklashbvgajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafkl
sdghasdklgklasdfhiosdfhiohgrhasdfkghadfhbgadfgasdfklghasjklhbgjklashbvg
ajklbgjkaghjklahgbvahgklasghklahgklahklghlakghaxfnhjklghafklsdghasdklgkl""" # """tekst""" podzielony enterami bedzie w wierszach jak chcemy stringwieloliniowy

print(abrakadabrastring)


print(abrakadabrastring[1])#nawias kwadratowy w print zmiennej oznacza literę uwaga;1 litera pozycja 0 a ostatnia to -1 przedostatnia -2 ...dobre do wykrywania imion....jak [:] dwukropek to wypisze całe słowo [1:] podaje wszystkie elementy bez pierwszego
print(abrakadabrastring[-1]) #wszystkie prócz ostatniego
print(abrakadabrastring[:])
print(abrakadabrastring[1:3]) #wszystko od pozycji 1(druga litera) do 3 bez 3 czyli 1 i 2
