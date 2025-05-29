


# lista de inicio

numeros = [ 3, 5, 8,7 ,9 ,1 , 8]

print(f"Lista inicial {numeros}")

#AGREGAR UN NUEVO ELEMENTO

## Opción 1. append

numeros.append(10)
print(f"Lista con append {numeros}")

## Opción 2 insert

numeros.insert(5, 2)
print(f"Lista con insert {numeros}")


# ELIMINAR UN ELEMENTO

## Opción 1 remove
## Elimina por valor
numeros.remove(8)
print(f"Lista con remove {numeros}")


## Opción 2 pop
# Elimina por indice
numeros.pop(7)
print(f"Lista con pop {numeros}")

#ORDENAR UNA LISTA
numeros.sort()
print(f"Lista con sort {numeros}")

#REVERSA
numeros.reverse()
print(f"Lista con reverse {numeros}")

numeros.append(7)
numeros.append(8)

#ELIMINAR DUPLICADO

## SET
numeros_sin_duplicados = list(set(numeros))
print(f"Lista con duplicados {numeros}")
print(f"Lista sin duplicados set {numeros_sin_duplicados}")

## for (no tan recomendada)
nueva_lista = []

for numero in numeros:
    if numero not in nueva_lista:
        nueva_lista.append(numero)

print(f"Lista sin duplicados for {nueva_lista}")

## dict.fromkeys

lista_final = list(dict.fromkeys(numeros))
print(f"Lista sin duplicados dict.fromkeys {lista_final}")


#TUPLAS

colores = ("amarillo", 'azul', "rojo", 'verde')
print(type(colores))

print(colores[0])
print(colores[1])
print(colores[2])
print(colores[3])

boton_primary = ("azul", "10px", "bold", "20px")

color, border, weight, size = boton_primary

amarillo, azuul, rojo, verde = colores

print(amarillo)
print(azuul)
print(rojo)
print(verde)


#CONJUNTOS

#asiganr por llaves

conjunto_primero = {1, 2, 5, 4, 6}
conjunto_segundo = set({9, 2, 5, 7, 6})

print(conjunto_primero)
print(conjunto_segundo)
print(type(conjunto_segundo))
print(type(conjunto_segundo))


union = conjunto_primero.union(conjunto_segundo)
print(f"union {union}")

interseccion = conjunto_primero.intersection(conjunto_segundo)
print(f"interseccion {interseccion}")


diferencia_conjunto_primero = conjunto_primero.difference(conjunto_segundo)
print(f"diferencia {diferencia_conjunto_primero}")


diferencia_conjunto_segundo = conjunto_segundo.difference(conjunto_primero)
print(f"diferencia {diferencia_conjunto_segundo}")



#DICCIONARIOS


estudiante = {
    'nombre': 'Fernando',
    'apellido': 'Garcia',
    'edad': 23, 
    'curso': 'Python'
    }

print(estudiante.keys())
print(estudiante.values())

## get

print(estudiante['apellido'])
print(estudiante.get('apellido'))

#eliminar

estudiante.pop('apellido')
print(estudiante)


#agregar

estudiante['apellido'] = 'Garcia'
print(estudiante)


#METODOS PARA MANIPULACIÓN DELISTAS

# EXTEND

letras = ['a', 'b', 'i', 'd', 'g', 'f', 'c', 'e', 'h']
print(f"letras {letras}")
nuevas_letras = ['c', 'e', 'h']
letras.extend(nuevas_letras)
print(f"letras extend {letras}")

nuevas_letras.clear()
print(f"letras clear nuevas_letras {nuevas_letras}")

#count

print(f"letras count a {letras.count('a')}")
print(f"letras count c {letras.count('c')}")

print(f"Indice de la letra a {letras.index('a')}")
letras.remove('c')
print(f"Indice de la letra c {letras.index('c')}")



import array


numeros_array = array.array('i', [1, 2, 3, 4, 5, 6])

print(f" array inicial {numeros_array}")

numeros_array.append(7)
print(f" array con append {numeros_array}")


numeros_array.insert(3, 8)
print(f" array con insert {numeros_array}")


numeros_array.remove(6)
print(f" array con remove {numeros_array}")


numeros_array.pop(3)
print(f" array con pop {numeros_array}")

numeros_array.insert(5, 6)
print(f" array con insert {numeros_array}")

numeros_array.reverse()
print(f" array con reverse {numeros_array}")

