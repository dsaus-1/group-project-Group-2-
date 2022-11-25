import json

def put_product_to_cart(data):
    with open('data/catalog.json', encoding='utf-8') as json_file:
        catalog_list = json.load(json_file)
        cart_list = []
        for i in catalog_list:
            for elem in i['products']:
                if data["data"]["id"] == elem['id']:
                    cart_list.append({'name': elem['name'], 'id': elem['id'], 'count': count_input})
                    print(f"'code': 201\n 'message': Товар {cart_list['name']} в количестве {cart_list['count']} штук добавлен в корзину успешно")
                if data["data"]["id"] != elem['id']:
                    print("'code': 404,\n 'message': Товара с таким номером не найдено.")
                if data["data"]["count"] > elem["balance"]:
                    print(f"Невозможно добавить товар {cart_list['name']} в количестве {count_input} штук в корзину, потому что их осталось всего {elem['balance']}.")

    with open('data/cart.json', 'w') as f:
        json.dump(cart_list, f)


def get_cart(data):
   with open('data/cart.json', encoding='utf-8') as read_file:
       read_cart = json.load(read_file)
       count = 0
       for i in read_cart:
           count += 1
           print(f'{count}. {i['name']} ')


get_cart(6)
