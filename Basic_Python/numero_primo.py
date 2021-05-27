def es_primo(numero):
   if numero > 0:
       factorial = 1
       for i in range(1,numero):
            factorial *= 1
            if (factorial + 1) % numero == 0 and numero != 1:
                return True
            else:
                return False
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
    