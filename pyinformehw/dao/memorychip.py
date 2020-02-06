from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Memorychip(Base):
    __tablename__ = 'memorychip'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    capacity = Column(String(17))
    description = Column(String(22))
    devicelocator = Column(String(20))
    manufacturer = Column(String(19))
    name = Column(String(22))
    partnumber = Column(String(23))
    positioninrow = Column(String(20))
    serialnumber = Column(String(19))
    speed = Column(String(12))
    tag = Column(String(24))
    typedetail = Column(String(19))
    
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
            elif campo == 'Description':
                self.description = valor
            elif campo == 'DeviceLocator':
                self.devicelocator = valor
            elif campo == 'Manufacturer':
                self.manufacturer = valor
            elif campo == 'Name':
                self.name = valor
            elif campo == 'PartNumber':
                self.partnumber = valor
            elif campo == 'PositionInRow':
                self.positioninrow = valor
            elif campo == 'SerialNumber':
                self.serialnumber = valor
            elif campo == 'Speed':
                self.speed = valor
            elif campo == 'Tag':
                self.tag = valor
            elif campo == 'TypeDetail':
                self.typedetail = valor
