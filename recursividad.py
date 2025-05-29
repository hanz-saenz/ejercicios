

#Fibonacci

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    #F = F(n-1) + F(n-2)
print(f"fibonacci {fibonacci(2)}")

#factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(5*4*3*2*1)   
print(f"factorial {factorial(5)}")


# contadores regresivos

def contador_regresivo(n):
    if n == 0:
        print('fin')
    else:
        print(n)
        contador_regresivo(n-1)

contador_regresivo(10)

#invertir cadena de caracteres

def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

print(invertir_cadena("curso de python"))