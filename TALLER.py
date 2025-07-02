#--------  1 Calcula el promedio -------#
# lista=[]

# cal1= float(input("ingresa calificacion 1: "))
# cal2= float(input("ingresa calificacion 2: "))
# cal3= float(input("ingresa calificacion 3: "))

# lista.append(cal1)
# lista.append(cal2)
# lista.append(cal3)

# opecaion= cal1 + cal2 + cal3

# oprcaion2= opecaion / 3

# print(f"{lista}")
# print(f"el promedio es de: {oprcaion2}")

#-------- 2 Actualiza el precio -------#
# productos = {
#     "Papas": 2500,
#     "Galletas": 2000,
#     "Jugo": 3000,
# }
# print(f"{productos}")

# Porcentaje= float(input("aumenta el porcentaje: "))
# productos["Papas"] +=productos["Papas"] * (Porcentaje / 100)
# productos["Galletas"] +=productos["Galletas"] * (Porcentaje / 100)
# productos["Jugo"]+=productos["Jugo"] * (Porcentaje / 100)
# print(f"{productos}")

#-------- 3 Comvercion de temperatura -------#
# c1=float(input("temperatura 1 °C: "))
# c2=float(input("temperatura 2 °C: "))
# c3=float(input("temperatura 3 °C: "))
# c4=float(input("temperatura 4 °C: "))
# c5=float(input("temperatura 5 °C: "))

# celsius = (c1,c2,c3,c4)

# f1= c1 * 9/5 + 32
# f2= c2 * 9/5 + 32
# f3= c3 * 9/5 + 32
# f4= c4 * 9/5 + 32
# f5= c5 * 9/5 + 32

# fahrenheit=(f1,f2,f3,f4,f5)

# print("Temperatura en °C: ", celsius)
# print("Temperatura en °F: ", fahrenheit)

#-------- 4 Edad Promedio co Listas -------#
# listal_edades=[
# int(input("ingresa edad 1: ")),
# int(input("ingresa edad 2: ")),
# int(input("ingresa edad 3: ")),
# int(input("ingresa edad 4: ")),
# int(input("ingresa edad 5: ")),
# ]

# promedio =sum(listal_edades) / len(listal_edades)

# print(f"Edad Mayor: {max(listal_edades)}, Edad Menor: {min(listal_edades)}, Edad Promedio: {listal_edades}")

#-------- 5 Diccionarios de Frutas  -------#
# diccionario_frutas= {
#   "manzana": 5000,
#     "pera": 4500,
#     "uva": 3000,
# }

# frutas=float(input("ingresa cuanto kilos de manzana: "))
# frutas+=float(input("ingresa cuanto kilos de pera: "))
# frutas+=float(input("ingresa cuanto kilos de uva: "))

# total=()

# kg = float(input(f"cuantos kg de {frutas} quieres"))
# total+=frutas[frutas] * kg
# print("total a pagar:", total)

#-------- 6 Suma de elementos en tuplas  -------#
# numeros = (1,2,3,4,5)
# print("suma", sum(numeros))

#-------- 7 Inventario con lista se diccionario  -------#
# Entrada manual para 3 productos
# d1 = {"nombre": input("Producto 1: "), 
#       "cantidad": int(input("Cantidad 1: ")), 
#       "precio": float(input("Precio 1: "))}

# d2 = {"nombre": input("Producto 2: "), 
#       "cantidad": int(input("Cantidad 2: ")), 
#       "precio": float(input("Precio 2: "))}

# d3 = {"nombre": input("Producto 3: "), 
#       "cantidad": int(input("Cantidad 3: ")), 
#       "precio": float(input("Precio 3: "))}

# # Lista del inventario
# inventario = [d1,d2,d3]

# # Cálculo del total sin usar bucles
# total = (
#     d1["cantidad"] * d1["precio"] +
#     d2["cantidad"] * d2["precio"] +
#     d3["cantidad"] * d3["precio"]
# )

# print("Total del inventario:", total)

#-------- 8 Modificar una lista de precios  -------#
# a = float(input("Valor 1: "))
# b = float(input("Valor 2: "))
# c = float(input("Valor 3: "))
# d = float(input("Valor 4: "))
# e = float(input("Valor 5: "))

# des = float(input("Descuento (%): ")) / 100

# a_d = a - (a * des)
# b_d = b - (b * des)
# c_d = c - (c * des)
# d_d = d - (d * des)
# e_d = e - (e * des)

# res = [a_d, b_d, c_d, d_d, e_d]

#print("Valores con descuento:", res)

#-------- 9 Notas con tuplas  -------#
# a = float(input("Nota uno: "))
# b = float(input("Nota dos: "))
# c = float(input("Nota tres: "))
# d = float(input("Nota cuatro: "))

# valores = (a, b, c, d)

# mayor = max(valores)
# menor = min(valores)

# print("Mayor:", mayor)
# print("Menor:", menor)

#-------- 10 Diccionario de conversiones  -------#
# conversiones = {"km": 1000, "m": 1, "cm": 0.01}
# unidad = input("Unidad (km/m/cm): ")
# cantidad = float(input("Cantidad: "))
# print("Equivalente en metros:", cantidad * conversiones[unidad])

#-------- 11 Lista de productos más IVA-------#
# a = float(input("Valor 1: "))
# b = float(input("Valor 2: "))
# c = float(input("Valor 3: "))
# d = float(input("Valor 4: "))
# e = float(input("Valor 5: "))

