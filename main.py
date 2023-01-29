from fastapi import FastAPI

from auth.router import router as auth_router
from database import Base, engine
from message.router import router as message_router
from user.router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
app.include_router(message_router)
app.include_router(auth_router)
