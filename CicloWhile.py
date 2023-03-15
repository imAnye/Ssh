'''
    Ciclo o Bucle while, se utiliza cuando no conocemos la cantidad de iteraciones que se
    desea ejecutar. Se utiliza con colecciones (listas, tuplas, conjuntos, diccionario o cadenas).

    Sintaxis: While condicion
'''

#Imprimir una lista de números
numero = 1

while numero <= 50:
    print(numero)
    numero = numero + 1

import math

numero = int(input("Introduzca un número: "))

while numero < 0:
    print("El número no puede ser negativo. Intentelo denuevo!!!")
    numero = int(input("Introduzca un número: "))

print(f"La raíz cuadrada de {numero} es: {(math.sqrt(numero)):.3f")
