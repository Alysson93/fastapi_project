from uuid import uuid4
from datetime import datetime
from dtos.ProductDto import ProductCreate

class ProductRepository():
    products = []
    
    @staticmethod
    def create(data: ProductCreate):
        ProductRepository.products.append(
            {
                'id': uuid4(),
                'name': data.name,
                'price': data.price,
                'qtd': data.qtd,
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow()
            }
        )

    @staticmethod
    def read():
        return ProductRepository.products

    @staticmethod
    def read_by_id(id):
       for i in ProductRepository.products:
           if i['id'] == id:
               return i


    @staticmethod
    def update(id, data: ProductCreate):
        for i, v in enumerate(ProductRepository.products):
            if v['id'] == id:
                ProductRepository.products[i] = {
                    'id': id,
                    'name': data.name,
                    'price': data.price,
                    'qtd': data.qtd,
                    'created_at': v['created_at'],
                    'updated_at': datetime.utcnow()
                }
                return True

    @staticmethod
    def delete(id):
        for i, v in enumerate(ProductRepository.products):
            if v['id'] == id:
                del ProductRepository.products[i]
                return True