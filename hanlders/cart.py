import json

def put_product_to_cart(data):
    with open('data_sample/catalog.json', encoding='utf-8') as json_file:
        catalog_list = json.load(json_file)
    data = {}
    data['filter'] = []
    for i in catalog_list:
        for elem in i['products']:
            if id_input == elem['id']:
                data['filter'].append({'name': elem['name'], 'id': elem['id'], 'count': count_input})
                print(f"'code': 201\n 'message': Товар {data['name']} в количестве {data['count']} штук добавлен в корзину успешно")
            if id_input != elem['id']:
                print("'code': 404,\n 'message': Товара с таким номером не найдено.")
            if count_input > elem["balance"]:
                print(f"Невозможно добавить товар {data['name']} в количестве {count_input} штук в корзину, потому что их осталось всего {elem['balance']}.")

    with open('data_sample/cart.json', 'w') as f:
        json.dump(data, f)


def get_cart(data):
   with open('data_sample/cart.json', encoding='utf-8') as read_file:
       read_cart = json.load(read_file)
       count = 0
       for i in read_cart:
           count += 1
           print(f'{count}. {i['name']} ')


get_cart(6)
