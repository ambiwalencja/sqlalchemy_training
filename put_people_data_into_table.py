from models import Animals, People
from connection import Base, engine, Session
import pandas as pd
import sample_data_and_functions

Base.metadata.create_all(engine) 
session = Session()


for i in range(100):
    record = sample_data_and_functions.generate_random_person()
    person = People(name=record[0],sex=record[1],height=record[2],hobby=record[3])
    # id=i
    session.add(person)

session.commit()

# sprawdzenie
people = session.query(People).all()
print("Tabela po akcji")
for person in people[0:2]:
    print(f'{id}, {person.name}, {person.hobby}')

session.close()
