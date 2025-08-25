# numero = int(input("ingresa un numero: "))
# while numero > 1:
#     print(f"{numero}")
#     numero -= 1
#     print(f"finaliza el sistema")

# num = int(input("ingresa un munero: "))

# i = 1

# print(f"\n inicia el contador en 1 {num}: ")

# while i <= 10:
#     print(f"{num} * {i} = {num * i}")
#     i += 1

# x = 5
# while True:
#   x -= 1
#   print(x)
#   if x ==0:
#     break
#   print("Fin del bucle")

# chance = 1
# while chance <= 3:
#     txt =input("escribe SI: ")
#     if txt =="SI":
#         print("OK, lo conseguiste en el intento", chance)
#         break
#     chance +=1
# else:
#     print("has agotado tus tres intentos")

# ----------- Ejercicio 1 Suma hasta cero -------------#
# total = 0

# numero = int(input("ingresa primer numero entero: "))

# while numero != 0:
#     total += numero
#     numero = int (input("ingresa segundo numero entero: "))

# print("la suma total es:", total)

# ----------- Ejercicio 2 Contraseña secreta -------------#

# clave = ""
# while clave != "horacio123":
#     clave = input("ingresa la contraseña: ")
# print("contraseña correcta")

# ----------- Ejercicio 3 Lista de compras -------------#
# lista = []

# productos = input("ingresa un producto (escribe 'fin' para teminar): ")
# while productos != "fin":
#     lista.append(productos)
#     productos = input("ingresa un producto (escribe 'fin' para teminar): ")
# print(f"la lista de productos es: {lista}")

# ----------- Ejercicio 4 Contador de pares e impares -------------#
# contador = 1
# pares = 0
# impares = 0

# while contador <= 10:
#     numero =int(input(f"ingresa el numero {contador}: "))
#     if numero % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     contador += 1
# print(f"la cantidad de numero pares es: {pares}")
# print(f"la cantidad de numero impares es: {impares}")

# ----------- Ejercicio 5 Promrdio de calificaciones ------------#
# lista_notas = []

# nota1 = float(input("ingresa la nota 1: "))
# nota2 = float(input("ingresa la nota 2: "))
# nota3 = float(input("ingresa la nota 3: "))

# lista_notas.append(nota1)
# lista_notas.append(nota2)
# lista_notas.append(nota3)

# promedio = (nota1 + nota2 + nota3) / 3

# while lista_notas != "salir":
#     print(f"tu promedio es: {promedio} ")
#     salir = "salir"
#     pedir_salir= input("Ingresa la palabra salir para salir")
    
#     if pedir_salir == "salir":
        
#         print("se rompe el bucle")
#     break
# ----------- Ejercicio 6 Tabla de multiplicar ------------#

# numero = int(input("ingresa un numero: "))

# perdir_numero = 1

# while perdir_numero <= 10:
#     print(f"{numero} x {perdir_numero} = {numero * perdir_numero}")
#     perdir_numero += 1

# ----------- Ejercicio 7 Adivina el numero ------------#

# secreto = 17

# while secreto == 17:

#     intento = int (input("adivina el numero: "))
#     if intento > secreto:
#         print("el numero es mayor ")
#     elif intento < secreto:
#         print("el numero es menor")
#     else:
#        print("¡ADIVINASTE!")
#        break

# ----------- Ejercicio 8 Tupla de frutas ------------#

# tupla_frutas = ("manzana", "pera", "mango")

# while True:
#     fruta = input("ingresa el una fruta: ")
#     if fruta in tupla_frutas:
#         print(f"ACERTASTE la fruta que escribiste es: {fruta}")
#         break
#     else:
#         print("no acertaste la fruta :(")

# ----------- Ejercicio 9 Diccionario de traducion ------------#

# diccionario = {
#     "hola": "hello",
#     "gracias": "thanks",
#     "rojo": "red",
#     "azul": "blue",
#     "gato": "cat"
# }

# while True:
#     palabra = input("ingresa una palabra: ")
#     if palabra in diccionario:
#         print(f"la traduccion de la palabra es: {diccionario[palabra]}")
#         break
#     else:
#         print("palabra no encontrada")

# ----------- Ejercicio 10 Calculadora basica ------------#

# opcion = 0

# while opcion != 5:
#     print("\n1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n5. Salir")
#     opcion = int(input("elija una opcion: "))

#     if opcion == 5:
#         print("saliste")
#         break

#     if opcion in [1,2,3,4]:
#         numero1 = float(input("ingresa primer numero: "))
#         numero2 = float(input("ingresa segundo numero: "))

#         if opcion == 1:
#             print(f"resultado: {numero1 + numero2}")
#             break
#         elif opcion == 2:
#             print(f"resultado {numero1 - numero2}")
#             break
#         elif opcion == 3:
#             print(f"resultado {numero1 * numero2}")
#             break
#         elif opcion == 4:
#             if numero2 != 0:
#                 print(f"resultado {numero1 / numero2}")
#                 break
#             else:
#                 print("no se pued dividir el entre cero")

# ----------- Ejercicio 11 Registro de edades ------------#
# edades = {}
# nombre = input("ingresa un nombre (o 'salir'): ")
# while nombre != "salir":
#     edad = int(input(f"ingresa la edad de {nombre}: "))
#     edades[nombre] = edad
#     nombre = input("ingrese otro nombre (o 'salir'): ")
# print(f"registro de edades: {edades}")

# ----------- Ejercicio 12 Busca una lista ------------#

# colores = ["rojo", "azul", "verde", "amarillo", "negro"]
# color = input("Escriba un color: ")

# while color not in colores:
#     color = input("no está en la lista, intente de nuevo: ")

# print("¡LO ENCONTRASTE!")

# ----------- Ejercicio 13 Potencia de un numero ------------#

# numero = int(input("Ingrese un número: "))
# potencia = 1

# while potencia <= 5:
#     print(f"{numero} ^ {potencia} = {numero ** potencia} ")
#     potencia+= 1

# ----------- Ejercicio 14 Lista de cuadrados ------------#

# cuadrados = []
# a = 1

# while a <= 5:
#     num = int(input(f"Ingrese número {a}: "))
#     cuadrados.append(num ** 2)
#     a += 1

# print(f"Lista de cuadrados: {cuadrados}")

# estudiantes = {}
# nombre = input("Ingrese nombre del estudiante (o 'fin'): ")

# ----------- Ejercicio 15 Diccionario de estudio ------------#

estudiantes = {}
nombre = input("Ingrese nombre del estudiante (o 'fin'): ")

while nombre.lower() != "fin":
    nota = float(input(f"Ingrese nota final de {nombre}: "))
    estudiantes[nombre] = nota
    nombre = input("Ingrese nombre del estudiante (o 'fin'): ")

print(f"Diccionario de estudiantes: {estudiantes}")













