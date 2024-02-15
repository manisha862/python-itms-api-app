from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.models.customer import Customer
from app.schemas.customer_schemas import CustomerCreate, CustomerResponse, CustomerUpdate

def create(db: Session, customer: CustomerCreate):
    db_customer = Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.id == customer_id).first()

def get_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Customer).offset(skip).limit(limit).all()

def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        for key, value in customer.dict().items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if db_customer:
        db.delete(db_customer)
        db.commit()
        return db_customer
    else:
        raise HTTPException(status_code=404, detail="Customer not found")