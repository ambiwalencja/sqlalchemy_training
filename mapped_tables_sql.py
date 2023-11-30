# to zadziała ale tylko w podejściu nie orm, tylko sqlowe
# czyli żeby żeby wrzucić coś potem do tej tabeli musimy napisać to w sqlu
# a żeby to zrobić tak, jak w przypadku models.py czyli parametry modelu, to trzeba inaczej pobrać te dane

from sqlalchemy import MetaData, Table
from connection import engine

metadata = MetaData(bind=engine) # on nam służy do wyciągania danych na temat tabeli

# musimy wiedzieć, że tabela istnieje, musimy znać jej nazwę chociaż

plant_info = Table(name='plant_info', metadata=metadata, autoload=True, autoload_with=engine)
# metadata wyciąga informacje
# autoload - że od razu wyciąga dane, a nie przy pierwszym wykorzystaniu dopiero
# autoload_with - którego połączenia mamy użyć (bo przecież można mieć różne połaczenia, connection stringi, nawet do tej samej tabeli, bo możemy mieć różne uprawnienia)
