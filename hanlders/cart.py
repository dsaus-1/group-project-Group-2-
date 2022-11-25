import json

def put_product_to_cart(data):
    with open('data_sample/catalog.json', encoding='utf-8') as json_file:
        dict = json.load(json_file)
    data = {}
    data['filter'] = []
    if id_input == dict['products']['id']:
        data['filter'].append({'name': dict["products"]["name"], 'id': dict["products"]["id"], 'count': count_input})
        dict["products"]["balance"] = dict["products"]["balance"] - data['count']
        print(f"'code': 201\n 'message': Товар {data['name']} в количестве {data['count']} штук добавлен в корзину успешно")
    if id_input != dict['products']['id']:
        print("'code': 404,\n 'message': Товара с таким номером не найдено.")
    if count_input > dict["products"]["balance"]:
        print(f"Невозможно добавить товар {data['name']} в количестве {count_input} штук в корзину, потому что их осталось всего {dict['products']['balance']}.")

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
