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