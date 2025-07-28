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
