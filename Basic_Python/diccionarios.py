def run():
    diccionario = {
        'llave1':1,
        'llave2':2,
        'llave3':3
    }
    print(diccionario)

    for keys in diccionario.keys():
        print(keys)

    for llaves in diccionario.values():
        print(llaves)
    
    for llaves,numero in diccionario.items():
        print(llaves,numero)


if __name__ == '__main__':
    run()   