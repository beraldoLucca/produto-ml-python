from enum import Enum
from typing import Optional
from pydantic import BaseModel

class CategoryEnum(str, Enum):
    BEBIDAS = "Bebidas"
    LANCHES = "Lanches"
    ELETRONICOS = "Eletrônicos"
    LIVROS = "Livros"

class ProductResponseSchema(BaseModel):
    name: str
    description: Optional[str] = None
    category: CategoryEnum

    class Config:
        orm_mode = True
