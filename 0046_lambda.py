#lambda gdy funkcja przy filtrowaniu jest uzywana nie wiecej niz raz.

def podw (x):
    return x * 2
print(podw (4))


lambda x:  x * 2                         #funkcja bez nazwy ale ma parametry
dzialanie = lambda x:  x * 2

print(dzialanie (5))

print((lambda x : x *2)(4))

list01 =[ 5, 10,  22, 133, 69, 99, 27, 83, 2140]

list01_filtered = list(filter(lambda x: x % 2 == 0, list01) )
print(list01_filtered)
list01_filtered2= list(filter(lambda x: x % 2 == 1, list01) )
print(list01_filtered2)

list01 =[ 5, 10,  22, 133, 69, 99, 27, 83, 2140]

def filterr (x):
    if( x % 2) == 0:
        return x

list01_filtered3 = list(filter(filterr, list01) )
print(list01_filtered3)