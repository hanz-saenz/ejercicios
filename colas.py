from collections import deque

#crarer la cola vacia
cola = deque()
#agregar elementos a la cola
cola.append("elemento 1")
print("++++++++",cola)
cola.append("elemento 2")
print("++++++++",cola)
cola.append("elemento 3")
print("++++++++",cola)
cola.popleft()
print("-------",cola)
cola.popleft()
print("-------",cola)
cola.popleft()
print("-------",cola)


cola_entrada = []


#funcion para agregar elemento a la cola_entrada
def agregarElemento(elemento):
    cola_entrada.append(elemento)
    print(f" + + + + se agrego el elemento {elemento} a la cola_entrada. \nla cola_entrada es {cola_entrada}")

def eliminarElemento():
    if cola_entrada:
        elementoEliminado = cola_entrada.pop(0)
        print(f" - - - -se elimino el elemento {elementoEliminado} de la cola_entrada. \nla cola_entrada es {cola_entrada}")
    else:
        print("la cola_entrada esta vacia")

agregarElemento("elemento 1")
agregarElemento("elemento 2")
agregarElemento("elemento 3")

eliminarElemento()
eliminarElemento()
eliminarElemento()
eliminarElemento()