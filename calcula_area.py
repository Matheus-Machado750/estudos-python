def main(get_medidas):

    comprimento = get_medidas[0]

    altura = get_medidas[1]

    area = comprimento * altura

    print(area)

def get_medidas():
    lista = []
    try:
        comprimento = float(input("Insira o comprimento do quadrado ou retângulo: "))
        altura = float(input("Insira a altura do quadrado ou retângulo: "))
        
        lista.append(comprimento)
        lista.append(altura)

    except ValueError:
        
        print("Precisa ser um número.")
        return [0, 0]

    return lista

if __name__ == "__main__":
    main(get_medidas())