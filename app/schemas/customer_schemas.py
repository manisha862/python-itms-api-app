from pydantic import BaseModel

class CustomerCreate(BaseModel):
    Name: str
    PhoneNumber: str
    LogoUrl: str
    Address: str

class CustomerResponse(BaseModel):
    id: int
    Name: str
    PhoneNumber: str
    LogoUrl: str
    Address: str

class CustomerUpdate(BaseModel):
    Name: str
    PhoneNumber: str
    LogoUrl: str
    Address: str