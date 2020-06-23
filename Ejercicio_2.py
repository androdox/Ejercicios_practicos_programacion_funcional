def recursividad(lista, final):
    if lista == []:
        return final
    else:
        return recursividad(lista[1:], final + [multiplicar(lista[0])])


def cambiar(lista):
    return [str(x) for x in lista]


def multiplicar(numero):
    return [int(x) * 3 for x in numero]


print(recursividad(cambiar([123, 456, 789]), []))
