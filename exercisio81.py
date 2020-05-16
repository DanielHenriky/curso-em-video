# Crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista dde valores, ordenada de forma decrecente.
# C) Se o valos 5 foi digitado e está ou não na lista.
lista = list()
cont = 0
while True:
    numero = int(input('Digite um valor:'))
    lista.append(numero)
    parar = str(input('Quer continuar [S/N] :')).strip().lower()
    v = 5 in lista
    if 'n' in parar:
        break
lista.sort(reverse = True)
print('Fim')
print(f'Foram digitados {len(lista)} valores.')
print(f'Os valores em ordem decrescente foram {lista}')
lista.sort()
print(f'Os valores em orde crescente foram {lista}')
if v == True:
    print('O valor 5 foi encotrado na lista')
else:
    print('O valor 5 não foi encontrado na lista ')
