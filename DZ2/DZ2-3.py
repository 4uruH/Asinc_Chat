import yaml

data = {'list': ['some letters', 'some numbers', 2],
        'number': 5,
        'dict': {'omega': '1\u03A9',
                 'sigma': '2\u03C3',
                 'delta': '3\u0394'}
        }

with open('dz2_3.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open('dz2_3.yaml', 'r', encoding='utf-8') as f:
    read_data = yaml.load(f, Loader=yaml.SafeLoader)

if data == read_data:
    print('все четко!')

