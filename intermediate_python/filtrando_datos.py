DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    # filtros con list comprehensions
    all_python_devs = [worker['name'] for worker in DATA if 
                    worker['language'] == 'python']

    all_platzi_workers = [worker['name'] for worker in DATA if
                    worker['organization'] == 'Platzi']

#Listado de desarrolladores de python
    for worker in all_python_devs:
        print(worker)

#Listado de trabajdores en platzi
    for worker in all_platzi_workers:
        print(worker)

#filtros con high order functions, con las funciones filter, map y reduce
    # Listamos  a las personas mayores de 18 años
    # Imprime los datos completos de todas las personas en el diccionario
    adults = list(filter(lambda person: person ['age'] > 18, DATA))
    # Sobre escribimos la variable adults, para listar unicamente los nombres
    # del diccionario mayores de 18 años
    adults = list(map(lambda person: person['name'], adults))
    #output con los nombres de las personas mayores de 18 años en DATA
    for person in adults:
        print(person)

    #agregar llave old dentro del diccionario DATA, si es mayor o menor a 70 años
    #usamos el simbolo | (pipe) para sumar la nueva llave old
    old_people= list(map(lambda person: person | {'old': person['age']>70}, DATA))
    #output con nueva llave old
    for person in old_people:
        print(person)

if __name__=='__main__':
    run()