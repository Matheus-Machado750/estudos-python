def contador_de_vogais():

    i = 0

    vogais = ("a", "e", "i", "o", "u")

    palavra = input("Insira uma palavra :").lower()

    for letra in palavra:

        if letra in vogais:
            i += 1

    return i

print(contador_de_vogais())
            