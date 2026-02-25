from fastapi import HTTPException
from app.repositories.product_repository import ProductRepository


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository


    def create_product(self, db, data):

        return self.repository.create(db, data)


    def get_product(self, db, product_id):

        product = self.repository.get(db, product_id)

        if not product:
            raise HTTPException(404, "Product not found")

        return product


    def get_products(self, db, skip=0, limit=10):

        return self.repository.get_all(db, skip, limit)