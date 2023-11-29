from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from connection import Base

class Animals(Base): # dziedziczy z Base
    __tablename__ = "animal_info" # to musi być dokładnie ta sama nazwa, co nazwa tabeli, do której chcemy wrzucać dane
    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    color = Column(String)
    food_preference = Column(String)

class People(Base): # dziedziczy z Base
    __tablename__ = "people_info"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sex = Column(String)
    height = Column(Integer)
    hobby = Column(String)