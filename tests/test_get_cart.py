from hanlders.cart import get_cart, put_product_to_cart

def test_put_product_to_cart():
    assert put_product_to_cart({
    "action": 5,
    "data": {
      "id": 1,
      "count": 5
    }
}) == {
    "code": 201,
    "message": "Товар 'Яблоки' в количестве 5 штук добавлен в корзину успешно"
}
    assert put_product_to_cart({
    "action": 5,
    "data": {
      "id": 7,
      "count": 5
    }
}) == {
    "code": 404,
    "message": "Товара с таким номер не найдено."
}
    assert put_product_to_cart({
    "action": 5,
    "data": {
      "id": 1,
      "count": 12
    }
}) == {
    "code": 409,
    "message": "Невозможно добавить товар 'Яблоки' в количестве 11 штук в корзину, потому что их осталось всего 10."
}

test_put_product_to_cart()
# assert get_cart() ==