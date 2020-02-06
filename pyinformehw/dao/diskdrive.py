from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class Diskdrive(Base):
    __tablename__ = 'diskdrive'

    mapa_campos = {}
    
    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    description = Column(String(18))
    deviceid = Column(String(25))
    interfacetype = Column(String(20))
    manufacturer = Column(String(29))
    mediatype = Column(String(28))
    model = Column(String(32))
    name = Column(String(25))
    sectorspertrack = Column(String(22))
    size = Column(String(19))
    totalcylinders = Column(String(21))
    totalheads = Column(String(17))
    totalsectors = Column(String(19))
    totaltracks = Column(String(18))
    trackspercylinder = Column(String(26))
    
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
            elif campo == 'DeviceID':
                self.deviceid = valor
            elif campo == 'InterfaceType':
                self.interfacetype = valor
            elif campo == 'Manufacturer':
                self.manufacturer = valor
            elif campo == 'MediaType':
                self.mediatype = valor
            elif campo == 'Model':
                self.model = valor
            elif campo == 'Name':
                self.name = valor
            elif campo == 'SectorsPerTrack':
                self.sectorspertrack = valor
            elif campo == 'Size':
                self.size = valor
            elif campo == 'TotalCylinders':
                self.totalcylinders = valor
            elif campo == 'TotalHeads':
                self.totalheads = valor
            elif campo == 'TotalSectors':
                self.totalsectors = valor
            elif campo == 'TotalTracks':
                self.totaltracks = valor
            elif campo == 'TracksPerCylinder':
                self.trackspercylinder = valor
