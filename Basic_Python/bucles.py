def run():
    contador = 0
    resultado = 2**contador
    while contador <= 10:
        print(f'2 elevado a {contador} es igual a: {resultado}')
        contador = contador + 1
        resultado = 2**contador

if __name__ == '__main__':
    run()