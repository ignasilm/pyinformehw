from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Memphysical(Base):
    __tablename__ = 'memphysical'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    maxcapacity = Column(String(18))
    memorydevices = Column(String(22))
    
    def __init__(self, computer, columns):
        self.computer = computer
        self.mapa_campos = columns
    
    def leer_linea(self, linea):
        pos_anterior = 0
        for campo,pos in self.mapa_campos.items():
            #print(campo, linea[pos_anterior:pos])
            valor = linea[pos_anterior:pos].strip()
            pos_anterior = pos
            if campo == 'MaxCapacity':
                self.maxcapacity = valor
            elif campo == 'MemoryDevices':
                self.memorydevices = valor
