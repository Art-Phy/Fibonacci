### Serie de Fibonacci ###

# Se le pide al usuario cuántos números desea imprimir
n = int(input("¿Cuántos números de la secuencia deseas? "))

def fibonacci(n):
    a = 0
    b = 1
    cuenta = 0

# Se crea un bucle hasta el número que haya escrito el usuario
    while cuenta < n:
        print(a, end=" ") # Se imprime el número actual

        a, b = b, a + b
        cuenta += 1 # Se indica que cada sucesión es +1

    # Este print se añade para evitar que al final de la impresión salga un %
    print()

# Se llama a la función
fibonacci(n)
