import pytest
from Class_Product import Product


@pytest.fixture
def eeployee_product():
    prod = {'name': 'Samsung Galaxy C23 Ultra',
            'description': '256GB, Серый цвет, 200MP камера',
            'price': 180000.0, 'quantity': 5}
    return Product(**prod)

def test_init_product(eeployee_product):
    assert eeployee_product.name == "Samsung Galaxy C23 Ultra"
    assert eeployee_product.description == "256GB, Серый цвет, 200MP камера"
    assert eeployee_product.price == 180000.0
    assert eeployee_product.quantity == 5

def test_get_product(eeployee_product):
    prod_1 = eeployee_product.get_product("Iphone 15", "256gb", 120000, 1)
    assert prod_1.name == "Iphone 15"
    assert prod_1.description == "256gb"
    assert prod_1.price == 120000
    assert prod_1.quantity == 1

def test_get_price(eeployee_product):
    assert eeployee_product.get_price == 180000.0

def test_get_price(eeployee_product):
    price = 0
    assert eeployee_product.get_price(0) == None