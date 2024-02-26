import pytest
from src.class_category import Category


@pytest.fixture
def eeployee_category():
    dict_cat = {'name': 'Смартфоны',
                'description': 'Смартфоны, как средство не только коммуникации, '
                               'но и получение дополнительных функций для удобства жизни',
                'products': [{'name': 'Samsung Galaxy C23 Ultra',
                              'description': '256GB, Серый цвет, 200MP камера',
                              'price': 180000.0, 'quantity': 5}]}
    return Category(**dict_cat)


def test_init_category(eeployee_category):
    assert eeployee_category.name == "Смартфоны"
    assert eeployee_category.description == ("Смартфоны, как средство не только коммуникации, "
                                             "но и получение дополнительных функций для удобства жизни")
    assert eeployee_category.get_product == [{'name': 'Samsung Galaxy C23 Ultra',
                                            'description': '256GB, Серый цвет, 200MP камера',
                                            'price': 180000.0, 'quantity': 5}]
    assert eeployee_category.total_category == 1
    #assert eeployee_category.unique_product == 1


def test_get_product(eeployee_category):
    assert eeployee_category.get_product({"name": "Гранта"}) == [
        {'name': 'Samsung Galaxy C23 Ultra', 'description': '256GB, Серый цвет, 200MP камера', 'price': 180000.0,
         'quantity': 5}, {"name": "Гранта"}]

def test_get_list(eeployee_category):
    assert eeployee_category.get_list == "\nSamsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."