# 1. Examen VCS con Git y GitHub
## 1.1 Introducción
Este pequeño proyecto es para realizar el examen VCS con Git y GitHub.

# 2. Composición del proyecto
El proyecto se compone de un archivo main.py que instancia un objeto de la clase Número para realizar varias operaciones
con un número mediante varios métodos.

## 2.1 La clase Número
Se encuentra ubicada en el directorio clases y su estructura es la siguiente:

Propiedades:

- numero      -> Un entero

Métodos:

- es_perfecto -> Devuelve True si el número es perfecto.
- es_positivo -> Devuelve True si el número es positivo.
- es_negativo -> Devuelve True si el número es negativo.
- es_cero     -> Devuelve True si el número es 0.

# 3. Cambios a realizar en los archivos fuente durante el examen

## Ejercicio 2a


------------------------------------
~~~
def suma(self, n: int) -> None:
    self.__numero += n
~~~
------------------------------------

## Ejercicio 5a

---------------------------------------------------------------
~~~
def suma(self, n: int) -> int:
    return self.__numero + n
~~~
-----------------------------------------------------------------------

## Ejercicio 7b

------------------------------------
~~~
def resta(self, n: int) -> None:
    self.__numero -= n
~~~
------------------------------------

## Ejercicio 8c

------------------------------------
Atento al número de clase (NC) en el nombre del método

~~~
class nombreNC:
    def __init__(self, n: int):
        self.numero = n
~~~
------------------------------------

## Ejercicio 9a

------------------------------------
~~~
def __str__(self) -> str:
    return self.numero.__str__()
~~~
------------------------------------

## Ejercicio 10a

------------------------------------
~~~
def __rep__(self) -> str:
    return self.numero.__str__()
~~~
------------------------------------
