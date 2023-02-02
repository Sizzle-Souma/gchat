from datetime import datetime

from fastapi import WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session

from . import models


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: models.Message):
        print(message.owner.username)
        for connection in self.active_connections:
            await connection.send_json(message.as_dict())


manager = ConnectionManager()


def get_messages(db: Session):
    return db.query(models.Message).all()


def create_message(c: str, user_id: int, db: Session):
    db_message = models.Message(content=c, owner_id=user_id, date=datetime.utcnow())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


async def chat(ws: WebSocket, user_id: int, db: Session):
    await manager.connect(ws)
    try:
        while True:
            data: dict = await ws.receive_json()
            return_message: models.Message = create_message(data["content"], user_id, db)
            await manager.broadcast(return_message)
    except WebSocketDisconnect:
        manager.disconnect(ws)
