from sqlalchemy import MetaData, Table
from connection import engine, Base
from sqlalchemy.orm import registry # rejestr przetrzymujący zmapowane tabele

metadata = MetaData(schema='public') # tutaj trzeba podać schema z bazy danych - u nas jest to public
# ale np w przypadku bazy danych leancodu byłoby "core" bo oni mają nie postgres tylko coś innego
# i wtedy parametr schema jest inaczej interpretowany, jako że 
# dane tabeli mają być według standardowych schematów (cokolwiek to znaczy)

plant_info = Table('plant_info', metadata, autoload_with=engine) # pierwsze dwa argumenty są pozycyjnem, nie potrzebują klucza
# tutaj dokładnie to co w sqlowym podejściu - bierzemy informacje o tabeli i wrzucamy do obiektu klasy Table

mapper_registry = registry() # tworzymy rejestr zmapowanych tabel do klas

class PlantInfo: # tworzymy pustą klasę, bo nie wiemy jak ona będzie wyglądać
    pass

mapper_registry.map_imperatively(PlantInfo,plant_info) # teraz mapujemy: 1 parametr - do jakiej klasy, 2 parametr - skąd, z jakiej tabeli