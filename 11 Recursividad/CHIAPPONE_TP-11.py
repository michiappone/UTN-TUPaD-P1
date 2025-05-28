#Ejercicio 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    print(factorial(i))


#Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)
    

posicion = int(input("Ingrese la posicion que desea imprimir: "))

for i in range (0, posicion + 1):
    print(f"En la posicion {i} de fibonacci obtenemos: {fibonacci(i)}")


#Ejercicio 3
def potencia_recursiva(num,exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * potencia_recursiva(num, exp -1)


#Algoritmo general
print("Ingrese un numero y un exponente: ")
numero = int(input(""))
exp = int(input(""))


print(potencia_recursiva(numero,exp))


#Ejercicio 4
def dec_a_bin_recursivo(num):
    if num == 0:
        return ""
    else:
        return dec_a_bin_recursivo(num // 2) + str(num % 2)
    

dec = int(input("Ingrese un decimal: "))
print(dec_a_bin_recursivo(dec))


#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    

#Ejercicio 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n // 10) + (n % 10)
    

#Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
    

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_dig = numero % 10
        if ultimo_dig == digito:
            contador = 1
        else:
            contador = 0
        return contador + contar_digito(numero // 10,digito)

