def recursividad(lista, final):
    if lista == []:
        return final
    else:
        return recursividad(lista[1:], final + [hallar(lista[0])])

def hallar(sublista):
    return [max(sublista), min(sublista), max(sublista) + min(sublista)]


print(recursividad([[1, 3, 5, 10], [6, 2, 8, 9]], []))
