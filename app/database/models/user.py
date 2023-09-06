from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.database.db import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True)
    username = Column(String(30))
    hashed_password = Column(String(100))
    steamid = Column(Integer)
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    wallet = relationship('Wallet', back_populates='user')


class Wallet(Base):
    __tablename__ = "balance"

    id = Column(Integer, primary_key=True, unique=True)
    balance = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='wallet')


class ShopItem(Base):
    __tablename__ = "shopitem"

