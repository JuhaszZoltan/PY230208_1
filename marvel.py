from marvel_module import Film

filmek:list[Film] = []
file = open(file='marvel.txt', mode='r', encoding='utf-8')
for s in file: filmek.append(Film(s))

print(f'3.1: {len(filmek)} filmje van a marvel moziverzumnak')

gyko:int = 0
for f in filmek:
    gyko += f.koltseg
print(f'3.2: a filmek átlagos gyártási költsége ${round(gyko/len(filmek), 2)}M')

m:int = 0
for i in range(1, len(filmek)):
    if filmek[i].bk_arany > filmek[m].bk_arany:
        m = i
print(f'3.3: a legkötséghatékonyabb film címe: {filmek[m].cim}')

ke:str = input('3.4: írj be egy évszámot: ')
print(f'a {ke}-ban/ben megjelent filmek:')
for f in filmek:
    if f.bemutato.startswith(ke): print(f'  {f.cim}')