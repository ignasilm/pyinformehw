from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Baseboard(Base):
    __tablename__ = 'baseboard'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    description = Column(String(18))
    manufacturer = Column(String(19))
    name = Column(String(17))
    product = Column(String(14))
    serialnumber = Column(String(31))
    version = Column(String(16))
    
    def __init__(self, computer, columns):
        self.computer = computer
        self.mapa_campos = columns
    
    def leer_linea(self, linea):
        pos_anterior = 0
        for campo,pos in self.mapa_campos.items():
            #print(campo, linea[pos_anterior:pos])
            valor = linea[pos_anterior:pos].strip()
            pos_anterior = pos
            if campo == 'Description':
                self.description = valor
            elif campo == 'Manufacturer':
                self.manufacturer = valor
            elif campo == 'Name':
                self.name = valor
            elif campo == 'Product':
                self.product = valor
            elif campo == 'SerialNumber':
                self.serialnumber = valor
            elif campo == 'Version':
                self.version = valor
