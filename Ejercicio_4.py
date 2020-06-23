class Nodo():
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha


def en_orden(arbol):
    if arbol == None:
        return []
    return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)


def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor > valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)
    return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor))


def ins_lista(arbol, lista):
    if lista == []:
        return arbol
    return ins_lista(insertar(arbol, lista[0]), lista[1:])


def recursividad(lista, final):
    if lista == []:
        return final
    else:
        return recursividad(lista[1:], final + [separar(lista[0])])


def cambiar(lista):
    return [str(x) for x in lista]


def separar(numero):
    return [int(x) for x in numero]


print(recursividad(cambiar(en_orden(ins_lista(None, [25, 15, 20, 50]))), []))
