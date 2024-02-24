class Category:
    """Класс категории товаров"""

    total_category = 0
    unique_product = []

    def __init__(self, name, description, products):  # Задание 2
        self.name = name
        self.description = description
        self._products = products

        Category.total_category += 1
        #Category.unique_product += len(set(list(self.get_uniq_prod().get("name"))))
        Category.unique_product.append(set(list(self.get_uniq_prod().get("name"))))

    def get_uniq_prod(self):
        for product in self._products:
            return product

    def get_product(self, product):
        return self._products.append(product)

    @property
    def get_list(self):
        for product in self._products:
            return f'{product.get("name")}, {product.get("price")} руб. Остаток: {product.get("quantity")} шт.'

    def __str__(self):
        return f"{self.name}, {self.description}, {Category.total_category}, {Category.unique_product}"
