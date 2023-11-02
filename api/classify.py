from fastapi import APIRouter
from pydantic import BaseModel
from prediction.detection import classify

router = APIRouter()

# Define a Pydantic model for data validation
class Email(BaseModel):
    email: str

@router.post("/classify")
def classify_email(item: Email):
    return {"isSpam": classify(item.email)}
