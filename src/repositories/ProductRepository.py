from uuid import uuid4
from datetime import datetime
from dtos.ProductDto import ProductCreate

class ProductRepository():
    __products = []

    @staticmethod
    def create(data: ProductCreate):
        ProductRepository.__products.append(
            {
                'id': uuid4(),
                'name': data.name,
                'qtd': data.qtd,
                'price': data.price,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
            }
        )

    @staticmethod
    def read():
        return ProductRepository.__products

    @staticmethod
    def read_by_id(id):
        for product in ProductRepository.__products:
            if product['id'] == id:
                return product

    @staticmethod
    def update(id, data: ProductCreate):
        for key, product in enumerate(ProductRepository.__products):
            if product['id'] == id:
                ProductRepository.__products[key] = {
                    'id': id,
                    'name': data.name,
                    'qtd': data.qtd,
                    'price': data.price,
                    'updated_at': datetime.utcnow(),
                }
                return True

    @staticmethod
    def delete(id):
        for key, product in enumerate(ProductRepository.__products):
            if product['id'] == id:
                del ProductRepository.__products[key]
                return True