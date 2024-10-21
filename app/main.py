from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories import ProductRepository
from app.adapters.schemas import ProductResponseSchema, CategoryEnum
from app.core.services import ProductService
from config.database import get_db

app = FastAPI()


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    repository = ProductRepository(db)
    return ProductService(repository)


@app.get("/products/{id}/{category}", response_model=ProductResponseSchema)
def get_product_by_id_and_category(id: int, category: CategoryEnum,
                                   service: ProductService = Depends(get_product_service)):
    product = service.get_product_by_id_and_category(id, category)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return product
