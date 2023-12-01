from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from connection import Base

# tutaj budujemy modele od podstaw - to jest dobra praktyka, ale nie zawsze jest to realne

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


# inny sposób to mapowanie tabeli, czyili wymuszanie na sqlalachemy żeby on 
# wyciągnął wszystkie informacje o tabeli z bazy danych i zapisał je w pamięci tymczasowej (na czas trwania programu)
# są na to 3 sposoby przynajmniej
# zrobimy to w mapped_tables.py
