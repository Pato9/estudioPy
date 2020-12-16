
"""
abs-> retorna el valor absoluto de un numero

-3 = 3
num = -3
in python -> abs(num)

"""

# ejemplo

input_num = int(input('Ingrese numero \n>'))

def absoluto(a):
    return abs(a)

#print(abs(input_num))
print(absoluto(input_num))


"""

any()->retornar un True(verdadero) si un elemento de un iterable es
verdadero.

any()-> toma un iterable(lista,tuple,string,diccionarios)


"""
print('=====any()======')
l = [1,2,3,4,0]
print(any(l))

l = [0,1]
print(any(l))

l = [True]
print(any(l))

l = [0,False]
print(any(l))

l = [-1,-3,-3]
print(any(l))

"""

all()-> esta funcion retorna veradero cuando todos los elementos del iterable son verdaderos, si no retorna falso

"""


print('======all()==========')
l = [1,2,3,4]
print(all(l))

l = [0,0,False]
print(all(l))

"""
ascii()-> si en string contiene una cadena de texto imprimible
de un objeto, espaca de los caracteres no ASCII es la cadena usando



sintaxis -> ascii(object)

"""


"""

bin()->El metodo bin convierte y retorna el string equivalente en binario de un entero. si el parametro no es un entero, se debe implementar __index__() method para retornar un entero

"""
print("======bin()=======")

num = 5
print(bin(num))

"""

bool()-> este metodo convierte un valor a boleano

sintaxis -> bool([valor])

"""

test = []
print(test,'is ',bool(test))
test = [0]
print(test,'is',bool(test))
test = 0
print(test,'is',bool(test))
test = 0.0
print(test,'is',bool(test))
test = None
print(test,'is',bool(test))

