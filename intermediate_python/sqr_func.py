
def run():
    if opcion == 1:
        enum_exahustiva(objetivo)
    elif opcion == 2:
        algoritmo_aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print('Opcion equivocada, elige de nuevo')


def enum_exahustiva (objetivo):

    #objetivo = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene uan raiz cuadrada exacta') 


def algoritmo_aproximacion(objetivo):
    
    #objetivo = int(input('Escoge un entero: '))
    epsilon = 0.01
    paso = epsilon ** 2
    respuesta = 0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2-objetivo),respuesta)
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
    else:
        print(f'La raiz cuadrado de {objetivo} es {respuesta}')


def busqueda_binaria(objetivo):

    #objetivo = int(input('Escoge un numero: '))
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrado de {objetivo} es {respuesta}')


if __name__=='__main__':
    opcion = int(input('''MENU:
        1. Enumeracion exhaustiva
        2. Algoritmo de aproximacion
        3. Busqueda binaria
        
        Elije una opcion: '''))
    
    objetivo = int(input('Introduce un numero: '))
    
    run()
