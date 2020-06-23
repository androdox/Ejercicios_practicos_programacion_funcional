def entero(lista, final):
    if lista == []:
        return final
    else:
        return eliminar(lista, final + str(lista[0] % 10))


def eliminar(lista, final):
    return entero(lista[1:], final)


print(entero([22, 55], ''))
