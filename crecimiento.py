

"""

La catidad de bacterias que hay en un cultivo esta dada por la funcion

B(t)= 2*3**t

t = tiempo
B(t) = miles


"""


tiempo = [3,5,6,7,8]

#arreglo de tiempo
def bacterias(t):
    #cantidad esta en miles
    cantidad = []
    for i in range(len(t)):
        result = (2*(3)**t[i])
        cantidad.append(result)
    return cantidad

print(bacterias(tiempo))




"""

Preguntas

1) ¿Cual es el numero inicial de bacterias?


"""

#Ingresando tiempo

tiempo = int(input('Ingrese el tiempo en hora \n >'))

def input_bacterias(t):
    return(2*(3)**t)

result = input_bacterias(tiempo)

print(f'El resultado es : {result}.000')






