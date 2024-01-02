from infra.db.session import Base, engine

async def create_db():
    async with engine.begin() as conn:
        from entities.Product import Product
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
