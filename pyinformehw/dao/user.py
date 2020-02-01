from sqlalchemy import Column, Integer, String
from base import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(10) )
    complet_name = Column(String(100))

    def __init__(self, name, complet_name):
        self.name = name
        self.complet_name = complet_name
