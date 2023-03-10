from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    date = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="messages", lazy="joined")

    def as_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "date": str(self.date),
            "owner": {
                "id": self.owner.id,
                "username": self.owner.username
            }
        }
