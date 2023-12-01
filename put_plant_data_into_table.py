from mapped_tables_orm import PlantInfo
from connection import Session
from sqlalchemy import inspect

# pobieramy informacje o tabeli
mapper = inspect(PlantInfo)
# for column in mapper.attrs:
#     print(column.key, column.expression.type) # expression.type jest po to, żeby wyciągnąć typt wartości
# no i tutaj dostaliśmy info:
# id INTEGER
# species VARCHAR(50)
# edible BOOLEAN
# height INTEGER
# sunlight DOUBLE PRECISION

session = Session()

# jak będziemy chcieli dodać rekord do takiej klasy z zaimportowanej tabeli, to nie dostaniemy 
# podpowiedzi, czym uzupełnić, tylko najpierw musielibyśmy sobie wyprintować, zeby to podejrzeć, jeśli nie znamy wyglądu tabeli
plant = PlantInfo(species='Rose',edible=False,height=50,sunlight=0.35)
session.add(plant)
session.commit()

# sprawdzenie
plants = session.query(PlantInfo).all() # wewnątrz query możemy wybierać co chcemy pobrac z tabeli
print("Tabela po akcji")
for plant in plants[0:2]:
    print(f'{id}, {plant.species}, {plant.sunlight}')

session.close()
