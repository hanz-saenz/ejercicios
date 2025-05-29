

# Variables

edad = 33
Edad = 34

print("Esta es la variable edad:", edad)
print("Esta es la variable edad:" + str(Edad))
print(f"Esta es otra concatenada: {edad}")

print(type(edad))

nombre = "Fernando"
print(f"Mi nombre es: {nombre}")
print(type(nombre))

valor_pi = 3.1416
print(f"El valor de pi es: {valor_pi}")
print(type(valor_pi))

es_estudiante = False
print(f"Soy estudiante: {es_estudiante}")
print(type(es_estudiante))

frutas = ["Manzana", "Pera", "Piña", True, 3.14, 33]
print(f"Las frutas son: {frutas}")
print(type(frutas))
nuevas_lista = [1, 2, 3, 4, 5]
print(f"Las nuevas frutas son: {nuevas_lista}")

lista_general = [frutas, nuevas_lista]
print(f"Las listas son: {lista_general}")
print(type(lista_general))

lista_erro = ["nombre","Fernando"]
print(f"Las listas son: {lista_erro}")
print(type(lista_erro))

diccionario_estudiante = {
    "nombre": "Andres", 
    "edad": 33, 
    "es_estudiante": True, 
    "valor_pi": 3.1416
    }

print(f"El estudiante es: {diccionario_estudiante}")
print(type(diccionario_estudiante))
# ver los valores del diccionario
print(f"El estudiante tiene es: {diccionario_estudiante["edad"]} años")
# ver los valores de una lista
print(f"valor 1 de la lista: {frutas[5]}")
print(len(frutas))
diccionario_combinado = {
    "frutas": frutas,
}
print(f"El diccionario combinado es: {diccionario_combinado}")
print(f"El diccionario combinado es: {diccionario_combinado['frutas']}")
print(type(diccionario_combinado['frutas']))

diccionario_numerico = {
    0: 0,
    1: "string",
    2: True,
    3: 3.14,
    4: frutas
}
print(f"El diccionario numerico es: {diccionario_numerico}")
print(type(diccionario_numerico))
print(f"El diccionario numerico es: {diccionario_numerico[4]}")


# Ciclos
# Operadores
#  = asignacion
#  == igual
#  != diferente
#  > mayor
#  < menor
#  >= mayor o igual
#  <= menor o igual
# === identico
# !== no identico

# Operadores logicos
#  and - y
#  or - o
#  not - no

# Operadores de asignacion
#  += sumar
numero = 10
numero += 1
print(f"El numero es: {numero}")
#  -= restar
#  *= multiplicar
#  /= dividir
#  %= modulo
#  **= potencia

#  IF
print()
print()
numero = 10 +1-2
if (numero == 10):
    print("El numero es 10")
elif (numero != 9):
    print(f"El numero no es 10: {numero}")
elif (numero < 10):
    print(f"El numero es menor a 10: {numero}")
elif (numero > 10):
    print(f"El numero es mayor a 10: {numero}")
else:
    print(f"El numero es diferente a los valores: {numero}")

numero = 10
valor = "stringe"

if (numero == 10 or valor == "string"):
    print("El numero es 10 y el valor es string")
else:
    print("El numero no es 10 o el valor no es string")


# modulo

a = 3
b = 2

a %= b
print(f"El modulo es: {a}")

# while

contador = 10
while contador == 10:
    print(f"El contador es: {contador}")
    contador += 1


for i in range(10):
    print(f"El contador es: {i}")

for fruta in frutas:
    print(f"La fruta es: {fruta}")

for diccionario in diccionario_estudiante:
    print(f"El diccionario es: {diccionario_estudiante[diccionario]}")

for clave, valor in diccionario_estudiante.items():
    print(f"La clave es: {clave} y el valor es: {valor}")



# try

a = 3
b = 2


try:
    resultado = a / b
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print(f"El resultado es: {resultado}") 
finally:
    print("Fin del programa") 

try:
    numero = int("5")
except ValueError:
    print("El valor ingresado no es un numero")
else:
    print(f"El numero ingresado es: {numero}")
finally:
    print("Fin del programa")


try:
    valor = 5/"5"
except Exception as e:
    print(f"El error es: {e}")
else:
    print(f"El valor es: {valor}")
finally:
    print("Fin del programa")


# funcion

def saludar(nombre, valor, valor2=0):
    saludo = f"Hola {nombre} {valor}, {valor2}"
    return saludo

saludo = saludar("Fernando", 1, 2)
print(saludo)