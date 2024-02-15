from app.db.config import SessionLocal
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.controllers.customer_controllers import create , get_customer, get_customers, update_customer,delete_customer
from app.schemas.customer_schemas import CustomerCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/customers/", response_model=CustomerCreate)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    try:
        customer = create(db=db, customer=customer)
        return customer
    except Exception as e:
        print("error", e)
        

@router.get("/customers/{customer_id}", response_model=CustomerCreate)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    return get_customer(db=db, customer_id=customer_id)

# @router.get("/customers/", response_model=list[CustomerResponse])
@router.get("/customers/")
def read_customers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_customers(db=db, skip=skip, limit=limit)

# @router.put("/customers/{customer_id}", response_model=CustomerCreate)
# def update_customer(customer_id: int, customer: CustomerCreate.CustomerUpdate, db: Session = Depends(get_db)):
#     return update_customer(db=db, customer_id=customer_id, customer=customer)

# @router.delete("/customers/{customer_id}", response_model=CustomerCreate)
# def delete_customer(customer_id: int, db: Session = Depends(get_db)):
#     return delete_customer(db=db, customer_id=customer_id)