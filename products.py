import json

file = '../data/catalog.json'

data = {"action": 2,
        "filter": {
            "price": '<1000',
            "category": None
        }
        }


def get_product_list(data):
    with open(file, encoding='utf-8') as catalog_data:
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

    with open("../data/amsple.json", "w") as outfile:
        json.dump(d, outfile)
    return d


print(get_product_list(data))
