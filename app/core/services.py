from app.adapters.repositories import ProductRepository
from app.models import ProductModel, CategoryEnum


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def get_product_by_id_and_category(self, product_id: int, category: CategoryEnum) -> ProductModel | None:
        return self.repository.get_product_by_id_and_category(product_id, category)
