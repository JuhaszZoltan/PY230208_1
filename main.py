from module import Diak

diakok:list[Diak] = []

file = open(file='diakok.txt', mode='r', encoding='utf-8')
for sor in file: diakok.append(Diak(sor))

m:int = 0
for i in range(1, len(diakok)):
    if diakok[i].magassag > diakok[m].magassag:
        m = i

print(f'a legmagasabb diák neve: {diakok[m].vezeteknev} {diakok[m].keresztnev} ({diakok[m].magassag} cm)')

lanyok:list[Diak] = []
for diak in diakok:
    if diak.nem == 'lány':
        lanyok.append(diak)

m:int = 0
for i in range(1, len(lanyok)):
    if lanyok[i].tti > lanyok[m].tti:
        m = i

print(f'a legkövérebb lány: {lanyok[m].vezeteknev} {lanyok[m].keresztnev}')
print(f'magasság: {lanyok[m].magassag} cm; súly: {lanyok[m].suly} kg; tti:{round(lanyok[m].tti, 2)} kg/m^2')