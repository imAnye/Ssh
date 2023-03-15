'''
    Bucle o ciclo For, se utiliza cuando conocemos la cantidad de iteraciones que se desea
    ejecutar. Se utiliza con colecciones (listas, tuplas, conjuntos, diccionarios o cadenas)

    Sintaxis: for nombrevariable in coleccion
'''

'''
#Mostrar una lista de números
for i in [1,2,3,4,5,6,7,8,9,10]:
    print("Tengo hambre, sueño y quiero café")
'''

#Mostrar los elementos del ciclo For usando una lista
for i in ["Rojo", 7, 25.2, True]:
    print(i)


#Mostrar los elementos de una colección en una variable
datos = ["Rojo", 7, 25.2, True]

for i in datos:
    print(i)


#Recorrer el contenido de un diccionario mostrando sola la clave
diccionario = {"José": 59, "Luis":38, "Manuel":25}

for elementos in diccionario:
    print(f"el resultado es: {elementos}")
    
for elementos in diccionario:
    print(f"el resultado es: {diccionario [elementos]}")
