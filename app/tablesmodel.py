from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, text, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class OTP(Base):
    __tablename__ = 'otps'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, ForeignKey('users.email'))
    otp = Column(String, nullable=False)    

class Hotels(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String, nullable=False)
    hotel_list = Column(String, nullable=False)    