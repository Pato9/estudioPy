"""

Se estudio el rebotre de una pelota y se concluyo que la altura
del rebote decrecia segun potencias de 0.9 es decir que se deja
caer 1 metro de altura, el primero rebote media 0,9m de alto
el segundo (0,9)**2 ....

"""

rebotes = [3,5,8,10,20]

def rebote(r):


    """
    m->metros
    funcion = f(x)=m*(0,9)**x
    """
    CONST_METRO  = 1
    result = CONST_METRO * (0.9)**r
    return result

"""
1) calcula la medida de la altura que alcanzo la pelota en el tercer rebote

"""

input_rebote = int(input('Para consultar la altura del debote ingrese cual desea consulta(rebote) :'))

print(rebote(input_rebote))

"""

un medicamento se elimina del organismo a traves de la orinas.
La dosisi inicial es de 10mg y la cantidad en el cuerpo t horas

10 = cantidad de mg

f(x) ->  A(t) = 10*(0.8)**t

"""

tiempo = [3,4,5,6,7]

def decreMedicamento(t):
    resultados = []
    for i in range(len(t)):
        result = 10*(0.8)**t[i]
        resultados.append(result)
    return resultados

#input_tiempo = int(input('Para consulta la cantidad de mg por tiempo transcurrido ingrese la hora :) : '))

#print(decreMedicamento(input_tiempo))
print(decreMedicamento(tiempo))


"""
si 10 gramos de sal se añaden a una cantidad de agua, la cantidad K(t)
de sal que no se disuelve despues de t minutos esta dada por

-> K(t) = 10 * (4/5)**t

preguntas
1) cual es la cantidad de sal sin disolver en agua 3 minutos despues
2) despues de añadir la sal al agua ¿cuando quedan solo 5g sin disolver?

programe su respuesta ! :)

"""


