from sqlalchemy import MetaData, Table
from connection import engine, Base
from sqlalchemy.orm import registry # rejestr przetrzymujący zmapowane tabele

metadata = MetaData(schema='core') # tym razem engine nie potrzeba, core = dane tabeli będa według standardowych schematów postgresa

plant_info = Table('plant_info', metadata, autoload_with=engine) # pierwsze dwa argumenty są pozycyjnem, nie potrzebują klucza
# tutaj dokładnie to co w sqlowym podejściu - bierzemy informacje o tabeli i wrzucamy do obiektu klasy Table

mapper_registry = registry() # tworzymy rejestr zmapowanych tabel do klas

class PlantInfo: # tworzymy pustą klasę, bo nie wiemy jak ona będzie wyglądać
    pass

mapper_registry.map_imperatively(PlantInfo,plant_info) # teraz mapujemy: 1 parametr - do jakiej klasy, 2 parametr - skąd, z jakiej tabeli