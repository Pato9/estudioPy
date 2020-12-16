
import math

"""
Analizar 2 grupos de autos con velocidades distintas
saber cuando es la media,moda,mediaa de cada grupo ademas
de obtener el rango, varianza, desviacion estandar, y coeficiente de
variacion, saber cuando tiene menos dispercion en sus datos
"""
grupo1 = [100,200,150,90,120,133,132,232]
grupo2 = [200,55,70,230,140,230,200,40,221,154]

def media(a):
    return (sum(a)/len(a))

def moda(a):
    repeticiones = 0
    for i in a:
        n = a.count(i)
        if n > repeticiones:
            repeticiones = n
    arrayModa = []
    for i in a:
        n = a.count(i)
        if n == repeticiones and i not in arrayModa:
            arrayModa.append(i)
    if len(arrayModa)==1:
        return arrayModa
    else:
        return ('No posee moda:(')


def mediana(a):
    l = len(a)
    sorted_array = sorted(a)
    print(sorted_array)
    if l % 2 != 0:
        pos = int((2*(l+1))/4)
        print(f'pos = {pos}')
        median = sorted_array[pos]
        return median
    else:
        pos = int((2*l)/4)
        median = (sorted_array[pos]+sorted_array[pos-1])/2
        print(pos)
        return median

def rango(a):
    mini = min(a)
    maxi = max(a)
    return maxi-mini
"""
Calculo de varianza poblacional

"""
def calcVarianzaMuestral(a):
    aux = 0
    promedio = media(a)
    largo = len(a)
    for i in range(len(a)):
        aux = aux + ((a[i] - promedio)**2/(largo-1))
    varianza = aux
    return varianza

def desviacionEstandar(a):
    varianza = calcVarianzaMuestral(a)
    desviacion = round(math.sqrt(varianza),4)
    return desviacion

def coeVariacion(a):
    desvi = desviacionEstandar(a)
    promedio = media(a)
    return round(desvi/promedio*100,2)


def hola(a):
    x = media(a)
    result = x**2 - (x)**2
    return result

print(f""" Datos grupo1 \n
promedio : {media(grupo1)}
mediana :  {mediana(grupo1)}
moda : {moda(grupo1)}
rango : {rango(grupo1)}
varianza : {calcVarianzaMuestral(grupo1)}
desviacion estandar : {desviacionEstandar(grupo1)}
coeficiente de variacion : {coeVariacion(grupo1)}
""")

print(f""" datos grupo 2\n
promedio : {media(grupo2)}
mediana : {mediana(grupo2)}
moda : {moda(grupo2)}
rango : {rango(grupo2)}
varianza : {calcVarianzaMuestral(grupo2)}
desviacion estandar : {desviacionEstandar(grupo2)}
coeficiente de variacion : {coeVariacion(grupo2)}
""")





