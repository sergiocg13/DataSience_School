def es_primo(numero):
    contador = 0
    for i in range(1,numero+1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    if es_primo(numero):
        print(f'{numero} es numero primo')
    else:
        print(f'{numero} no es un numero primo')


if __name__ == '__main__':
    numero = int(input('Escribe un numero: '))
    run()
    