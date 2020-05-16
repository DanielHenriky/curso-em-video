# Crie um programa onde o usuário posa digitar vários valores
# numéricos e cadastre-os em uma lista. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
    valor = input('Digite um valor:')
    # ------------------------------------------------------------
    #                       EXEMPLO 1
    # va = valor in lista
    # if va == True:
    # if
    #     print('Ese valor ja existe!!!!!!')
    #     print('-=-'*10)
    # else:
    #     lista.append(valor)
    #     print('Valor add com sucesso...')
    #     print('-=-'*10)
    #-------------------------------------------------------------
    #                       EXEMPLO 2
    if valor not in lista:
        lista.append(valor)
        print('\033[1;32mValor add com sucesso...\033[m')
        print('-=-'*10)
    else:
        print('\033[1;31mEse valor ja existe!!!!!!\033[m')
        print('-=-'*10)
    conti = str(input('Deseja continuar [S/N]')).strip().lower()
    if conti in 'n':
        break
print('-=-'*10)
lista.sort()
print('Lista',lista)
print(len(lista), 'Valores')
