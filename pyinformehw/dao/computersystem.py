from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Computersystem(Base):
    __tablename__ = 'computersystem'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    caption = Column(String(18))
    description = Column(String(23))
    manufacturer = Column(String(19))
    model = Column(String(20))
    name = Column(String(18))
    numberofprocessors = Column(String(25))
    primaryownername = Column(String(23))
    systemtype = Column(String(19))
    username = Column(String(25))
    
    def __init__(self, computer, columns):
        self.computer = computer
        self.mapa_campos = columns
    
    def leer_linea(self, linea):
        pos_anterior = 0
        for campo,pos in self.mapa_campos.items():
            #print(campo, linea[pos_anterior:pos])
            valor = linea[pos_anterior:pos].strip()
            pos_anterior = pos
            if campo == 'Caption':
                self.caption = valor
            elif campo == 'Description':
                self.description = valor
            elif campo == 'Manufacturer':
                self.manufacturer = valor
            elif campo == 'Model':
                self.model = valor
            elif campo == 'Name':
                self.name = valor
            elif campo == 'NumberOfProcessors':
                self.numberofprocessors = valor
            elif campo == 'PrimaryOwnerName':
                self.primaryownername = valor
            elif campo == 'SystemType':
                self.systemtype = valor
            elif campo == 'UserName':
                self.username = valor
