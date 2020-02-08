from sqlalchemy import Column, Integer, String
from pyinformehw.dao.base import Base

class User(Base):
    __tablename__ = 'user'

    name = Column(String(10), primary_key=True )
    computer = Column(String(20), primary_key=True )
    complet_name = Column(String(100))
    email = Column(String(100))
    num_empleado = Column(Integer)

    def __init__(self, name, computer):
        self.name = name
        self.computer = computer

