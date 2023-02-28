data = ['разработка', 'сокет', 'декоратор']
data_unicode = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

for i in range(len(data)):
    print(f"строковое содержание: {data[i]}, тип данных {type(data[i])} \nданные в юникод: {data_unicode[i]}, "
          f"тип данных {type(data_unicode[i])}\n\n")