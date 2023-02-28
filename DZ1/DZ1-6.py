from chardet import detect

data = ['сетевое программирование', 'сокет', 'декоратор']

with open('file.txt', 'w', encoding='utf-8') as f:
    for el in data:
        f.write(f'{el}\n')

with open('file.txt', 'rb') as f:
    out = f.read()
print(detect(out)['encoding'])

with open('file.txt', 'r', encoding='utf-8') as f:
    out = f.read()
print(out)

"""
если не задать принудительно кодеровку файл создается в кодеровке windows-1251 и при попытке прочитать в utf-8 
падает с ошибкой

"""