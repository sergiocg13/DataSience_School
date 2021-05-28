#High order functions o funciones de orden superior, son aquellas en las que
#una funcion recibe como parametro otra funcion.

#Ejemplo:
#La funcion saludo (high order function) hace un llamado a las funciones de
# hola o adios: 
def saludo(func):
     func()

def hola():
    print("Hola!!")

def adios():
    print("Adios!!")

saludo(hola)
saludo(adios)

# Las tres funciones de order superior clasicas filter, map, reduce

# filter devuelve True or False según el valor esté dentro de los criterios 
# buscados o no. En caso de que no cumpla con la condición, no será devuelto
# y la lista se verá reducida por este filtro.

#ejemplo:
# filtar los numero impares de una lista, en una nueva lista llamada odd:
my_list=[1, 4, 5, 6, 9, 13, 19, 21]
odd=[i for i in my_list if i % 2 != 0]
print(odd)
    
#Solucion con "filter", la funcion "list" simpre debe envolver a la funcion "filter"
list_filter = list(filter(lambda x:x%2 != 0, my_list))
print(list_filter)


# Map funciona muy parecido, pero su diferencia radica en que no puede eliminar
# valores de la lista del array entregado. Es decir, el output tiene la misma
# cantidad de valores que el input.

#ejemplo
#Convertir los numero de una lista en una lista elevado al cuadrado

my_list2 = [1,2,3,4,5]
squares = [i**2 for i in my_list2]
print(squares)

# Solucion con map
squares = list(map(lambda x: x**2, my_list2))
print(squares)


# Reduce toma 2 valores entregados como parámetros y el iterador como otro 
# parámetro. Realiza la función con estos 2 valores, y luego con el resultado
# de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

# multiplicar todos los elementos de una lista(resultado debe ser 32):
my_list3 = [2,2,2,2,2]
all_multiplied = 1

for i in my_list3:
    all_multiplied = all_multiplied * i
    print(all_multiplied) #imprime los resultados en cada vuelta del ciclo (2,4,8,16,32)

# Solucion con reduce:
#importamos functools
from functools import reduce

multiplied = reduce(lambda a,b : a * b, my_list3)
print(multiplied) #imprime directamente el resultado total


