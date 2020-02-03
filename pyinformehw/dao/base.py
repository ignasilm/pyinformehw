from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from os import getcwd

#print(getcwd())
engine = create_engine('sqlite:///pyinformehw/data/test.db')
#engine = create_engine('sqlite:///C:\\Python\\PyInformeHW\\pyinformehw\\pyinformehw\\data\\test.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()