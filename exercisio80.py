# Crie um programa onde o usuário possa digitar cinco valores
# núméricos e cadastre-os em uma lista, Já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista
# ordenada na tela
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('add ao final da lista...')
    else:
        posi = 0
        while posi < len(lista):
            if n <= lista[posi]:
                lista.insert(posi, n)
                print(f'add na posição {posi} da lista...')
                break
            posi += 1
print('-=-'*20)
print(lista)

