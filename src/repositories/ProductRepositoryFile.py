from uuid import uuid4
from datetime import datetime
from dtos.ProductDto import ProductCreate

class ProductRepository():
    __file = 'src/infra/files/products.txt'
    
    @staticmethod
    def create(data: ProductCreate):
        with open(ProductRepository.__file, 'a') as file:
            file.write(
                f'{uuid4()} | {data.name} | {data.qtd} | {data.price} | {datetime.utcnow()} | {datetime.utcnow()} \n'
            )

    @staticmethod
    def read():
        with open(ProductRepository.__file, 'r') as file:
            products = []
            for line in file.readlines():
                line = line[:-2]
                line = line.split(' | ')
                products.append({
                    'id': line[0],
                    'name': line[1],
                    'qtd': int(line[2]),
                    'price': float(line[3]),
                    'created_at': line[4],
                    'updated_at': line[5]
                })
            return products

    @staticmethod
    def read_by_id(id):
        with open(ProductRepository.__file, 'r') as file:
            for line in file.readlines():
                line = line[:-2]
                line = line.split(' | ')
                if line[0] == str(id):
                    return {
                        'id': line[0],
                        'name': line[1],
                        'qtd': int(line[2]),
                        'price': float(line[3]),
                        'created_at': line[4],
                        'updated_at': line[5]  
                    }


    @staticmethod
    def update(id, data: ProductCreate):
        product = ProductRepository.read_by_id(id)
        if product == None:
            return
        with open(ProductRepository.__file, 'a') as file:
            file.write(
                f'{id} | {data.name} | {data.qtd} | {data.price} | {product['created_at']} | {datetime.utcnow()} \n'
            )
        ProductRepository.delete(id)
        return True

    @staticmethod
    def delete(id):
        cont = 0
        product = ProductRepository.read_by_id(id)
        if product == None:
            return
        products = ProductRepository.read()
        with open(ProductRepository.__file, "w") as file:
            for i in products:
                if str(id) == i['id'] and cont < 1:
                    cont += 1
                    continue
                file.write(
                    f'{i['id']} | {i['name']} | {i['qtd']} | {i['price']} | {i['created_at']} | {i['updated_at']} \n'
                )
            return True