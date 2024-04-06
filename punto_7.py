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