import glob
from os import chdir
import codecs
from pyinformehw.dao.base import Session, engine, Base, borrar_todo, exportar
from pyinformehw.dao.user import User
from pyinformehw.dao.computersystem import Computersystem
from pyinformehw.dao.baseboard import Baseboard
from pyinformehw.dao.cpu import Cpu
from pyinformehw.dao.memphysical import Memphysical
from pyinformehw.dao.memorychip import Memorychip
from pyinformehw.dao.diskdrive import Diskdrive
from pyinformehw.dao.volume import Volume
from pyinformehw.dao.benchmark import Benchmark
from pyinformehw.dao.diskmodel import Diskmodel


def crea_registro(seccion, computer, mapa_campos):
    if seccion == 'COMPUTERSYSTEM':
        return Computersystem(computer,mapa_campos)
    elif seccion == 'BASEBOARD':
        return Baseboard(computer,mapa_campos)
    elif seccion == 'CPU':
        return Cpu(computer,mapa_campos)
    elif seccion == 'MEMPHYSICAL':
        return Memphysical(computer,mapa_campos)
    elif seccion == 'MEMORYCHIP':
        return Memorychip(computer,mapa_campos)
    elif seccion == 'DISKDRIVE':
        return Diskdrive(computer,mapa_campos)
    elif seccion == 'VOLUME':
        return Volume(computer,mapa_campos)


def run():
    print('Iniciamos ejecucion de PyInformeHW')

    Base.metadata.create_all(engine)

    #Borramos todos los datos de las tablas
    session = Session()
    borrar_todo(engine.connect())
    session.commit()
    session.close()

    session = Session()

    chdir('./ficherosEntrada')
    #Recorremos todos los ficheros de la carpeta que cumplen el patron
    for file_name in glob.glob('info_*.txt'):
        print('Procesando el fichero:', file_name)
        
        #dividimos el nombre para saber usuario y maquina
        file_name_parts = file_name.replace('.','_').split('_')
        user = file_name_parts[1]
        computer = file_name_parts[2]

        #Actualizamos el usuario o lo insertamos nuevo
        registro_user = session.query(User).filter(User.name == user).filter(User.computer == computer).first()
        if registro_user is not None:
            print('Usuario ya encontrado:',registro_user.name, '-',registro_user.computer)
        else:
            registro_user = User(user, computer)
            session.add(registro_user)
            print('Nuevo usuario insertado:',registro_user.name, '-',registro_user.computer)

        #leemos el fichero linea a linea, procesando la cabecera de seccion, la linea de titulos y los datos
        seccion = ''
        primera_linea = False

        fichero = codecs.open(file_name,'r','utf_16_le')
        
        lineas = fichero.readlines()
        for linea in lineas:
            #Cabecera de seccion
            if linea[0] == '#':
                seccion = linea.strip()[1:-1]
                #print('Seccion', seccion)
                primera_linea = True

            #titulos de la linea
            elif primera_linea:
                primera_linea = False
                lista_campos = linea.split()
                mapa_campos = {}
                for i in range(0,len(lista_campos)):
                    if i == len(lista_campos)-1:
                        mapa_campos[lista_campos[i]] = len(linea)
                    else:
                        mapa_campos[lista_campos[i]] = linea.find(lista_campos[i+1])
                #print(mapa_campos)

            #lineas de datos
            else:
                #creamos el registro que corresponda segun la seccion
                registro = crea_registro(seccion, computer, mapa_campos)
                #procesamos la linea
                registro.leer_linea(linea)
                #insertamos en BBDD
                session.add(registro)

    #Recorremos todos los ficheros de la carpeta que cumplen el patron
    for file_name in glob.glob('benchmark_*.txt'):
        print('Procesando el fichero:', file_name)
        
        #dividimos el nombre para saber maquina y fecha
        file_name_parts = file_name.replace('.','_').split('_')
        computer = file_name_parts[1]
        fecha = file_name_parts[2]

        #leemos el fichero linea a linea, procesando la cabecera de seccion, la linea de titulos y los datos
        fichero = codecs.open(file_name,'r','utf_8')
        
        lineas = fichero.readlines()
        for linea in lineas:
            valores = linea.replace('"','').split(',')
            registro_benckmark = Benchmark(computer,fecha,valores[0],valores[1] )
            session.add(registro_benckmark)

    session.commit()
    session.close()

    session = Session()

    #Actualizamos la tabla de modelos de discos por si ha entrado alguno nuevo
    Diskmodel.actualizar_diskmodel(engine.connect())

    session.commit()
    session.close()

    exportar('../InformeHW.xlsx')