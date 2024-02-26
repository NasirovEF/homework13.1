import json
from class_category import Category
from class_product import Product


def read_file(filee_json):
    """Читает файл json, возвращает список"""

    with open(filee_json, encoding="utf8") as file:
        list_products = json.load(file)

    return list_products


def add_category(list_products):
    """Из полученного списка создает экземпляр класса Category"""

    for category in list_products:
        cls_category = Category(**category)
        return cls_category


def add_product(list_products):
    """Из полученного списка создает экземпляр класса Product"""

    for products in list_products:
        for product in products.get("products"):
            cls_product = Product(**product)
            return cls_product
