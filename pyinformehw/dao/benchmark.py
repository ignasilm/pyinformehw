from sqlalchemy import Column, Integer, String, Date, Numeric
from pyinformehw.dao.base import Base
from dateutil.parser import parse

class Benchmark(Base):
    __tablename__ = 'benchmark'

    id = Column(Integer, primary_key=True)
    computer = Column(String(20))
    fecha = Column(Date())
    core = Column(Numeric(10,2))
    multicore = Column(Numeric(10,2))
    
    def __init__(self, computer, fecha, core, multicore):
        self.computer = computer
        self.fecha = parse(fecha).date()
        self.core = core
        self.multicore = multicore
    
