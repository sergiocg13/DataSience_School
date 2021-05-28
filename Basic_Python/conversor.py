

#Funcion de conversion
def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantas pesos ' + tipo_pesos + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')


menu = """
Bienvenido al conversor de monedas 💰💰💰💰

1 - Pess colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: 

"""
opcion = int(input(menu))

if opcion == 1:
    conversor('colombianos',3692.09600)
   
elif opcion == 2:
    conversor('argentinos',91.64689)
    
elif opcion == 3:
    conversor('mexicanos',20.61775)

else:
    print('Opcion seleccionada incorrecta')