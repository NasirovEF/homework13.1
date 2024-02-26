import pytest
from src.class_product import Product


@pytest.fixture
def eeployee_product():
    prod = {'name': 'Samsung Galaxy C23 Ultra',
            'description': '256GB, Серый цвет, 200MP камера',
            'price': 180000.0, 'quantity': 5}
    return Product(**prod)


def test_init_product(eeployee_product):
    assert eeployee_product.name == "Samsung Galaxy C23 Ultra"
    assert eeployee_product.description == "256GB, Серый цвет, 200MP камера"
    assert eeployee_product.get_price == 180000.0
    assert eeployee_product.quantity == 5


def test_get_product(eeployee_product):
    prod_dict = {"name": "Iphone 15", "description": "256gb", "price": 120000, "quantity": 1}
    prod_1 = eeployee_product.get_product(**prod_dict)
    assert prod_1.name == "Iphone 15"
    assert prod_1.description == "256gb"
    assert prod_1.get_price == 120000
    assert prod_1.quantity == 1


def test_get_price(eeployee_product):
    assert eeployee_product.get_price == 180000.0


def test_get_price(eeployee_product):

    assert eeployee_product.get_price(0) == ""