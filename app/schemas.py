from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PropertyResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    location: Optional[str]
    price: float
    created_at: datetime  # <-- Cambiar de str a datetime


    class Config:
        orm_mode = True
