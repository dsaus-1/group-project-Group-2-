from hanlders.products import get_product_list
from main import main

data = {"action": 2,
        "filter": {
            "price": '<1000',
            "category": None
        }
        }


def test_get_product_list():


    assert get_product_list(data) == {'code': 200, 'data': '1. Груши. Сильвер. (500 руб/кг) 3 шт.\n2. сливы. (50 руб/кг) 4 шт.\n3. картошка (300 руб/кг) 5 шт.\n4. горох (780 руб/кг) 8 шт.\n5. баклажан (150 руб/кг) 17 шт.\n'}
   # assert result.get('category') == expected_result.get('category')