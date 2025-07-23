from pydantic import BaseModel , Field
from typing import List , Optional

class Product(BaseModel):
    name: str = Field(...)
    brand: Optional[str] = None
    price: float