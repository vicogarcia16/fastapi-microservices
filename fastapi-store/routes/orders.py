from fastapi import APIRouter
from typing import List
from db.models import Order, ProductOrder
from schemas.schemas import ProductOrderBase, ProductOrderDisplay
from fastapi.background import BackgroundTasks
from tools.orders import order_complete
import requests

router = APIRouter(
    prefix="/orders",
    tags=["store"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
def create_order(productOrder: ProductOrderBase, background_tasks: BackgroundTasks):
    req = requests.get(f"http://localhost:8000/product/{productOrder.product_id}")
    product = req.json()
    fee = product["price"] * 0.2
    order = Order(
        product_id = productOrder.product_id,
        price = product["price"],
        fee = fee,
        total = product["price"] + fee,
        quantity = productOrder.quantity,
        status = "pending"
    )
    order.save()
    background_tasks.add_task(order_complete, order)
    return order

@router.get("/all/", response_model=List[ProductOrderDisplay])
def get_orders():
    orders_pks = Order.all_pks()
    orders = [Order.get(pk) for pk in orders_pks]
    return orders

@router.get("/{pk}/", response_model=ProductOrderDisplay)
def get_order(pk: str):
    order = Order.get(pk)
    return order    
    
   