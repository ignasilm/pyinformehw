from pyinformehw.dao.base import Session, engine, Base
from pyinformehw.dao.user import User
from pyinformehw.dao.computersystem import ComputerSystem


def run():
    print("Hola Mundo!")

    linea = r"DESKTOP-2RVC015  AT/AT COMPATIBLE  MSI           MS-7972  DESKTOP-2RVC015  1                   Usuario de Windows  x64-based PC  DESKTOP-2RVC015\Usuario  "
    Base.metadata.create_all(engine)
    print('Creo engine', engine)
    session = Session()

    yo = ComputerSystem("DESKTOP-2RVC015","")
    yo.leer_linea(linea)

    session.add(yo)



    session.commit()
    session.close()