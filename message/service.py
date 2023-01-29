from datetime import datetime

from sqlalchemy.orm import Session

from . import models, schemas


def get_messages(db: Session):
    return db.query(models.Message).all()


def create_message(db: Session, message: schemas.MessageCreate, user_id: int):
    db_message = models.Message(**message.dict(), owner_id=user_id, date=datetime.utcnow())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
