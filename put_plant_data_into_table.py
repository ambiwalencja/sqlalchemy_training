from mapped_tables_orm import PlantInfo
from connection import Session
from sqlalchemy import inspect

mapper = inspect(PlantInfo)
for column in mapper.attrs:
    print(column.key)

# session = Session()

# # jak będziemy chcieli dodać rekord do takiej klasy z zaimportowanej tabeli, to nie dostaniemy 
# # podpowiedzi, czym uzupełnić, tylko najpierw musielibyśmy sobie wyprintować, zeby to podejrzeć, jeśli nie znamy wyglądu tabeli
# plant = PlantInfo()

# session.close()