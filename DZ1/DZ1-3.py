data = ['attribute', 'класс', 'функция', 'type']

for el in data:
    try:
        bytes(el, 'ascii')
    except UnicodeEncodeError:
        print(f'слово {el} не представить в байтовом типе')
