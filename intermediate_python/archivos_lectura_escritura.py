def read():
    numbers = []
    with open ('C:\\Users\\SergioCG\\DataScience_Platzi\\DataSience_School\\intermediate_python\\archivos\\numbers.txt','r', encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Facundo','Miguel', 'Mateo', 'Leonardo', 'Cristian', 'Rocío']
    with open ('C:\\Users\\SergioCG\\DataScience_Platzi\\DataSience_School\\intermediate_python\\archivos\\names.txt','a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def run():
    write()


if __name__ == '__main__':
    run()