precos = ('Camisa', 199.00, 'Shorts', 89.90, 'Meião', 29.90, 'Chuteira', 299.90, 'Caneleira', 32.90, 'Térmica', 79.90)
print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<30}', end='')
    else:
        print(f'R${precos[pos]:>7.2f}')
print('='*40)
