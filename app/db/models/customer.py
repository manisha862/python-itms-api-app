from app.db.config import Base
from sqlalchemy import Column, Integer, String

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    PhoneNumber = Column(String)
    LogoUrl = Column(String)
    Address = Column(String)
