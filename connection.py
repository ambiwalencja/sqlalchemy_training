
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

database_url = 'hidden'
engine = create_engine(database_url) # tworzymy silnik, który obsługuje połączenie
Base = declarative_base() # tworzymy sobie bazową klasę, która definiuje, że to, co stworzymy jako następne to będa tabele

Session = sessionmaker(bind=engine) # tworzymy propotyp sesji