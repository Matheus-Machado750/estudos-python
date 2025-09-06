lista_numerica = [2, 7, 8, 9, 2, 4, 0, 19]

def quantia_pares(lista):

    i = 0

    for par in lista:

        if par %2 == 0:
            i += 1

    print(i)

quantia_pares(lista_numerica)