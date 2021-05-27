def run():
    my_list = [1,"Hello",True, 4.5]
    my_dict ={"firstname": "Sergio", "lastname": "García"}

    super_list =[
                        {"firstname": "Mateo", "lastname": "Robles"},
                        {"firstname": "Leonardo", "lastname": "Gonzalez"},
                        {"firstname": "Alicia", "lastname": "García"},
                        {"firstname": "Fernando", "lastname": "Martinez"},
                        {"firstname": "Miguel", "lastname": "Torres"},
                        {"firstname": "Susana", "lastname": "Casas"},
                        {"firstname": "Cameron", "lastname": "Holt"},
                        {"firstname": "Alejandra", "lastname": "Yera"},
                        {"firstname": "Lucia", "lastname": "Carrillo"},
                        {"firstname": "Elizabeth", "lastname": "Flores"},
                        {"firstname": "Maria", "lastname": "Arriaga"},
                        {"firstname": "Tania", "lastname": "Castro"},
                        {"firstname": "Sergio", "lastname": "Cermeño"}
    ]

    super_dict={
                        "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8],
                        "interger_nums":[-1,-2,0,1,2,3],
                        "floating_nums":[1.1, 4.5, 6.43, 13.4]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

    for i in super_list:
           print(i)

    #otra forma de imprimir la lista
    #for values in super_list:
    #    for key, value in values.items():
    #        print(f'{key} - {values}')    


if __name__ == '__main__':
    run()