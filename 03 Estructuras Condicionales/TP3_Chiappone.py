#Ejercicio 1
edad = int(input("Ingrese su edad: "))

edad_minima = 18

if edad > edad_minima:
    print("Es mayor de edad")
else:
    pass


#Ejercicio 2
nota = int(input("Ingrese la nota: "))

nota_min = 6

if nota >= nota_min:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
num = int(input("Ingrese un numero par: "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un numero par")


#Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad >= 18 and edad < 30:
    print("Joven adulto/a")
elif edad >= 30:
    print("Adulto/a")


#Ejercicio 5
a = input("Ingrese una contraseña: ")

longit = len(a)

if longit >= 8 and longit <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
import random 
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")


#Ejercicio 7
frase = input("Ingrese una palabra o frase: ")

ult_letra = frase[-1]
vocal = {"a","e","i","o","u"}

if ult_letra in vocal:
    print(frase + "!")
else:
    print(frase)


#Ejercicio 8
nombre = input("Ingrese su nombre: ")

print("Ingrese un numero del 1 al 3 de acurdo a su eleccion: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
num = int(input())

if num == 1:
    nombre = nombre.upper()
    print(nombre)
elif num == 2:
    nombre = nombre.lower()
    print(nombre)
elif num == 3:
    nombre = nombre.title()
    print(nombre)


#Ejercicio 9 
magnit = float(input("Ingrese la magnitud del terremoto: "))

if magnit < 3:
    print("Muy leve")
elif magnit >= 3 and magnit < 4:
    print("Leve")
elif magnit >= 4 and magnit < 5:
    print("Moderado")
elif magnit >= 5 and magnit < 6:
    print("Fuerte")
elif magnit >= 6 and magnit < 7:
    print("Muy Fuerte")
elif magnit >= 7:
    print("Extremo")

#Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))

if hemisferio == "n" or hemisferio == "N":
#Invierno
    if mes == 12 and dia >= 21:
        print("Invierno")       
    elif (mes == 3 and dia <= 20) or (mes < 3 and dia <= 31) :
            print("Invierno")
#Primavera
    elif mes == 3 and dia >= 21:
        print("Primavera")       
    elif (mes == 6 and dia <= 20) or (mes > 3 and mes < 6 and dia <= 31) :
            print("Primavera")
#Verano
    elif mes == 6 and dia >= 21:
        print("Verano")  
    elif (mes == 9 and dia <= 20) or (mes > 6 and mes < 9 and dia <= 31) :
            print("Verano")
#Otoño
    elif mes == 9 and dia >= 21:
        print("Otoño")  
    elif (mes == 12 and dia <= 20) or (mes > 9 and mes < 12 and dia <= 31) :
            print("Otoño")   

elif hemisferio == "s" or hemisferio == "S":
#Verano
    if mes == 12 and dia >= 21:
        print("Verano")       
    elif (mes == 3 and dia <= 20) or (mes < 3 and dia <= 31) :
            print("Verano")
#Otoño
    elif mes == 3 and dia >= 21:
        print("Otoño")       
    elif (mes == 6 and dia <= 20) or (mes > 3 and mes < 6 and dia <= 31) :
            print("Otoño")
#Invierno
    elif mes == 6 and dia >= 21:
        print("Invierno")  
    elif (mes == 9 and dia <= 20) or (mes > 6 and mes < 9 and dia <= 31) :
            print("Invierno")
#Primavera
    elif mes == 9 and dia >= 21:
        print("Primavera")  
    elif (mes == 12 and dia <= 20) or (mes > 9 and mes < 12 and dia <= 31) :
            print("Primavera") 
else: 
    print("El valor ingresado es incorrecto")