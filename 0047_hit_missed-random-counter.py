import random
print(random.random())
print(random.randrange(0, 20, 4))
print(random.randrange(10))
print(random.randint(0, 13))
import random
e = 0
while e < 100:
    e = e+1
    print(random.uniform(0,100))

def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance= random.uniform(0,100)
    if(isHitChance < weaponChanceToHitPercentage):
        return "HIT"
    else:
        return "MISSED"
print(will_weapon_hit(50))
import random
x=0
listHit = []
while x <100:
    x =x +1
    listHit.append(will_weapon_hit(50))
print(listHit)
print(listHit.count("HIT"))
print(listHit.count("MISSED"))
from collections import Counter
dictionaryHit  = Counter(listHit)
print(dictionaryHit)
"""
y =0 
while y < 100:
    y = y +1
    print(random.randrange(10))
    print(random.randint(0,10))

"""
