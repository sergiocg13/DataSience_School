# Manejo de excepciones con assert

def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")

    # Colocamos palabra clave assert, y en este caso utilizamos un metodo
    # especial de los string "isnumeric" el cual devuelve True si el string
    # ingresado por el usuario es numerico, y False si no es un numero 
    # (en este ultimo caso, el assert devolvera el texto de error)
    assert num.isnumeric() and int(num) > 0, "Solo puedes ingresar numeros positivos"
    print(divisors(int(num)))
    print("Termino mi programa")

if __name__ == '__main__':
    run()