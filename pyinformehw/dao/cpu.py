from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Cpu(Base):
    __tablename__ = 'cpu'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    caption = Column(String(44))
    currentclockspeed = Column(String(24))
    description = Column(String(44))
    manufacturer = Column(String(19))
    maxclockspeed = Column(String(20))
    name = Column(String(46))
    numberofcores = Column(String(20))
    numberofenabledcore = Column(String(26))
    numberoflogicalprocessors = Column(String(32))
    processorid = Column(String(23))
    systemname = Column(String(20))
    
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
            elif campo == 'CurrentClockSpeed':
                self.currentclockspeed = valor
            elif campo == 'Description':
                self.description = valor
            elif campo == 'Manufacturer':
                self.manufacturer = valor
            elif campo == 'MaxClockSpeed':
                self.maxclockspeed = valor
            elif campo == 'Name':
                self.name = valor
            elif campo == 'NumberOfCores':
                self.numberofcores = valor
            elif campo == 'NumberOfEnabledCore':
                self.numberofenabledcore = valor
            elif campo == 'NumberOfLogicalProcessors':
                self.numberoflogicalprocessors = valor
            elif campo == 'ProcessorId':
                self.processorid = valor
            elif campo == 'SystemName':
                self.systemname = valor
