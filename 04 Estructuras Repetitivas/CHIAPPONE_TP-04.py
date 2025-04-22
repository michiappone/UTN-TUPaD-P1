#Ejercicio 1
for num  in range(101):
    print(num)

#Ejercicio 2
num = int(input("Ingrese un numero entero: "))

cant_dig = 0

if num == 0:
    cant_dig = 1
else:
    while num != 0:
        num = num // 10
        cant_dig += 1

print (f"El numero ingresado tiene {cant_dig} digitos")

#Ejercicio 3
print("Ingrese dos numeros, primero el menor de ellos ")
num1 = int(input())
num2 = int(input())

suma = 0

while num1 < (num2 -1):
    num1 += 1
    suma = suma + num1

print(f"La suma de los numeros comprendidos entre los dos ingresados es : {suma}")

#Ejercicio 4
num = int(input("Ingrese un numero "))
total_acum = num

while num != 0:
    num = int(input("Ingrese un numero o ingrese 0 para finalizar: "))
    total_acum = total_acum + num

print(f"El total acumulado es : {total_acum}")


#Ejercicio 5
import random

num_aleatorio = random.randint(0,9)
num = int(input("Ingrese un numero entre 0 y 9: "))
cont = 1

if 0 <= num <=9:
    while num != num_aleatorio:
        num = int(input("Siga intentando "))
        cont  += 1
    print(f"Te tomo {cont} intentos acertar el numero")
else:
    print("El numero ingresado no esta dentro del rango")

#Ejercicio 6
for i in range (100 -2,0,-2):
    print(i)


#Ejercicio 7
num = int(input("Ingrese un numero: "))
total_acumulado = 0

for i in range(num):
    total_acumulado = total_acumulado + i
    print(total_acumulado)

print(f"La suma de los numeros comprendidos entre 0 y {num} es: {total_acumulado}")


#Ejercicio 8
print("Ingrese 100 numeros: ")
impar = 0
par = 0
pos = 0
neg = 0

for i in range (1,101):  
    num = int(input(""))

    if num % 2 == 0:
        par += 1
    else:
        impar += 1

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print("Hay:")
print(f"{par} numeros pares")
print(f"{impar} numeros impares")
print(f"{pos} numeros positivos")
print(f"{neg} numeros negativos")


#Ejercicio 9
print("Ingrese 100 numeros: ")
suma = 0
media = 0
cont = 0

for i in range (1,101):  
    num = int(input(""))

    suma = suma + num
    cont +=1

media = suma / cont

print(f"La media es: {media}")


#Ejercicio 10
num = int(input("Ingrese un numero: "))

dig = 0
inverso = 0

while num != 0:
    dig = num % 10
    num = num // 10
    inverso = inverso * 10 + dig

print(f"El numero inverso es: {inverso}")
