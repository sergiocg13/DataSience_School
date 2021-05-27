def run():

# imprimir los numeros de 1 al 100 y guardarlos en una lista: squares, solo si no son divisibles entre 3 
    # squares = []
    # for i in range(1, 101):
    #     #solo guardara los numeros que no son divisibles entre 3
    #     if i % 3 != 0:
    #         squares.append(i**2)
    #print(squares)

# impresion de lista 1 al 100 con "list comprehension"
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

# list comprehension, multiplos de 4,6 y 9, hasta 5 digitos (99,999)
    list = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(list)


if __name__ == '__main__':
    run()