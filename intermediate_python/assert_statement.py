def palindromo(palabra):
    #assert len(palabra) > 0, 'No se puede ingresar una cadena vacia'
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
    #Impide que el usuario no ingrese una cadena de texto
    assert len(palabra) > 0, 'No se puede ingresar una cadena vacia'
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


#Punto de entrada de un programa de python
if __name__ == '__main__':
    run()
