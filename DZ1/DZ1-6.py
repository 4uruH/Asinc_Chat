from chardet import detect

data = ['сетевое программирование', 'сокет', 'декоратор']

with open('file.txt', 'w') as f:
    for el in data:
        f.write(f'{el}\n')

with open('file.txt', 'rb') as f:
    out = f.read()
    enc = detect(out)['encoding']
    print(f'кодировка файла: {enc}')
    if enc.lower() != 'utf-8':
        out = out.decode(enc)
        out = out.encode('utf-8')
        with open('file.txt', 'wb') as file:
            file.write(out)

with open('file.txt', 'r', encoding='utf-8') as f:
    out = f.read()
print(out)
