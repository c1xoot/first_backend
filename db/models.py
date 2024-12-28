from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String


class Base(DeclarativeBase):
    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = "user"

    first_name = Column(String)
    last_name = Column(String)
    age  = Column(Integer, )