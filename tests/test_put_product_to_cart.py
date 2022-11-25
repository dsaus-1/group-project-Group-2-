from hanlders.cart import get_cart, put_product_to_cart


def test_put_product_to_cart():
    assert put_product_to_cart({
        "action": 5,
        "data": {
            "id": 1,
            "count": 5
        }
    }) == f"'code': 201,\n'message': Товар Яблоки. Голден. в количестве 5 штук добавлен в корзину успешно"
    assert put_product_to_cart({
        "action": 5,
        "data": {
            "id": 7,
            "count": 5
        }
    }) == f"'code': 404,\n'message': Товара с таким номер не найдено."
    assert put_product_to_cart({
        "action": 5,
        "data": {
            "id": 1,
            "count": 11
        }
    }) == f"'code': 409,\n'message': Невозможно добавить товар Яблоки. Голден. в количестве 11 штук в корзину, потому что их осталось всего 10."
