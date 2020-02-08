from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql import text
from pyinformehw.dao.base import Base

class Diskmodel(Base):
    __tablename__ = 'diskmodel'

    mapa_campos = {}
    
    model = Column(String(32), primary_key=True)
    interfacetype = Column(String(20))
    size = Column(Integer)
    ssd = Column(Boolean)
    
    def __init__(self, model, interfacetype, ssd):
        self.model = model
        self.interfacetype = interfacetype
        self.ssd = ssd

    def actualizar_diskmodel(con):
        print('Vamos a actualizar los modelos de disco')
        query = text('insert into diskmodel \
                        SELECT dd.model, dd.interfacetype, dd.size/1000/1000/1000 as size, false as ssd \
                        FROM DISKDRIVE dd \
                        left join diskmodel dm on dm.model = dd.model \
                        where dm.model is null \
                        group by dd.model;')
        insertados = con.execute(query)
        print('Se han insertado',insertados.rowcount,'discos nuevos.')
