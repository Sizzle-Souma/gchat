from datetime import datetime

from pydantic import BaseModel

from user.schemas import User


class MessageBase(BaseModel):
    content: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int

    date: datetime
    owner: User

    class Config:
        orm_mode = True
