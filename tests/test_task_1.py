import pytest

from task_1 import *


@pytest.fixture
def eeployee_category():
    return Category("телефоны", "мобильные смартфоны с сенсорным экраном", ["Iphone 15ProMax", "Samsung", "Iphone", "Iphone"])


@pytest.fixture
def eeployee_product():
    return Product("Iphone 15ProMax", "лучший телефон", 120000, 10)


def test_init_category(eeployee_category):
    assert eeployee_category.name == "телефоны"
    assert eeployee_category.description == "мобильные смартфоны с сенсорным экраном"
    assert eeployee_category._products == ["Iphone 15ProMax", "Samsung", "Iphone", "Iphone"]
    assert eeployee_category.total_category == 1
    assert eeployee_category.unique_product == 3

def test_get_product(eeployee_category):
    assert eeployee_category.get_product("Xiaomi") == None



def test_init_product(eeployee_product):
    assert eeployee_product.name == "Iphone 15ProMax"
    assert eeployee_product.description == "лучший телефон"
    assert eeployee_product.price == 120000
    assert eeployee_product.quantity == 10

def test_get_product(eeployee_product):
    assert eeployee_product.get_product("Xiaomi", "Китай", 100000, 10) == ["Xiaomi", "Китай", 100000, 10]
