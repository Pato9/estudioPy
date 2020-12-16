import math


precios = [12,20,40,5,145,20,30,123,20,40,12,12,1]

sueldos = [1500,1200,1700,1300,1800]

grupo1 = [19,20,20,19,22]
grupo2 = [28,32,30,4,6]

#promedio
def promedio(a):
    return(sum(a)/len(a))

def mediana(a):
    mitad = int(len(a)/2)
    mediana = a[mitad]
    return mediana

def moda(a):
    repeticiones = 0
    for i in a:
        n = a.count(i)
        if n > repeticiones:
            repeticiones = n
    moda = []

    for i in a:
        n = a.count(i)
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda)==1:
        return moda
    else:
        print('En la lista no hay moda!')


def minimo(a):
    return (min(a))

def maximo(a):
    return(max(a))

def rango(a):
    mini = minimo(a)
    maxi = maximo(a)
    return(maxi-mini)

def calcVarianza(a):
    result = 0
    media = promedio(a)
    for i in range(len(a)):
        result = result + (a[i] - media)**2/len(a)

    varianza = result
    return varianza

def desviacionEstandar(a):
    result = 0
    media = promedio(a)
    varianza = calcVarianza(a)
    desviEstandar = math.sqrt(varianza)

    return desviEstandar

def coeVariacion(a):
    desviE = desviacionEstandar(a)
    media = promedio(a)
    cVariacion = desviE/media
    return cVariacion

def porcentaje(num):
    return(num*100)

#print(f'El promedioo es de {promedio(precios)}usd')
#print(f'La mediana es de {mediana(precios)}')
#print(f'La moda es de {moda(precios)}')
#moda(precios)

#print(rango(precios))
print(calcVarianza(grupo1))
desviacionEstandar(grupo1)
cV = round(porcentaje(coeVariacion(grupo1)),2)
cv2 = round(porcentaje(coeVariacion(grupo2)),2 )
print(f'El coeficiente de variacion es de {round(porcentaje(cV),2)}%')
print(f'El coeficiente de variacion del grupo 2 es de {cv2}')
"""
Comparar los 2 grupos y validar cual posee menor desviacion estadar
"""


desvEstandarGrupo1 = round(desviacionEstandar(grupo1),6)
desvEstandarGrupo2 = round(desviacionEstandar(grupo2),6)

print(f'Grupo1 : {desvEstandarGrupo1}, Grupo2 :{desvEstandarGrupo2} ')

if desvEstandarGrupo1<desvEstandarGrupo2:
    print('El grupo 1 posee una menor desviacion estandar')
    print(f'Este grupo posee un coeficiente de variacion de : {cV}')
else:
    print('El grupo 2 posee una menor desbviacion estandar')
    print(cv2)




