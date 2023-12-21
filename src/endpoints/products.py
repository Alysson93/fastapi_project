from uuid import UUID
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix='/products', tags=['products'])

from repositories.ProductRepository import ProductRepository
from dtos.ProductDto import ProductCreate


@router.get('/')
def read():
    return ProductRepository.read()


@router.get('/{id}')
def read_by_id(id: UUID):
    product = ProductRepository.read_by_id(id)
    if product is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return product


@router.post('/', status_code=201)
def create(data: ProductCreate):
    ProductRepository.create(data)
    return {'msg': 'Produto cadastrado com sucesso'}


@router.put('/{id}', status_code=204)
def update(id: UUID, data: ProductCreate):
    product = ProductRepository.update(id, data)
    if product is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')


@router.delete('/{id}', status_code=204)
def delete(id: UUID):
    product = ProductRepository.delete(id)
    if product is None:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
