from hanlders.products import get_single_product


def test_func_get_single_product():
    assert get_single_product(
        {
            "action": 4,
            "data": {
                "id": 5
            }
        }
    ) == {'code': 200, 'message': "Конфеты 'Cтеп'\nЦена: 3000 за кг\nОстаток на складе: 50 кг\nОписание: Поможет не грустить, если проект тяжело идёт"}
    assert get_single_product(
        {
            "action": 4,
            "data": {
                "id": 7
            }
        }
    ) == {'code': 404, 'message': 'Товара с таким номер не найдено'}
