import json

def put_product_to_cart(data):
    pass


def get_cart(data):
   with open('data_sample/cart.json', encoding='utf-8') as read_file:
       read_cart = json.load(read_file)
       count = 0
       for i in read_cart:
           count += 1
           print(f'{count}. {i['name']} ')


get_cart(6)
