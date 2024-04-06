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