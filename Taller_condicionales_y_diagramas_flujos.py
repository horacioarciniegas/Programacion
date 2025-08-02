# letra = input("ingresa una volcal en minuscula: ")
# if letra in "aeiou" and not letra in "AEIOU":  
#     print("La vocal en mayuscula es:" , {"a":"A", "e":"E", "i":"I", "o":"O", "u": "U"}[letra])
# else:
#     print("no ingresaste una vocal minuscula.")

#--------------- 1 -----------------#
# numeros= float(input("ingresa un numero (positivo o negativo): "))

# if numeros > 0:
#     print("es un numero positivo")
# elif numeros < 0:
#     print("es un numero negativo")
# else:
#     print("no has pueste ningun numero (negatio o positivo)")

#--------------- 2 -----------------#
# numero1= float(input("ingresa un numero 1: "))
# numero2= float(input("ingresa un numero 2: "))

# if numero1 < numero2:
#     print(f"el numero {numero1} es mayor a {numero2}")
# elif numero1 > numero2:
#     print(f"el numero {numero2} es mayor a {numero1}")
# else:
#     print("ningun numero es igual")

#--------------- 3 -----------------#

# numero = float(input("ingresa un numero: "))
# if numero % 2:
#     print("el numero es impar")
# elif numero % 3:
#     print("el numero es par")
# else:
#     print("no es un numero")

#--------------- 4 -----------------#

# numero = int(input("ingresa un numero: "))

# if numero > 10 and numero < 20:
#     print("si esta entre 10 y 20")
# else:
#     print("no esta entre 10 y 20")

#--------------- 5 -----------------#
# numero1 = int(input("ingresa un numero 1: "))
# numero2 = int(input("ingresa un numero 2: "))
# numero3 = int(input("ingresa un numero 3: "))

# if numero1 >= numero2 and numero1 >= numero3:
#     print(f"el numero mayor es {numero1}")
# elif numero2 >= numero3:
#     print(f"el numero mayor es {numero2}")
# else:
#     print(f"el numero mayor es {numero3}")

#--------------- 6 -----------------#
# total =float(input("ingresa el total de la compra: "))
# if total > 100:
#     precio_final = total - (total * 0.10)
#     print(f"se aplica el descuento del 10%. Precio final: {precio_final}")
# elif total == 100:
#     print(f"total exacto, no se aplica el descuento. Precio final:{total}")
# else:
#     print(f"no hay descuento. Precio final {total}")

#--------------- 7 -----------------#
# edad= int(input("ingresa tu edad: "))
# if edad >= 18:
#     print("si puede votar")
# else:
#     print("no puede votar")

#--------------- 8 -----------------#
# precio = float(input("ingresa el precio: "))
# cliente =input("que tipo de cliente eres? (VIP o normal: ")

# descuento = -precio * 0.20 + precio
# if cliente == "VIP":
   
#    print(f"se aplica el descuento del 20% {descuento}")
# else:
#    print("eres un cliente normal, no se aplica el descuento")

#--------------- 9 -----------------#
# numero = int(input("ingresa un número: "))
# if numero % 3 == 0 and numero % 5 == 0:
#     print("es múltiplo de 3 y 5")
# else:
#     print("no lo es")

#--------------- 10 -----------------#
# numero = int(input(" ingresa un numero: "))
# d1 = int(input("Divisor 1: "))
# d2 = int(input("Divisor 2: "))
# if numero % d1 == 0 and numero % d2 == 0:
#     print("es divisible entre ambos")
# else:
#     print("no es divisible entre ambos")

#--------------- 11 -----------------#
# lista = [5, 4, 11, 3, 7]
# if lista[2] > 10:
#      print("mayor a 10")
# else:
#      print("menor o igual a 10")

#--------------- 12 -----------------#
# lista = [3, 5, 7, 9]
# if 7 and lista:
#     print("está en la lista")
# else:
#     print("no esta en la lista")

#--------------- 13 -----------------#
# lista = [4, 6, 2, 8]
# suma = lista[0] + lista[1]
# if suma > 10:
#     print("suma alta")
# else:
#     print("suma baja")

#--------------- 14 -----------------#
# lista = ["Ana", "Luis", "Pedro","Marta"]
# if lista [3]== "Marta":
#     print("nombre correcto")
# else:
#     print("nombre diferente")

#--------------- 15 -----------------#
# lista = ["rojo", "azul", "verde"]
# if lista[1] == "azul":
#     lista[1] = "celeste"
# print(f"la lista actualizada es: {lista}")

#--------------- 16 -----------------#
# tupla = (5, 8, 12, 20)
# if tupla[0] < tupla[3]:
#     print("orden ascendente")
# else:
#     print("orden descendente")

#--------------- 17 -----------------#
# tupla = (25, 32, 28)
# if tupla[1] > 30:
#     print("edad meyor a 30")
# else:
#     print("edad menor o igual a 30")

#--------------- 18 -----------------#
# tupla =(1, 2, 3)
# lista =list(tupla)
# if lista[1] == 2:
#     lista[1] = 10
# tupla_2 =tuple(lista)
# print(f"la nueva tupla es: {tupla_2}")

#--------------- 19 -----------------#
# tupla =(4, 9)
# if tupla[1] > 5:
#     print("coordenada alta")
# else:
#     print("coordenada baja")

#--------------- 20 -----------------#
# tupla_1 =(3, 4)
# tupla_2= (3, 5)
# if tupla_1 == tupla_2:
#     print("tuplas iguales")
# else:
#     print("tuplas diferentes")

#--------------- 21 -----------------#
# diccionario = {
#     "nombre": "Juan",
#     "edad": 17
# }
# if diccionario["edad"] >= 18:
#     print("adulto")
# else:
#     print("menor de edad")

#--------------- 22 -----------------#
# diccionario = {
#     "nombre": "Lucia",
#     "edad": 20
# }
# if diccionario["edad"] > 18:
#     diccionario["edad"] = 21
# print(diccionario)

#--------------- 23 -----------------#
# diccionario = {
#     "nombre": "Carlos"
# }
# if "ciudad" not in diccionario:
#     diccionario["ciudad"] = "Bogota"
# print(diccionario)

#--------------- 24 -----------------#
# diccionario = {
#     "producto": "pan",
#     "precio": 1200
# }
# if "precio" in diccionario:
#     print(diccionario["precio"])
# else:
#     print("no hay precio")

#--------------- 25 -----------------#
# diccionario = {
#     "pan": 1200,
#     "leche": 2000
# }
# if "pan" in diccionario:
#     print(diccionario["pan"])
# else:
#     print("producto no disponible")
