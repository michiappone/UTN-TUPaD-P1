#Ejercicio 1
multiplos_de_4 = list(range(4,101,4))
print(multiplos_de_4)


#Ejercicio 2
lista_frutas = ["Manzana", "Banana", "Pera", "Durazno", "Naranja"]

print(lista_frutas[2])


#Ejercicio 3
lista_verduras = []

lista_verduras.append("Lechuga")
lista_verduras.append("Cebolla")
lista_verduras.append("Calabaza")

print(lista_verduras)


#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"] 

animales[1] = "Loro"
animales[3]= "Oso"

print(animales)


#Ejercicio 5
"""
En la primer linea el programa crea una lista de 5 elementos, a la cual le elimina elimina el elemento ubicado en la ultuma posicion(en este caso la posicion 4) para luego imprimir por pantalla la lista modificada

"""


#Ejercicio 6
numeros = list(range(10,31,5))

print(numeros[0])
print(numeros[1])


#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "posicion 1"
autos[2] = "posicion 2"

print(autos)


#Ejercicio 8
dobles = []

dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)

print(dobles)


#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

compras[2].append("jugo")
compras[1][1] =  "tallarines"
compras[0].remove("pan")

print(compras)


#Ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)