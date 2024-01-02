from datetime import datetime
from sqlalchemy import String, DateTime, Float, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import UUIDType
from infra.db.session import Base

class Product(Base):
    __tablename__ = 'products'
    __allow_unmapped__ = True

    id: Mapped[str] = mapped_column(UUIDType, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    qtd: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<Product {self.name} at {self.created_at}>'