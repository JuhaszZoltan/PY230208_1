file = open(file='tablazat.csv', mode='a', encoding='UTF-8')

szamlalo:int = 1
file.write('név;átlag\n')
while True:
    nev:str = input(f'írd be a {szamlalo}. diák nevét: ')
    if nev == '': break
    atlag:float = float(input(f'írd be {nev} a 9. év végi átlagát: '))
    file.write(f'{nev};{atlag}\n')
    szamlalo += 1
print('kész!') 