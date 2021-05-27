import math

def run():
#Crear diccionario en donde las llaves sean 1 al 100 y los valores sean
# llaves**3

    # my_dict = {}

    # for i in range(1, 101):
    #     if i%3==0:
    #         my_dict[i] = i**3

    # print(my_dict)

#Creado con dictionary_comprehensions, numero no divisibles entre 3
    #my_dict = {i: i**3 for i in range(1,101) if i % 3 !=0}

    #print(my_dict)


#Crear dictionary comprehension, cuyas llaves sean los primeros 1000 numeros
#y los valores las raices cuadradas de estos

    dict_square = {i:round(math.sqrt(i),2) for i in range(1,1001)}

    print(dict_square)


if __name__ == '__main__':
    run()