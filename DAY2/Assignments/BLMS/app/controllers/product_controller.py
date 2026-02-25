from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.product_schema import ProductCreate, ProductResponse
from app.services.product_service import ProductService
from app.repositories.product_repository import ProductRepository
from app.core.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])

repo = ProductRepository()
service = ProductService(repo)


@router.post("", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db)
):
    return service.create_product(db, data)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return service.get_product(db, product_id)


@router.get("", response_model=list[ProductResponse])
def get_products(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return service.get_products(db, skip, limit)