#iniciamos pila
pila = []


#funcion para agregar elemento a la pila
def agregarElemento(elemento):
    pila.append(elemento)
    print(f" + + + + se agrego el elemento {elemento} a la pila. \nla pila es {pila}")

def eliminarElemento():
    if pila:
        elementoEliminado = pila.pop()
        print(f" - - - -se elimino el elemento {elementoEliminado} de la pila. \nla pila es {pila}")
    else:
        print("la pila esta vacia")

agregarElemento("elemento 1")
agregarElemento("elemento 2")
agregarElemento("elemento 3")

eliminarElemento()
eliminarElemento()
eliminarElemento()
eliminarElemento()