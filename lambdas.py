

multiplicacion = lambda x, y: x * y

print(multiplicacion(2, 3))
print(multiplicacion(3, 4))

potencia = lambda x, y: x ** y

print(potencia(2, 3))
print(potencia(3, 4))

es_par = lambda x: x % 2 == 0

print(es_par(2))
print(es_par(3))


datos = [(1, 3), (2, 1), (4, 2), (4, 5)]

ordenado = sorted(datos, key=lambda x: x[0])
print(ordenado)


plabras = ["hola", "adios", "buenos dias", "buenas noches"]

filtro = list(filter(lambda palabra: len(palabra)> 4, plabras))
print(filtro)


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor="Número"
conversion = list(map(lambda x: x / 2, numeros))
print(conversion)