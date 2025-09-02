frase_espaco = input("Insira uma frase qualquer : ")

def remove_espacos(frase):

    frase_junta = frase.replace(" ", "-")

    return frase_junta

print (remove_espacos(frase_espaco))