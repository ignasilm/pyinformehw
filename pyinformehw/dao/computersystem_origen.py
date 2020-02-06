from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class ComputerSystem(Base):
    __tablename__ = 'computersystem'

    mapa_campos = {}

    id = Column(Integer, primary_key=True)
    computer = Column(String(20)) 
    caption = Column(String(20))
    description = Column(String(40))
    manufacturer = Column(String(20))
    model = Column(String(40))
    name = Column(String(20))
    number_of_processors  = Column(Integer)
    primary_owner_name = Column(String(20))
    system_type = Column(String(20))
    user_name = Column(String(40))         

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
                self.number_of_processors = int(valor)
            elif campo == 'PrimaryOwnerName':
                self.primary_owner_name = valor
            elif campo == 'SystemType':
                self.system_type = valor
            elif campo == 'UserName':
                self.user_name = valor

