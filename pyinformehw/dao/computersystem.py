from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class ComputerSystem(Base):
    __tablename__ = 'computersystem'

    columns = [0,17,18,14,9,17,20,20,14,25]

    id = Column(Integer, primary_key=True)
    caption = Column(String(columns[1]) )
    description = Column(String(columns[2]) )
    manufacturer = Column(String(columns[3]) )
    model = Column(String(columns[4]) )
    name = Column(String(columns[5]) )
    number_of_processors  = Column(String(columns[6]) )
    primary_owner_name = Column(String(columns[7]) )
    system_type = Column(String(columns[8]) )
    user_name = Column(String(columns[9]) )         

    def __init__(self, name, complet_name):
        self.name = name
        self.complet_name = complet_name

    def leer_linea(self, linea):
        i = 1
        self.caption = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        #print(sum(self.columns[0:i]))
        #print(sum(self.columns[0:i+1]))
        self.description = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.manufacturer = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.model = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.name = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.number_of_processors = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.primary_owner_name = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.system_type = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]
        i += 1
        self.user_name = linea[sum(self.columns[0:i]):sum(self.columns[0:i+1])]

