#Ejercicio 1
#Definicion de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()


#Ejercicio 2
#Definicion de funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!") 

#Programa principal
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Ejercicio 3
#Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#Ejercicio 4
#Definicion de funciones
def calcular_perimetro_circulo(radio) :
    perimetro = 2 * 3.1415 * radio

    print(f"El perimetro del circulo es: {perimetro}")

def calcular_area_circulo(radio):
    area = 3.1415 * radio ** 2

    print(f"El area del circulo es: {area}")

#Programa principal
radio = float(input("Ingrese el radio: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


#Ejercicio 5
#Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} Segundos equivalen a: {horas} horas")

#Programa principal
segundos = int(input("Ingrese los segundos que desea convertir a horas: "))
segundos_a_horas(segundos)  


#Ejercicio 6
#Definicion de funciones
def tabla_multiplicar(numero):
    resultado = 0

    print(f"La tabla de multiplicar de {numero} es: ")
    for i in range (1, 10 +1):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

#Programa principal
num = int(input("Ingrese un numero: "))
tabla_multiplicar(num)


#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b

    print(f"El resultado de aplicarle las operaciones basicas a los numeros {a} y {b} es: ")
    print(f"Suma = {suma}")
    print(f"Resta = {resta}")
    print(f"Multiplicacion = {producto}")
    print(f"Division = {division}")
    
#Programa principal
print("Ingrese dos numeros ")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))

operaciones_basicas(num1, num2)


#Ejercicio 8
#Definicion de funciones
def calcular_imc(peso, altura):
    IMC = peso / altura

    print(f"Tu IMC es de: {IMC}")


#Programa principal
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

calcular_imc(peso, altura)


#Ejercicio 9
#Definicion de funciones
def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

#Programa principal
celsius = float(input("Ingrese la temperatura en celsius: "))

print(f"{celsius} °C = {celsius_a_fahrenheit(celsius)} °F")


#Ejercicio 10
#Definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
print("Ingrese 3 numeros: ")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
num3 = int(input("Tercer numero: "))

print(f"El promedio entre {num1}, {num2} y {num3} es: {calcular_promedio(num1, num2, num3)}")