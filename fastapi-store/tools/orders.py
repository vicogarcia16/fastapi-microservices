import time
from db.models import Order
from db.db import redis

def order_complete(order: Order):
  time.sleep(5)
  order.status = 'completed'
  order.save()
  redis.xadd(name='order-completed', fields=order.model_dump())