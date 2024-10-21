from sqlalchemy.orm import Session

from app.models import ProductModel, CategoryEnum


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_product_by_id_and_category(self, product_id: int, category: CategoryEnum) -> ProductModel | None:
        return (self.db.query(ProductModel)
                .filter(ProductModel.product_id == product_id, ProductModel.category == category.name)
                .first())
