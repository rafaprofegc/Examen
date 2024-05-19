"""
Clase:          Numero
Descripción:    Representa a un  número entero
"""
class Numero:
    def __init__(self, numero: int):
        self.__numero = numero


    # Métodos getters and setters
    @property
    def numero(self) -> int:
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        self.__numero = numero

    # Método es_perfecto
    def es_perfecto(self):
        suma_divisores = 1
        divisor = 2
        while divisor < self.numero / 2:
            if self.numero % divisor == 0:
                suma_divisores += divisor
            divisor = divisor + 1

        # Fin del bucle while
        return suma_divisores == self.__numero

# Fin del método es_perfecto


    def es_negativo(self) -> bool:
        # Añado comentario y lo modifico
        return True if self.__numero < 0 else False

    def es_positivo(self) -> bool:
        return True if self.__numero > 0 else False

    def es_cero(self) -> bool:
        return True if self.__numero == 0 else False

    def __str__(self) -> str:
        return self.__numero.__str__()

# Fin de la clase Numero
