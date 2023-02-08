from math import pi

file = open(file='elso.txt', mode='w', encoding='UTF-8')

file.write('this is my first txt file!\n')
file.write(f'PI = {pi}\n')

print('done')