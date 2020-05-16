# Faça um programa que leia 5 valores númericos e guarde-os em 
# uma lista. No final, mostre quau foi o maior e o menor valor
# digitados e as suas respectivas posições na lista
lista = []
for n in range(1, 6):
    print(f'{n}ª', end=' ')
    va = int(input(f'valor na posição {n - 1}:'))
    lista.append(va)
maior = max(lista)
menor = min(lista)
print(f'\nVoce digitou o valores {lista}')
print('-=-'*10)
print(f'Maior valor {maior} nas posições',end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'Menor valor {menor} nas posições',end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')


