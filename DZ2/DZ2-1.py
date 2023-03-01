import re
import csv
import os


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    for file in os.listdir("C:/Users/fanto/Asinc_Chat/DZ2"):

        if file.endswith(".txt"):
            row = []
            with open(file, 'r') as f:
                data = f.read()
                os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
                os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
                row.append(os_prod_reg.findall(data)[0].split()[2])

                os_name_reg = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\d*')
                os_name_list.append(os_name_reg.findall(data)[0])
                row.append(os_name_reg.findall(data)[0].split()[2] + " " + os_name_reg.findall(data)[0].split()[3] + " "
                           + os_name_reg.findall(data)[0].split()[4])

                os_code_reg = re.compile(r'Код продукта:\s*\S*')
                os_code_list.append(os_code_reg.findall(data)[0].split()[2])
                row.append(os_code_reg.findall(data)[0].split()[2])

                os_type_reg = re.compile(r'Тип системы:\s*\S*')
                os_type_list.append(os_type_reg.findall(data)[0].split()[2])
                row.append(os_type_reg.findall(data)[0].split()[2])

                main_data.append(row)
    return main_data


def write_to_csv(file_name):

    main_data = get_data()
    with open(file_name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        for row in main_data:
            writer.writerow(row)


if __name__ == '__main__':
    write_to_csv('some_file.csv')
