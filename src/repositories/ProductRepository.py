from uuid import uuid4
from datetime import datetime
from dtos.ProductDto import ProductCreate
from infra.db.dbconfig import get_db_connection

class ProductRepository():
    conn = get_db_connection()
    
    @staticmethod
    def create(data: ProductCreate):
        with ProductRepository.conn as connection:
            cursor = connection.cursor()
            cursor.execute('''
				INSERT INTO products(id, name, price, qtd)
				VALUES (?, ?, ?, ?);
			''', (str(uuid4()), data.name, data.price, data.qtd))
            connection.commit()
            return True

    @staticmethod
    def read():
        products = None
        with ProductRepository.conn as connection:
            cursor = connection.cursor()
            cursor.execute('''
				SELECT * FROM products;
			''')
            products = cursor.fetchall()
        return products

    @staticmethod
    def read_by_id(id):
        product = None
        with ProductRepository.conn as connection:
            cursor = connection.cursor()
            cursor.execute('''
                SELECT * FROM products WHERE id = ?
			''', (str(id), ))
            product = cursor.fetchone()
        return product


    @staticmethod
    def update(id, data: ProductCreate):
        with ProductRepository.conn as connection:
            product = ProductRepository.read_by_id(id)
            if product is None:
                return
            cursor = connection.cursor()
            cursor.execute("UPDATE products SET name=?, price=?, qtd=?, updated_at=? WHERE id=?",
                        (data.name, data.price, data.qtd, datetime.utcnow(), str(id)))
            connection.commit()
            return True

    @staticmethod
    def delete(id):
        with ProductRepository.conn as connection:
            product = ProductRepository.read_by_id(id)
            if product is None:
                return
            cursor = connection.cursor()
            cursor.execute("DELETE FROM products WHERE id=?", (str(id),))
            connection.commit()
            return True