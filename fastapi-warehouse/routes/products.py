from fastapi import APIRouter
from schemas.schemas import ProductDisplay, ProductBase
from db.models import Product
from typing import List

router = APIRouter(
    prefix="/product",
    tags=["warehouse"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ProductDisplay)
def create_product(request: ProductBase):
    product = Product(
        name=request.name,
        price=request.price,
        quantity=request.quantity
    )
    product.save()
    return product

@router.get("/all/", response_model=List[ProductDisplay])
def get_products():
    product_pks = Product.all_pks()
    products = [Product.get(pk) for pk in product_pks]
    return products

@router.get("/{pk}/", response_model=ProductDisplay)
def get_product(pk: str):
    product = Product.get(pk)
    return product

@router.delete("/{pk}/")
def delete_product(pk: str):
    Product.delete(pk)
    return "Deleted"



