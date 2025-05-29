import re

#cualquier carcater que no sean lineas


#PATRONES COMUNES
texto = "Mi código en python _ -"
#Bucar cualquier caracter 

patron = r"M.................n"

busqueda = re.search(patron, texto)
print(busqueda.group())

#busquedad d numeros
digitos = "Mi numero es 123456789"
patron = r"\d+"
busqueda = re.findall(patron, digitos)
print(busqueda)

#busqueda diferente a numeros
digitos = "Mi numero es 123456789"
patron = r"\D+"
busqueda = re.findall(patron, digitos)
print(busqueda)

#busqueda alfanumerios
alfanumerico = "abc 5-4 *"
patron = r"\w+"
busqueda = re.findall(patron, alfanumerico)
print(busqueda)


#busqueda no alfanumerios
alfanumerico = "abc 5-4 *"
patron = r"\W+"
busqueda = re.findall(patron, alfanumerico)
print(busqueda)

# busqueda espacioe en blanco, saltos de linea y tabs
espacios = "Mi numero es 123456789\n \t"
patron = r"\s+"
busqueda = re.findall(patron, espacios)
print(busqueda)

# busqueda no espacioe en blanco, saltos de linea y tabs
espacios = "Mi numero es 123456789\n \t"
patron = r"\S+"
busqueda = re.findall(patron, espacios)
print(busqueda)



#CUANTIFICADORES

#CONCIDENCIA DE 0 O MAS VECES

texto = "abc123"
patron = r"ab*"
busqueda = re.findall(patron, texto)
print(busqueda)


#CONCIDENCIA DE 1 O MAS VECES

texto = "abc123 ab ab"
patron = r"ab+"
busqueda = re.findall(patron, texto)
print(busqueda)


#CONCIDENCIA DE 0 O 1 VECES

texto = "abc123"
patron = r"2?"
busqueda = re.findall(patron, texto)
print(busqueda)

#concidencia de n veces

texto = "abc123"
patron = r"\d{2}"
busqueda = re.findall(patron, texto)
print(busqueda)

#concidencia de n veces entre n veces

texto = "abc45123678"
patron = r"\d{2,3}"
busqueda = re.findall(patron, texto)
print(busqueda)


#Funciones del Módulo re

texto = "Hola. ¿Cómo estas?"
patron = r"^Hola"
busqueda = re.match(patron, texto)

if busqueda:
    print("Se inicio un saludo")
else:
    print("No saludo")


texto = "Hola. ¿Como estas?"
patron = "estas"
busqueda = re.search(patron, texto)

if busqueda:
    print("encontro")
    print("palabra",busqueda.group())
    print("indice_inicio",busqueda.start())
    print("indice_final",busqueda.end())
    indice_inicial = busqueda.start()
    indice_final = busqueda.end()
    print(texto[indice_inicial:indice_final])
else:
    print("No encontro")


texto =" el numero es 123-456-7890 y el otro numero es 987-654-321"

patron = r"\d{3}-\d{3}-\d{3}"
busqueda = re.findall(patron, texto)

print(busqueda)


texto = "mi contraseña es 12345"

patron = r"\d+"

texto = re.sub(patron, "*****", texto)
print(texto)