data = ['разработка', 'администрирование', 'protocol', 'standard']
b_data = []
data_out = []

for el in data:
    b_data.append(el.encode('utf-8'))

for el in b_data:
    data_out.append(el.decode('utf-8'))

if data == data_out:
    print('преобразование в байты и обратно прошло успешно')