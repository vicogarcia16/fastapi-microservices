from pydantic import BaseModel, ConfigDict

class ProductOrderBase(BaseModel):
    product_id: str
    quantity: int
    
class ProductOrderDisplay(ProductOrderBase):
    pk: str
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str
    model_config = ConfigDict(from_attributes=True)
