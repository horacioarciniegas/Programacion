#----- 1 -----#

# edad =int(input("ingresa tu edad: "))
# if edad < 18:
#     print("eres menor de edad")
# elif edad < 65:
#     print("eres mayor de edad")
# else:
#     print("eres adulto mayor")

#----- 2 -----#

# estatura = float(input("¿cual es tu estatura?: "))
# if estatura < 1.5:
#     print("eres conciderado bajo")
# elif estatura <= 1.8:
#     print("eres de estatura media")
# else:
#     print("eres alto")

#----- 3 -----#

# numero = int(input("ingresa un numero: "))
# if numero % 2 == 0:
#     print("es multiplo de 2")
# elif numero % 3 == 0:
#     print("es multiplo de 3")
# else:
#     print("no es multiplo de ninguno de los dos")

#----- 4 -----#

# num = float (input("ingresa un numero decimal: "))
# num_str = str(num)
# partes = num_str.split(".")
# if len(partes) == 2:
#     decimales = len(partes[1])
#     if decimales == 1:
#         print("tienes 1 decimal")
#     elif decimales == 2:
#         print("tienes 2 decimales")
#     else:
#         print("tienes mas de 2 decimales")
# else:
#     print("no tienes decimales")

#----- 5 -----#

# pais = input("ingresa un pais: ")
# paises = ("Colombia", "Peru", "Argentina", "Mexico")
# if pais in paises:
#     print("estas en la lista")
# else:
#     print("no estas en la lista")
    
#----- 6 -----#

# tipo = input("Ingresa tu tipo de sangre (A, B, AB, O): ").upper()

# compatibilidad = {
#     "A": "puede donar a A y AB",
#     "B": "puede donar a B y AB",
#     "AB": "puede donar solo a AB",
#     "O": "puede donar a todos"
# }

# tipos_validos = ["A", "B", "AB", "O"]

# if tipo == "A":
#     print("Compatibilidad:", compatibilidad["A"])
# elif tipo == "B":
#     print("Compatibilidad:", compatibilidad["B"])
# elif tipo == "AB":
#     print("Compatibilidad:", compatibilidad["AB"])
# elif tipo == "O":
#     print("Compatibilidad:", compatibilidad["O"])
# else:
#     print("Tipo de sangre no válido")

#----- 7 -----#

# temp = float(input("ingresa la temperatura en °C: "))
# if temp < 10:
#     print("hace frio")
# elif temp <= 25:
#     print("templado")
# else:
#     print("hace calor")

#----- 8 -----#

# print("1. sumar,2. Restar,3. Multiplicar")
# op = int(input("Elige una opción: "))
# a = float(input("Primer número: "))
# b = float(input("Segundo número: "))

# if op == 1:
#     print("Resultado:", a + b)
# elif op == 2:
#     print("Resultado:", a - b)
# elif op == 3:
#     print("Resultado:", a * b)
# else:
#     print("Opción inválida")

#----- 9 -----#

# meses = {
#     1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
#     5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
#     9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
# }

# numero = int(input("Ingresa un número entre 1 y 12: "))

# if numero in meses:
#     print("Mes correspondiente:", meses[numero])
# else:
#     print("Número inválido")

#----- 10 -----#

# numero = input("Ingresa un número de 4 dígitos: ")

# primer_digito = numero[0]

# if primer_digito == "1":
#     print("Comienza con 1")
# elif primer_digito == "2":
#     print("Comienza con 2")
# else:
#     print("Comienza con otro número")

#----- 11 -----#

# palabra = input("Ingresa una palabra: ")

# primer_caracter = palabra[0]

# vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
# numeros = "0123456789"  

# if primer_caracter in numeros:
#     print("Empieza con un número")
# elif primer_caracter in vocales:
#     print("Empieza con vocal")
# else:
#     print("Empieza con consonante")

#----- 12 -----#

# fruta = input("Ingresa una fruta: ")
# precios = {"manzana": 1500, "pera": 1200, "piña": 1800}
# if fruta in precios:
#     print("Precio:", precios[fruta])
# else:
#     print("No está disponible")

#----- 13 -----#

# nota = float(input("Ingresa tu calificación (0 a 5): "))
# if nota < 3:
#     print("Reprobado")
# elif nota <= 4:
#     print("Aprobado")
# else:
#     print("Excelente")

#----- 14 -----#

# num = int(input("Ingresa un número: "))
# if num % 4 == 0:
#     print("Divisible entre 4")
# elif num % 6 == 0:
#     print("Divisible entre 6")
# else:
#     print("No es divisible entre 4 ni 6")

#----- 15 -----#

# usuarios = {"admin": "1234", "juan": "abcd"}
# usuario = input("Usuario: ")
# clave = input("Clave: ")
# if usuario in usuarios and usuarios[usuario] == clave:
#     print("Acceso concedido")
# else:
#     print("Usuario o clave incorrectos")

#----- 16 -----#

# edad = int(input("Ingresa tu edad: "))
# if edad <= 12:
#     print("Niño")
# elif edad <= 17:
#     print("Adolescente")
# elif edad <= 64:
#     print("Adulto")
# else:
#     print("Mayor")

#----- 17 -----#

# ciudades = ("Bogotá", "Lima", "Buenos Aires", "Ciudad de México")
# ciudad = input("Ingresa el nombre de la ciudad: ")
# if ciudad in ciudades:
#     print("Es capital")
# else:
#     print("Ciudad secundaria")

#----- 18 -----#

# compra = float(input("Valor de la compra: "))
# if compra > 200000:
#     descuento = 0.15
# elif compra >= 100000:
#     descuento = 0.10
# else:
#     descuento = 0
# total = compra * (1 - descuento)
# print(f"Total a pagar: ${total:,.0f}")

#----- 19 -----#

# nombre = input("Nombre: ")
# horas = int(input("Horas trabajadas: "))
# salario = horas * 10000
# if horas > 40:
#     salario *= 1.2
# print(f"{nombre}, tu salario es: ${salario:,.0f}")

#----- 20 -----#

# puntaje = int(input("Ingresa tu puntaje (0 a 100): "))
# if puntaje < 50:
#     print("Insuficiente")
# elif puntaje < 80:
#     print("Aceptable")
# else:
#     print("Sobresaliente")









