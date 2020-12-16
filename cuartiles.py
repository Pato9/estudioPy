import math

edades = [36,25,27,24,39,20,36,45,31,21,39,24,29,23,41,83,33,24,34,40]

"""
    calcular medidas de tendecia central

    media = promedio
    moda
    mediana

"""

#TODO: se necesita terminar lo ultimo....

def media(a):
    # len() -> largo de una cadena de texto,arreglo,lista,tupla,etc..
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
        return moda

def mediana(a):
    #sorted()-> [2,4,1,3,5] -> [1,2,3,4,5]
    orden = sorted(a)
    l = len(a) # ->
    if l % 2 != 0:
        #Q2 = mediana
        pos = int((2*(l+1)/4))
        q2 = orden[pos]
        return q2
    else:
        #Q2 = mediana
        pos = int((2*(l)/4))
        q2 = (orden[pos]+orden[pos-1])/2
        return q2
print(sorted(edades))
print(f""" medidas de tendencia central\n
media : {media(edades)}
moda :  {moda(edades)}
mediana : {mediana(edades)}
""")


"""

    calcular medidas de tendencia no central

    se debe retilizar funcion mediana ya que es igual al Q2

    calcular IQR y valores atipicos
"""

def Q1(a):
    orden = sorted(a)
    l = len(a)
    if l % 2 !=0:
        pos = int(1*(l+1)/4)
        q1 = orden[pos]
        return q1
    else:
        pos = int((1*l)/4)
        q1 = (orden[pos]+orden[pos-1])/2
        return q1

def Q3(a):
    orden = sorted(a)
    l = len(a)
    if l % 2 != 0: # -> impar
        pos = int((3*(l+1))/4)
        q3 = orden[pos]
        return q3
    else:
        pos = int((3*l)/4)
        q3 = (orden[pos]+orden[pos-1])/2
        return q3

#TEST DE TUKEY
def IQR(a):
    q3 = Q3(a)
    q1 = Q1(a)
    return q3 - q1

"""
    valores atipicos leves 1.5
"""
def LS(a):
    q3 = Q3(a)
    iqr = IQR(a)
    form = q3 + (1.5 * iqr)
    return form

def LI(a):
    q1 = Q1(a)
    iqr = IQR(a)
    form = q1 - (1.5 * iqr)
    return form

def minimo(a):
    orden = sorted(a)
    li = LI(a)
    minimo = ([i for i in orden if i<li])
    if len(minimo) == 0:
        minimo = orden[0]
    else:
        minimo = li
    return minimo

def maximo(a):
    orden = sorted(a)
    ls = LS(a)
    maximo = ([i for i in orden if i>ls])
    if len(maximo)!=0:
        maximo = ls
        return maximo
    else:
        return maximo

def valorAtipicoS(a):
    maxi = maximo(a)
    va = ([i for i in a if i>maxi])
    return va

print(f'Q1 : {Q1(edades)}')
print(f'Q2 : {mediana(edades)}')
print(f'Q3 : {Q3(edades)}')
print(f'IQR : {IQR(edades)}')
print(f'LS : {LS(edades)}')
print(f'LI : {LI(edades)}')
print(f'minimo : {minimo(edades)}')
print(f'maximo {maximo(edades)}')
print(f'valor atipico :  {valorAtipicoS(edades)}')

"""
    calcular medidas de dispercion

    rango o amplitud
    varianza,
    desviacion estandar,
    coeficiente de variacion

"""

def variacion(a):
    return max(a) - min(a)

def varianza(a):
    l = len(a)
    aux = 0
    x = media(a)
    var = float(0)
    for i in range(len(a)):
        aux = aux + ((a[i]-x)**2/(l-1))
    var = aux
    return var

def desviacionEstandar(a):
   var = varianza(a)
   return round(math.sqrt(var),7)


def coeVariacion(a):
    s = desviacionEstandar(a)
    x = media(a)
    return s/x

def porcentaje(num):
    return num*100

print(f'varianza :  {varianza(edades)}')
print(f'desviacion estandar : {desviacionEstandar(edades)}')
print(f'El coeficiente de variaron es de {porcentaje(coeVariacion(edades))}')




