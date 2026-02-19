from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String)
    api_key=Column(String)
    user_name=Column(String,index=True)

class address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,index=True)
    address=Column(String,index=True)
    city=Column(String,index=True)
    state=Column(String,index=True)
    zip_code=Column(String,index=True)
    country=Column(String,index=True)

class Order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,index=True)
    address_id=Column(Integer,index=True)
    order_date=Column(DateTime,index=True)
    total_amount=Column(Integer,index=True)
    status=Column(String,index=True)
