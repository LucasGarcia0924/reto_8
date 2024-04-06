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