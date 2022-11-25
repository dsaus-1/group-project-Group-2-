import json

def put_product_to_cart(data):
    with open('data/catalog.json', encoding='utf-8') as json_file:
        catalog_list = json.load(json_file)
        cart_list = {}
        cart_list['cart'] = []
        code = 404
        message = "Товара с таким номер не найдено."
        for i in catalog_list:
            for elem in i['products']:
                if data["data"]["id"] == elem['id'] and data["data"]["count"] > elem["balance"]:
                    code = 409
                    message = f"Невозможно добавить товар {elem['name']} в количестве {data['data']['count']} штук в корзину, потому что их осталось всего {elem['balance']}."
                    return f"'code': {code},\n'message': {message}"
                if data["data"]["id"] == elem['id']:
                    code = 201
                    message = f"Товар {elem['name']} в количестве {data['data']['count']} штук добавлен в корзину успешно"
                    cart_list['cart'].append({'name': elem['name'], 'id': elem['id'], 'count': data["data"]["count"]})
                    return f"'code': {code},\n'message': {message}"

    return f"'code': {code},\n'message': {message}"
    with open('data/cart.json', 'w') as f:
        json.dump(cart_list, f)


def get_cart(data):
   with open('data/cart.json', encoding='utf-8') as read_file:
       read_cart = json.load(read_file)
       count = 0
       for i in read_cart:
           count += 1
           print(f"{count}. {i['name']}")