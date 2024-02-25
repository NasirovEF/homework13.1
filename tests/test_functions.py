import pytest
import json
from functions import *


def test_read_file():
    file = "for_test.json"
    assert read_file(file) == [{"name": "Смартфоны",
                                           "description": "Смартфоны, как средство не только коммуникации, "
                                                          "но и получение дополнительных функций для удобства жизни",
                                           "products": [{"name": "Samsung Galaxy C23 Ultra",
                                                         "description": "256GB, Серый цвет, 200MP камера",
                                                         "price": 180000.0,
                                                         "quantity": 5}]}]

