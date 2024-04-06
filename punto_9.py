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