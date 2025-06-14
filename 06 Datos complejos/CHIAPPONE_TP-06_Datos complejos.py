#EJERCICIO 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300


#EJERCICIO 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800


#EJERCICIO 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700
precios_frutas["Melón"]=2800

lista_frutas = precios_frutas.keys()


#EJERCICIO 4
agenda = {}

print("Cargá 5 contactos")

for i in range (5):
    nombre = input("Ingrese el nombre: ")
    numero = int(input("Ingrese el numero: "))
    agenda[nombre] = numero

consulta = input("Ingrese el nombre del numero que desea ver: ")

if consulta in agenda:
    print(f"El numero de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontro el contacto ´{consulta}´")


#EJERCICIO 5
# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras (separadas por espacios)
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)

# Contar cuántas veces aparece cada palabra
conteo_palabras = {}
for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

# Mostrar los resultados
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nCantidad de veces que aparece cada palabra:")
for palabra, cantidad in conteo_palabras.items():
    print(f"{palabra}: {cantidad}")


#EJERCICIO 6
# Crear un diccionario para guardar alumnos y sus notas
alumnos = {}

# Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i+1}: ")
    
    # Ingresar las 3 notas, separadas por espacios
    notas_input = input(f"Ingresá 3 notas para {nombre}, separadas por espacios: ")
    
    # Convertir a tupla de enteros o flota

#EJERCICIO 7
# Sets de estudiantes que aprobaron cada parcial
parcial1 = {'Ana', 'Bruno', 'Carlos', 'Diana'}
parcial2 = {'Carlos', 'Diana', 'Elena', 'Fernando'}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

#EJERCICIO 8
# Diccionario con productos y stock inicial
stock_productos = {
    'Pan': 20,
    'Leche': 15,
    'Huevos': 30
}

# Mostrar el stock actual
print("Stock actual de productos:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

# Solicitar al usuario un producto
producto = input("\nIngresá el nombre de un producto: ")

if producto in stock_productos:
    print(f"El stock actual de '{producto}' es: {stock_productos[producto]} unidades.")

    # Preguntar si desea agregar unidades
    agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
    if agregar == 's':
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de '{producto}': {stock_productos[producto]} unidades.")
else:
    print(f"El producto '{producto}' no existe.")
    agregar_nuevo = input("¿Querés agregarlo al inventario? (s/n): ").lower()
    if agregar_nuevo == 's':
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] = unidades
        print(f"Producto '{producto}' agregado con {unidades} unidades.")

# Mostrar el stock final
print("\nStock actualizado:")
for producto, stock in stock_productos.items():
    print(f"{producto}: {stock} unidades")

#EJERCICIO 9
# Crear una agenda vacía
agenda = {}

# Cargar algunos eventos
agenda[('Lunes', '10:00')] = 'Reunión con equipo'
agenda[('Martes', '14:30')] = 'Clase de inglés'
agenda[('Miércoles', '09:00')] = 'Consulta médica'

# Mostrar la agenda completa
print("Agenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

# Permitir agregar un nuevo evento
nuevo_dia = input("\nIngresá el día del nuevo evento: ")
nueva_hora = input("Ingresá la hora del nuevo evento (formato HH:MM): ")
nuevo_evento = input("Describí el evento: ")

# Usar la tupla como clave
agenda[(nuevo_dia, nueva_hora)] = nuevo_evento

# Mostrar agenda actualizada
print("\nAgenda actualizada:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

#EJERCICIO 10
# Invertir el diccionario
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

# Mostrar el nuevo diccionario
print("Diccionario invertido (capital: país):")
print(capitales_paises)