# iva = 0.19

# a_iva = a + (a * iva)
# b_iva = b + (b * iva)
# c_iva = c + (c * iva)
# d_iva = d + (d * iva)
# e_iva = e + (e * iva)

# con_iva = [a_iva, b_iva, c_iva, d_iva, e_iva]

# print("Valores con IVA:", con_iva)

#-------- 12 Tupla de operaciones matemáticas-------#
# a = float(input("Número uno: "))
# b = float(input("Número dos: "))

# resultados = (a + b, a - b, a * b, a / b)

# print("Resultados (suma, resta, mult, div):", resultados)

#-------- 13 Diccionario de estudiantes-------#
# estudiantes = {
#     "Ana": 4.5,
#     "Luis": 3.8,
#     "María": 4.2
# }
# promedio = sum(estudiantes.values()) / len(estudiantes)
# print("Promedio general:", promedio)

#-------- 14 Lista de salarios-------#
# a = float(input("Salario 1: "))
# b = float(input("Salario 2: "))
# c = float(input("Salario 3: "))
# d = float(input("Salario 4: "))
# e = float(input("Salario 5: "))

# a_nuevo = a * 1.10
# b_nuevo = b * 1.10
# c_nuevo = c * 1.10
# d_nuevo = d * 1.10
# e_nuevo = e * 1.10

# nuevos = [a_nuevo, b_nuevo, c_nuevo, d_nuevo, e_nuevo]

# print("Salarios con aumento:", nuevos)

#-------- 15 Diccionario de impuestos-------#
# a = float(input("Valor 1: "))
# b = float(input("Valor 2: "))
# c = float(input("Valor 3: "))

# t = float(input("Porcentaje de carga: ")) / 100

# a_f = a + (a * t)
# b_f = b + (b * t)
# c_f = c + (c * t)

# res = {"uno": a_f, "dos": b_f, "tres": c_f}

# print("Valores finales:", res)

#-------- 16 Análisis de lista de edades-------#
# a = int(input("Edad 1: "))
# b = int(input("Edad 2: "))
# c = int(input("Edad 3: "))
# d = int(input("Edad 4: "))
# e = int(input("Edad 5: "))


# mayores = (a >= 18) + (b >= 18) + (c >= 18) + (d >= 18) + (e >= 18)
# menores = 5 - mayores

# print("Mayores de edad:", mayores)
# print("Menores de edad:", menores)

#-------- 17 Tupla de conversiones de moneda-------#
# usd = float(input("Cantidad en dólares: "))
# conversiones = (usd * 0.85, usd * 3800, usd * 110.5) 
# print("Euros, Pesos, Yenes:", conversiones)

#-------- 18 Diccionario de ventas-------#
# a_nom = input("Nombre del producto 1: ")
# a_cant = int(input("Cantidad vendida de producto 1: "))

# b_nom = input("Nombre del producto 2: ")
# b_cant = int(input("Cantidad vendida de producto 2: "))

# c_nom = input("Nombre del producto 3: ")
# c_cant = int(input("Cantidad vendida de producto 3: "))

# ventas = {
#     a_nom: a_cant,
#     b_nom: b_cant,
#     c_nom: c_cant
# }

# total = ventas[a_nom] + ventas[b_nom] + ventas[c_nom]

# print("Total unidades vendidas:", total)

#-------- 19 Lista de temperaturas extremas-------#
# a = float(input("Dato 1: "))
# b = float(input("Dato 2: "))
# c = float(input("Dato 3: "))
# d = float(input("Dato 4: "))
# e = float(input("Dato 5: "))
# f = float(input("Dato 6: "))
# g = float(input("Dato 7: "))
# h = float(input("Dato 8: "))
# j = float(input("Dato 9: "))
# k = float(input("Dato 10: "))

# mayor = []
# menor = []

# (a > 30) * mayor.append(a)
# (a < 10) * menor.append(a)

# (b > 30) * mayor.append(b)
# (b < 10) * menor.append(b)

# (c > 30) * mayor.append(c)
# (c < 10) * menor.append(c)

# (d > 30) * mayor.append(d)
# (d < 10) * menor.append(d)

# (e > 30) * mayor.append(e)
# (e < 10) * menor.append(e)

# (f > 30) * mayor.append(f)
# (f < 10) * menor.append(f)

# (g > 30) * mayor.append(g)
# (g < 10) * menor.append(g)

# (h > 30) * mayor.append(h)
# (h < 10) * menor.append(h)

# (j > 30) * mayor.append(j)
# (j < 10) * menor.append(j)

# (k > 30) * mayor.append(k)
# (k < 10) * menor.append(k)

# print("Temperaturas mayores a 30:", mayor)
# print("Temperaturas menores a 10:", menor)

#-------- 20 Actualizacion precios con metodos de listas-------#
# a = float(input("Valor 1: "))
# b = float(input("Valor 2: "))
# c = float(input("Valor 3: "))
# d = float(input("Valor 4: "))
# e = float(input("Valor 5: "))

# valores = [a, b, c, d, e]

# elim = float(input("Valor a eliminar: "))
# nuevo = float(input("Valor a agregar: "))

# valores.remove(elim)
# valores.append(nuevo)

# valores.sort()

# print("Lista ordenada:", valores)


