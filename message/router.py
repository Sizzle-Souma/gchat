from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.utils import get_user
from database import get_db
from . import schemas, service

router = APIRouter(
    dependencies=[Depends(get_user)],
    tags=["message"]
)


@router.get("/messages", response_model=list[schemas.Message])
def read_messages(db: Session = Depends(get_db)):
    messages = service.get_messages(db)
    return messages


@router.post("/messages", response_model=schemas.Message)
def create_messages(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return service.create_message(db, message, 1)
