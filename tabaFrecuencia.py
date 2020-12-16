


"""

Cantidades de veces en que alumnos han ido a un cine el ultimo
mes

!realizar tabla de frecuencia para cada dato

"""

idaCine = [2,3,0,1,5,3,2,3,0,0,2,1,2,1,0,2,1,1,1,3,4,0,0,2,1]


def xi (a):
    numeros = []
    for i in a:
        if i not in numeros:
            numeros.append(i)
    sortA = sorted(numeros)
    return sortA

xiCine = xi(idaCine)

def frecuenciaA(a):
    lista = xi(a)
    ordenA = sorted(a)
    repeticiones = []

    #TODO: validar la variable lista con el orden a y
    #      encontrar la repeticiones de las litas

    for i in ordenA:
        for j in lista:
            if i in ordenA:
                n = ordenA.count(i)
        repeticiones.append(n)

    print(repeticiones)

    if len(repeticiones)>0:
        print('si hay repeticiones')

frecuenciaA(idaCine)




