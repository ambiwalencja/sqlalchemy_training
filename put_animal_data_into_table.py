from models import Animals, People
from connection import Base, engine, Session
import pandas as pd
# import generate_data # to powodowało, że za każdym razem dane generowały się od początku

Base.metadata.create_all(engine)

# csv_file = generate_data.filename # to powodowało, że za każdym razem dane generowały się od początku
csv_file = "animal_data_headers.csv"
data = pd.read_csv(csv_file) # to będzie dataframe

# print("Dane przed akcją")
# print(data.head())

for _, row in data.iterrows(): # wolne, do niewielkich tabeli
    animal = Animals(id=row['id'], name=row['name'],species=row['species'],age=row['age'],color=row['color'],food_preference=row['food_preference'])
    # powyżej, jak nie było dodanego id, to wpisywanym rekordom przypisywały się id uwzględniające rkordy, które były w tej tabeli wcześniej
    # czyli jak wcześniej było tam 5 wpisów, a potem je usunęliśmy, to po zaimportowaniu nasze rekordy miały id od 6 w górę
    session.add(animal)

session.commit()

# # sprawdzenie
# animals = session.query(Animals).all() # wewnątrz query możemy wybierać co chcemy pobrac z tabeli
# print("Tabela po akcji")
# for animal in animals[0:2]:
#     print(f'{id}, {animal.name}, {animal.species}')

session.close()
