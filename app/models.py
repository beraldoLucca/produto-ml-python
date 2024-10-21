from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class CategoryEnum(enum.Enum):
    BEBIDAS = "Bebidas"
    LANCHES = "Lanches"
    ELETRONICOS = "Eletrônicos"
    LIVROS = "Livros"

class ProductModel(Base):
    __tablename__ = 'produto'

    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    category = Column(Enum(CategoryEnum), nullable=False)

