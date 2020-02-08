from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
import pandas as pd

engine = create_engine('sqlite:///pyinformehw/data/pyinformehw.db', connect_args={'timeout': 15})
#engine = create_engine('sqlite:///C:\\Python\\PyInformeHW\\pyinformehw\\pyinformehw\\data\\test.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()


def borrar_todo(con):
    print('Se van a borrar todos los datos.')
    tablas = ['VOLUME', 'DISKDRIVE', 'CPU', 'MEMORYCHIP', 'MEMPHYSICAL', 'BASEBOARD', 'COMPutersystem', 'BENCHMARK']

    for tabla in tablas:
        query = text('delete from ' + tabla + ';')
        borrados = con.execute(query)
        print('Se han eliminado',borrados.rowcount,'de la tabla', tabla)


def exportar(nom_excel):
    db_df = pd.read_sql_query("SELECT * FROM informehw;", engine)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(nom_excel, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    db_df.to_excel(writer, sheet_name='Informe HW')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()