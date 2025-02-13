from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import get_db
from .models import Property
from .schemas import PropertyResponse

router = APIRouter()

@router.get("/properties", response_model=List[PropertyResponse])
def get_all_properties(db: Session = Depends(get_db)):
    properties = db.query(Property).all()
    return properties

@router.get("/properties/{property_id}", response_model=PropertyResponse)
def get_property_by_id(property_id: int, db: Session = Depends(get_db)):
    property_record = db.query(Property).filter(Property.id == property_id).first()
    if not property_record:
        raise HTTPException(status_code=404, detail="Property not found")
    return property_record
