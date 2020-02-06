from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Volume(Base):
    __tablename__ = 'volume'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    capacity = Column(String(19))
    driveletter = Column(String(18))
    drivetype = Column(String(16))
    filesystem = Column(String(17))
    freespace = Column(String(18))
    label = Column(String(23))
    name = Column(String(58))
    
    def __init__(self, computer, columns):
        self.computer = computer
        self.mapa_campos = columns
    
    def leer_linea(self, linea):
        pos_anterior = 0
        for campo,pos in self.mapa_campos.items():
            #print(campo, linea[pos_anterior:pos])
            valor = linea[pos_anterior:pos].strip()
            pos_anterior = pos
            if campo == 'Capacity':
                self.capacity = valor
            elif campo == 'DriveLetter':
                self.driveletter = valor
            elif campo == 'DriveType':
                self.drivetype = valor
            elif campo == 'FileSystem':
                self.filesystem = valor
            elif campo == 'FreeSpace':
                self.freespace = valor
            elif campo == 'Label':
                self.label = valor
            elif campo == 'Name':
                self.name = valor
