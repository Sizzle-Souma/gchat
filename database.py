import sys
from os import environ as env

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベース URL
try:
    DATABASE_URL = env['GCHAT_DATABASE_URL']
except KeyError:
    print('[error]: `GCHAT_DATABASE_URL` environment variable required')
    sys.exit(1)

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
