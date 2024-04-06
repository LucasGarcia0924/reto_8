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