from clases.Numero import Numero

def main():

    while True:
        print("Ejecución de la clase Número")
        print("----------------------------")

        numero = int(input("Introduce un número (0 para terminar): "))

        n = Numero(numero)

        if n.es_perfecto():
            print(f"El número {n} ES perfecto")
        else:
            print(f"El número {n} NO ES perfecto")

        if n.es_positivo():
            print(f"El número {n} ES +")

        if n.es_negativo():
            print(f"El número {n} ES -")

        if n.es_cero():
            print(f"El número {n} ES cero")

        if numero == 0:
            break
    # Fin del bucle while
            
if __name__ == '__main__':
    main()
