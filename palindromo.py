palavra = input("Insira uma palavra :")

def acha_palindromo(str):

    str_invertida = "".join(reversed(str))

    if str_invertida == str:
        print("É um palíndromo")

    else:
        print("Não é um palíndromo")

acha_palindromo(palavra)