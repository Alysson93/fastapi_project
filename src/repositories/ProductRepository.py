from datetime import datetime
from uuid import uuid4
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import async_sessionmaker
from dtos.ProductDto import ProductCreate
from entities.Product import Product
from infra.db.session import engine

class ProductRepository():
    session = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )
    
    @staticmethod
    async def create(data: ProductCreate):
        async with ProductRepository.session() as session:
            product = Product(
                id=uuid4(),
                name=data.name,
                price=data.price,
                qtd=data.qtd
            )
            session.add(product)
            await session.commit()

    @staticmethod
    async def read():
        async with ProductRepository.session() as session:
            statement = select(Product).order_by(Product.id)
            result = await session.execute(statement)
            return result.scalars().all()

    @staticmethod
    async def read_by_id(id):
        async with ProductRepository.session() as session:
            statement = select(Product).filter(Product.id == id)
            result = await session.execute(statement)
            return result.scalar_one_or_none()


    @staticmethod
    async def update(id, data: ProductCreate):
        async with ProductRepository.session() as session:
            product = await ProductRepository.read_by_id(id)
            if product is None:
                return
            stmt = (
                 update(Product).
                 where(Product.id == id).
                 values(
                      name = data.name,
                      price = data.price,
                      qtd = data.qtd,
                      updated_at = datetime.utcnow()
                 )
            )
            await session.execute(stmt)
            await session.commit()  
            return True 

    @staticmethod
    async def delete(id):
        async with ProductRepository.session() as session:
            product = await ProductRepository.read_by_id(id)
            if product is None:
                return
            await session.delete(product)
            await session.commit()
            return True
