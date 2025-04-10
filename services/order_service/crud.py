from datetime import datetime, timezone
from sqlalchemy.orm import Session
from models import Order
from schemas import OrderCreate



def create_order(order_data: OrderCreate, db: Session) -> Order:
    
    order_values = order_data.model_dump()

    db_order = Order(**order_values)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    
    return db_order

def get_orders(db: Session):
    return db.query(Order).all()

def get_order(order_id: int, db: Session):
    return db.query(Order).filter(Order.order_id == order_id).first()

def delete_order(order: Order, db: Session):
    db.delete(order)
    db.commit()
    return order

