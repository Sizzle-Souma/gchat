from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.utils import get_user
from database import get_db
from . import schemas, service
from .models import User

router = APIRouter(
    tags=["user"]
)


@router.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="このネームはすでに存在しています。")
    return service.create_user(db=db, user=user)


@router.get("/users/me", response_model=schemas.User)
def read_users_me(current_user: User = Depends(get_user)):
    return current_user
