from _includes import *

from dtos.ProductDto import ProductCreate


class TestRoutes(TestCase):
    def test_root(self):
        response = client.get('/')
        assert response.status_code == 200
        assert response.json() == {'msg': 'Hello, World'}


class TestProductsRoutes(TestCase):

    def test_get_products(self):
        response = client.get('/products')
        assert response.status_code == 200

    # def test_post_product(self):
    #     data = ProductCreate(name='Test Product', price=99.99, qtd=12)
    #     response = client.post('/products', json=data.model_dump())
    #     assert response.status_code == 201
    #     assert response.json() == {'msg': 'Produto cadastrado com sucesso'}
