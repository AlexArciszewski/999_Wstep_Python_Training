#Homework
#Even numbers fromt he list

liczby = [1, 2, 3, 4, 5, 6]
liczbyparzyste = []
for cyfra in liczby:
    if  (cyfra %  2 == 0):
        liczbyparzyste.append(cyfra)
print(liczbyparzyste)


liczbyparzyste2 = [cyfra
                  for cyfra in liczby
                    if(cyfra %  2 == 0)]
print(liczbyparzyste2)
                  