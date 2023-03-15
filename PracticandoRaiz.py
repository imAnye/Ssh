'''
for i in [1,2,3,4]:
    print("Salu2")

for i in [1,2,3,4]:
    print(i)

datos= ["yea", "xdxd"]
for a in datos:
    print(a)

diccionario= {"Pepe":40, "Luis":8}
for elementos in diccionario:
    print(f"El resultado es {elementos}")

for elementos in diccionario:
    print(f"El resultado es: {diccionario[elementos]}")

numero = 1
while numero < 50:
    print(numero)
    numero= numero + 1

'''
'''
nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
academico = input("Digite su nivel académico: ")
edad = int(input("Digite su edad: "))

if academico == "Bachiller" or academico == "bachiller" and edad >=16:
    print("Usted puede entrar")
else:
    print("xd")
'''
import math
numero = int(input("Digite su numero: "))

while numero <0:
    print("El numero no puede ser negativo, intentelo denuevo")
    numero = int(input("Digite su numero: "))
print(f"El resultado de {numero} es: {(math.sqrt(numero)):.3f}")
