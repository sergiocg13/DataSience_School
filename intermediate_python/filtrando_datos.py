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

#filtros con list_comprehensios y las funciones filter, map y reduce
    # Listamos  a las personas mayores de 18 años
    # Imprime los datos completos de todas las personas en el diccionario
    adults = list(filter(lambda person: person ['age'] > 18, DATA))
    # Sobre escribimos la variable adults, para listar unicamente los nombres
    # del diccionario mayores de 18 años
    adults = list(map(lambda person: person['name'], adults))
    old = list(reduce(lambda person))

    for person in adults:
        print(person)

if __name__=='__main__':
    run()