import json
import os


def get_product_list(data):

    path_catalog = os.path.join(os.path.dirname(__file__), 'data/catalog.json')

    with open(path_catalog, encoding='utf-8') as catalog_data:
        products_ = json.load(catalog_data)

    price = data['filter']['price']
    category = data['filter']['category']
    price_prod = []
    price_kg = []
    coll = []
    product = products_[0]["products"]
    count = 0
    for i in products_:

        if category == i['name']:
            count += 1
            if count == 0:
                return []

    if price == None and category == None:

        for i in products_:
            for j in range(len(i['products'])):
                price_prod.append(i["products"][j]["name"])
                price_kg.append(i["products"][j]["price"])
                coll.append(i["products"][j]["balance"])
    elif price != None and category == None:
        for k in products_:
            for i in k['products']:
                list_price = (" ".join(price)).split()
                price_ = i['price']
                if ">" in list_price and "=" in list_price:
                    list_price.remove('>')
                    list_price.remove('=')
                    l_p = ''.join(list_price)
                    if price_ >= int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif "<" in list_price and "=" in list_price:
                    list_price.remove('<')
                    list_price.remove('=')
                    l_p = ''.join(list_price)
                    if price_ <= int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif ">" in list_price:
                    list_price.remove('>')
                    l_p = ''.join(list_price)
                    if price_ > int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])
                elif "<" in list_price:
                    list_price.remove('<')
                    l_p = ''.join(list_price)
                    if price_ < int(l_p):
                        price_prod.append(i['name'])
                        price_kg.append(i['price'])
                        coll.append(i['balance'])

    elif price == None and category != None:

        for i in products_:
            if category in i["name"]:
                for j in range(len(i['products'])):
                    price_prod.append(i["products"][j]["name"])
                    price_kg.append(i["products"][j]["price"])
                    coll.append(i["products"][j]["balance"])
    else:

        for i in products_:
            if category in i["name"]:

                for j in i['products']:
                    list_price = (" ".join(price)).split()
                    price_ = j['price']
                    if ">" in list_price and "=" in list_price:
                        list_price.remove('>')
                        list_price.remove('=')
                        l_p = ''.join(list_price)
                        if price_ >= int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif "<" in list_price and "=" in list_price:
                        list_price.remove('<')
                        list_price.remove('=')
                        l_p = ''.join(list_price)
                        if price_ <= int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif ">" in list_price:
                        list_price.remove('>')
                        l_p = ''.join(list_price)
                        if price_ > int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
                    elif "<" in list_price:
                        list_price.remove('<')
                        l_p = ''.join(list_price)
                        if price_ < int(l_p):
                            price_prod.append(j['name'])
                            price_kg.append(j['price'])
                            coll.append(j['balance'])
    d = {'code': 200}
    json_format = []
    for i in range(len(price_prod)):
        json_format.append(f"{i + 1}. {price_prod[i]} ({price_kg[i]} руб/кг) {coll[i]} шт.\n")
    d['data'] = ''.join(json_format)
    return d






def get_single_product(data):
    request_user_id = data["data"]["id"]  # итоговый айдишник, который запрашиавает пользователь
    with open('data/catalog.json', encoding='utf-8') as json_file:
        catalog_list = json.load(json_file)
    for i in catalog_list:
        for j in i['products']:
            if request_user_id in j.values():
                write = f'''{j["name"]}\nЦена: {j["price"]} за кг\nОстаток на складе: {j["balance"]} {j["unit"]}\nОписание: {j["description"]}'''
                return {
                    "code": 200,
                    "message": write
                }
    else:
        return {
                    "code": 404,
                    "message": "Товара с таким номер не найдено"
                }
