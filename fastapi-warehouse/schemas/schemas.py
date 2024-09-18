from pydantic import BaseModel, ConfigDict

class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
        
class ProductDisplay(ProductBase):
    pk: str
    model_config = ConfigDict(from_attributes=True)
