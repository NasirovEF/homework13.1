import json
from Class_Category import Category
from Class_Product import Product


def read_file(file_json):
    """Читает файл json, возвращает список"""

    with open(file_json, encoding="utf8") as file:
        list_products = json.load(file)

    return list_products


def add_category(list_products):
    """Из полученного списка создает экземпляр класса Category"""

    for category in list_products:
        cls_category = Category(**category)
        print(cls_category)

file_json = "products.json"

add_category(read_file(file_json))
