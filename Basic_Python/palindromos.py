
def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


#Definir funcion principal llamada "run"
def run():
    palabra = input('Escribre una palaba: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


#Punto de entrada de un programa de python
if __name__ == '__main__':
    run()
