from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class OrderStatusEnum(str, Enum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"

class OrderBase(BaseModel):
    #product_id: int
    #buyer_id: int
    quantity: int
    total_price: float
    #status: OrderStatusEnum

class OrderCreate(OrderBase):
    pass
