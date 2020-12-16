import math


grupo1 = [19,20,20,19,22]
grupo2 = [28,32,30,4,6]



def media(a):
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
        moda = moda[0]
        return moda
    else:
        return('No posee moda')

def median(a):
    l = len(a)
    sArray = sorted(a)
    if l % 2 == 0:
        """
        pos-> len(a)/2 = (2*l/4)

        par 2 43 30 20

        i =    0  1  2  3 ....
        sorted 2 20 30 43

        pos->30
        median = (30+20) / 2 = 35

        """
        pos = int((2*l)/4)
        median = (sArray[pos]+sArray[pos-1])/2
        return median
    else:
        pos = int((2*(l+1))/4)
        median = sArray[pos]
        return median


"""
medidas de dispercion
Rango,varianza,desviacion estandar, coe de variacion

Rango = max-min

n = total de numeros
  -
**x = promedio             -  2
Varianza = sumatoria de (Xi-x) / n
Varianza = promedio de las deviaciones cuadraticas de las observaciones
respecto a la media(promedio), mide el grado de dispercion de los varoles
respecto a la media aritmetica

desviacion estandar = se define como la raiz cuadrada de la varianza
ya que como la varianza tiene de unidad de medida el cuadrado,se
hace un poco mas dificil su interpretacion.

    sqrt = raiz cuadrada
            sqrt(varianza)

coe de variacion = se define como la razon entre la desviacion estandar
y la media aritmetica, normalmente se expresa como porcentaje.

           -
    cv = o/x = s -> desviacion estandar
            ______
               _
               x   -> media aritmetica
"""





def rango(a):
    return max(a)-min(a)

def varianza(a):
    aux = 0
    l = len(a)
    promedio = media(a)
    for i in range(len(a)):
        aux = aux +(a[i] - promedio)**2/(l-1)
    return aux

def desviEstandar(a):
    var = varianza(a)
    return math.sqrt(var)

def coeVar(a):
    s = desviEstandar(a)
    x = media(a)
    return s/x


print(f""" grupo 1 \n

Promedio : {media(grupo1)}
Moda : {moda(grupo1)}
mediana : {median(grupo1)}
rango : {rango(grupo1)}
Varianza : {varianza(grupo1)}
Desviacion estandar : {desviEstandar(grupo1)}
Coeficiente de variacion  : {coeVar(grupo1)}
""")

print(f"""  grupo 2 \n
Promedio : {media(grupo2)}
Moda : {moda(grupo2)}
Mediana : {median(grupo2)}
Rango : {rango(grupo2)}
Varianza : {varianza(grupo2)}
Desviacion estandar : {desviEstandar(grupo2)}
Coeficiente de variacion : {coeVar(grupo2)}""")

