from fastapi import FastAPI
from app.db.models.customer import Customer
from app.routers.customer_routers import router
from app.db.config import engine
from app.db.config import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.include_router(router, prefix="/book", tags=["book"])
app.include_router(router, prefix="/customer", tags=["Customer"])
# app.include_router(customer_router, prefix="/api/v1")

