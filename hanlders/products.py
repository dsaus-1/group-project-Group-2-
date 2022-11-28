import json


def get_product_list(data):
    pass


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
