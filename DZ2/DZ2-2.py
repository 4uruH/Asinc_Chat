import os
import json

if not os.path.isfile('orders.json'):
    with open('orders.json', 'w', encoding='utf-8') as f:
        data = {'orders': []}
        json.dump(data, f)


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='utf-8') as data_file:
        file_data = json.load(data_file)
    with open('orders.json', 'w', encoding='utf-8', ) as file:
        orders = file_data['orders']
        input_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders.append(input_info)
        json.dump(file_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':

    write_order_to_json('вертолет', '1000', '1452345135', 'weapon_baron', '01.03.2023')
    write_order_to_json('танк', '101230', '45135', 'somali_piraten', '01.03.2023')
