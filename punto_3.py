if __name__ == "__main__": # Función Main para iniciar el código
    
    num = int(input("Digita un número")) # Se pide ingresar el valor de la variable

    for num in range (num, 1, -1): # El ciclo se repite para todo num hasta llegar a ser igual a 2, de -1 en -1
        if (num % 2) != 0: # Si el num es impar el ciclo continua pero omite la iteración actual
            continue
        print(num) # Se muestra el num en la terminal