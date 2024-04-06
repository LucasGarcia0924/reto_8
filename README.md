# Reto_8
Solución de los problemas asignados - Realizado por Lucas Garcia

[![Logo-equipo.webp](https://i.postimg.cc/Z5BYw1Tx/Logo-equipo.webp)](https://postimg.cc/9D2jMgwD)
## Punto 1
***
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```
i : int = 1 # Se declaran las variables
if __name__ == "__main__": # Función Main para iniciar el código
    for i in range (1,101): # Se inicia el ciclo para toda i entre 1 y 100
        print (i, i**2) # Se imprime el valor de i con su cuadrado
```
## Punto 2
***
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```
i : int  # Se declaran las variables
if __name__ == "__main__": # Función Main para iniciar el código

    print("Números impares:") # Muestra al usuario un título
    for i in range (1,1000): # Se inicia el ciclo para toda i entre 1 y 999
        if (i % 2) == 0: # Si el módulo de i y 2 es igual a 0, osea es par, continua y no escribe dicho i
            continue
        print(str(i)) # Muestra al usuario la lista

    print("Números pares:") # Muestra al usuario un título
    for i in range (1,1001): # Se inicia el ciclo para toda i entre 1 y 1000
        if (i % 2) != 0: # Si el módulo de i y 2 es diferente a 0, osea es impar, continua y no escribe dicho i
            continue
        print(str(i)) # Muestra al usuario la lista
```
## Punto 3
***
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.
```
if __name__ == "__main__": # Función Main para iniciar el código
    
    num = int(input("Digita un número")) # Se pide ingresar el valor de la variable

    for num in range (num, 1, -1): # El ciclo se repite para todo num hasta llegar a ser igual a 2, de -1 en -1
        if (num % 2) != 0: # Si el num es impar el ciclo continua pero omite la iteración actual
            continue
        print(num) # Se muestra el num en la terminal
```
## Punto 4
***
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.
```
# Se declaran las variables
num_anter: int
factorial_1: int

def factorial_3 (number: int) -> int: # a la función factorial_3 se le ingresa un int y esta entrega un int
    # Para el caso especial de 0 se hace un if, ya que no cumple con la formula
    if number == 0 or number == 1 :
        factorial_1 = 1

    # En cualquier otro natural que no sea 0 se sigue el algoritmo
    else:
        # Se inicializan las variables para el ciclo
        num_anter = 1
        # El ciclo termina en 2 ya que multiplicar por 1 resulta en el mismo valor
        for number in range (number, 1, -1):
            # Se multiplica el numero actual por el anterior y se va "acumulando" la factorización
            factorial_1 = number * num_anter 
            # Se iguala el num anterior a la factorización para que en la próxima iteración se siga acumulando
            num_anter = factorial_1
            
    return factorial_1

if __name__ == "__main__": # Función Main para iniciar el código
    
    number = int(input("Ingrese un número")) # Se pide ingresar un valor para la variable
    for number in range (0, number+1): # Se inicia el ciclo para number desde 0 hasta él mismo
        factorial_2 = factorial_3(number) # Se llama a la función factorial_3 para que entregue el factorial del numero
        print(f"El número {number} tiene como su factorial a {factorial_2}") # Se muestran los resultados
```
## Punto 5
***
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```
# Se declaran las variables
previo: int = 1
potencia: int
if __name__ == "__main__": # Función Main para iniciar el código
    n = int(input("El exponente de la potencia es: ")) # Se ingresa el exponente
    
    for potencia in range (1, n+1): # Se inicia el ciclo desde 1 hasta n
        potencia = previo*2 # se multiplica 2 por el producto previo
        previo = potencia # Se actualiza la variable para que en la proxima iteración tome el valor del producto
    if n == 0: # Si el exponente es 0 la potencia es 1
        potencia = 1
    print(potencia) # Se muestra el valor de la potencia
```
## Punto 6
***
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```
# Se declaran las variables
previo: int = 1
potencia: int

if __name__ == "__main__": # Función Main para iniciar el código
    x = float(input("La base de la potencia es: ")) # Se ingresa la base
    n = int(input("El exponente de la potencia es: ")) # Se ingresa el exponente
    
    for potencia in range (1, n+1): # Se inicia el ciclo desde 1 hasta n
        potencia = previo*x # se multiplica la base por el producto previo
        previo = potencia # Se actualiza la variable para que en la proxima iteración tome el valor del producto
    if n == 0: # Si el exponente es 0 la potencia es 1
        potencia = 1
    print(potencia) # Se muestra el valor de la potencia
```
## Punto 7
***
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```
# Se declaran las variables
i : int
multiplicador: int

if __name__ == "__main__": # Función Main para iniciar el código
    i = 1 # Se inicializa la variable para el ciclo

    for i in range (1,10): # El ciclo se da para i, desde 1 hasta 9

        print(f"Tabla del {i}") # Muestra al usuario un título
        multiplicador = 1 # Se inicializa la variable para el ciclo
        for multiplicador in range (1,11): # El ciclo se da para multiplicador, desde 1 hasta 10
            tabla  = i * multiplicador # Se calculan los productos
            print(f"{i} x {multiplicador} = {tabla}") # Se muestra una línea de una tabla

        i += 1 # Se actualiza la variable para que en la proxima iteración tome el valor mayor por 1
        print("") # Se imprime salto de línea para mayor organización
```
## Punto 8
***
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
```
import math
from punto_4 import factorial_3

formula = float
verdadero: float
diferencia: float
termino: float
n: int

if __name__ == "__main__": # Función Main para iniciar el código
    x = float(input("El exponente de la potencia es: "))
    n = 0
    diferencia = float('inf')  # Inicializa la diferencia con un valor infinito para entrar en el bucle
    
    while (diferencia > 0.1): # # Ciclo durante diferencia mayor a 0.1
        n += 1
        formula = 0
        for i in range(n+1): # Para todas las i desde 0 hasta n
            formula += (x**i) / factorial_3(i)
        
        verdadero = math.exp(x)
        diferencia = abs(verdadero - formula)  # Valor absoluto de la diferencia entre los valores real y aproximado
    # Se muestran resultados
    print(f"Valor real: {verdadero}")
    print(f"Valor aproximado: {formula}")
    print(f"Su diferencia: {diferencia}")
    print(f"Valor de n necesario para que el error sea menor o igual a 0.1: {n}")
```
## Punto 9
***
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```
import math
from punto_4 import factorial_3

formula = float
verdadero: float
diferencia: float
termino: float
n: int

if __name__ == "__main__": # Función Main para iniciar el código
    x = float(input("El valor de seno es: "))
    n = 0
    diferencia = float('inf')  # Inicializa la diferencia con un valor infinito para entrar en el bucle
    
    while diferencia > 0.1:
        n += 1
        formula = 0
        for i in range(n+1):  # Itera sobre los primeros n términos de la serie de Maclaurin
            if i % 2 == 0:  # Solo considera términos impares
                continue
            termino = ((-1) ** (i // 2)) * (x ** i) / factorial_3(i)
            formula += termino
        
        verdadero = math.sin(x)
        diferencia = abs(verdadero - formula)  # Valor absoluto de la diferencia entre los valores real y aproximado
    
    # Se muestran resultados
    print(f"Valor real: {verdadero}")
    print(f"Valor aproximado: {formula}")
    print(f"Su diferencia: {diferencia}")
    print(f"Valor de n necesario para que el error sea menor o igual a 0.1: {n}")
```
## Punto 10
***
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```
import math

formula = float
verdadero: float
diferencia: float
termino: float
n: int
if __name__ == "__main__": # Función Main para iniciar el código

    x = float(input("Digite una x dentro de [-1,1] para hallar el valor de la arcotangente: "))
    n = 0
    diferencia = float('inf')  # Inicializa la diferencia con un valor infinito para entrar en el bucle
    if -1 < x and x < 1: 
        while diferencia > 0.1:
            n += 1
            formula = 0
            for i in range(n+1):  # Itera sobre los primeros n términos de la serie de Maclaurin
                if i % 2 == 0:  # Solo considera términos impares
                    continue
                termino = ((-1) ** (i // 2)) * (x ** i) / i
                formula += termino
            
            verdadero = math.atan(x)
            diferencia = abs(verdadero - formula)  # Valor absoluto de la diferencia entre los valores
        
        # Se muestran resultados
        print(f"Valor real: {verdadero}")
        print(f"Valor aproximado: {formula}")
        print(f"Su diferencia: {diferencia}")
        print(f"Valor de n necesario para que el error sea menor o igual a 0.1: {n}")
    else:
        print("Valor ingresado incorrecto, intente otra vez")
```
