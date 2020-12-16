
"""
Calcular los deciles de las notas finales en matematicas de 20
estudiantes

obtener los deciles!!

"""

notas = [25,28,30,30,35,35,36,37,37,38,40,40,
        40, 40 ,40 ,40 ,41 ,43,48,50]


def promedio(a):
    return (sum(a)/len(a))

def moda(a):
    repeticiones = 0
    for i in a:
        n = a.count(i)
        if n>repeticiones:
            repeticiones = n
    moda = []
    for i in a:
        n = a.count(i)
        if n == repeticiones and i not in moda:
            moda.append(i)
    if len(moda)==1:
        return moda
    else:
        return('no se ha encontrado moda')

def mediana(a):
    l = len(a)
    sorted_array = sorted(a)
    if l % 2 !=0:
        mitad = l/2
        median = sorted_array[mitad]
        return median
    else:
        mitad = l/2
        median = (sorted_array[mitad]+sorted_array[mitad-1])/2
        return metian

"""

calcular decil 10

"""

def decil1(a):
    l = len(a)
    sorted_array = sorted(a)
    if l % 2 !=0:
        pos = int((1*l+1)/10)
        deci1 = sorted_array[pos]
        return deci10
    else:
        pos = int((1*l)/10)
        deci1 = (sorted_array[pos]+sorted_array[pos-1])/2
        return deci1

def decil4(a):
    l = len(a)
    sorted_array = sorted(a)
    if l % 2 != 0:
        pos = int((4*(l+1))/10)
        deci4 = sorted_array[pos]
        return deci4
    else:
        pos = int((4*l)/10)
        deci4 = (sorted_array[pos]+sorted_array[pos-1])/2
        return deci4


print(sorted(notas))
print(f'decil 1 : {decil1(notas)}')
print(f'decil 4:  {decil4(notas)}')





