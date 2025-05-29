
#decorador 1
import time
def decorador_prints(funcion):
    def wrapper():
        print("antes de la llamada")
        funcion()
        print("despues de la llamada")
    return wrapper

def logs_ejecucion(funcion):
    def wrapper(*args, **kwargs):
        print(f'Función ejecutandose {funcion.__name__}')
        print(f"argumentos: args: {args}, kwargs: {kwargs}")
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()

        print(f"Resultado: {resultado}")
        print(f"Tiempo de ejecucion: {fin - inicio:.4f} segundos")
        return resultado
    return wrapper


#decorador de permisos

# roles_permitidos = ['admin', 'editor']

# def validacion_rol(funcion):
#     def wrapper(usuario, *args, **kwargs):
#         rol = getattr(usuario, 'rol', None)

#         if rol not in roles_permitidos:
#             raise PermissionError(f"El usuario {usuario} no tiene permiso para realizar esta accion")
        
#         print(f"El usuario {usuario} tiene permiso para realizar esta accion")
#         return funcion(usuario, *args, **kwargs)
#     return wrapper




@decorador_prints
def saludar():
    print("hola")

saludar()



@logs_ejecucion
def sumar(a, b):
    return a + b

sumar(1, 2)
@logs_ejecucion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    #F = F(n-1) + F(n-2)
print(f"fibonacci {fibonacci(1)}")



# @validacion_rol(["admin", "editor"])
# def eliminar_usuario(usuario, id_usuario):
#     print(f"Eliminando el usuario {usuario}, con id {id_usuario}")

# admin = Usuario("admin", "admin")
# eliminar_usuario(admin, 1)


#opcion 2

from functools import wraps
def validad_rol(roles_permitidos):
    def decorador(funcion):
        @wraps(funcion)
        def wrapper(usuario, *args, **kwargs):
            rol = getattr(usuario, 'rol', None)

            if rol not in roles_permitidos:
                raise PermissionError(f"El usuario {usuario.nombre} no tiene permiso para realizar esta accion")
            
            print(f"El usuario {usuario.nombre} tiene permiso para realizar esta accion")
            return funcion(usuario, *args, **kwargs)
        return wrapper
    return decorador

class Usuario:
    def __init__(self, nombre, rol):
        self.rol = rol
        self.nombre = nombre


@validad_rol(["superuser", "editor"])
def eliminar_usuario(usuario, id_usuario):  
    print(f"Eliminando el usuario {usuario.nombre}, con id {id_usuario}")

admin = Usuario("admin", "superuser")
eliminar_usuario(admin, 1)