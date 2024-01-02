from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_async_engine(
    url = 'sqlite+aiosqlite:///src/infra/db/store.db',
    echo = True
)

Base = declarative_base()