import glob
from os import chdir
import codecs
from pyinformehw.dao.base import Session, engine, Base
from pyinformehw.dao.user import User
from pyinformehw.dao.computersystem import ComputerSystem

def crea_registro(seccion, computer, mapa_campos):
    if seccion == 'COMPUTERSYSTEM':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'BASEBOARD':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'CPU':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'MEMPHYSICAL':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'MEMORYCHIP':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'DISKDRIVE':
        return ComputerSystem(computer,mapa_campos)
    elif seccion == 'VOLUME':
        return ComputerSystem(computer,mapa_campos)



def run():
    print('Iniciamos ejecucion de PyInformeHW')

    Base.metadata.create_all(engine)
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
        registro_user = session.query(User).filter(User.name == user).all()
        if len(registro_user) > 0:
            registro_user.computer = computer
            session.add(registro_user)
        else:
            registro_user = User(user,'')
            registro_user.computer = computer
            session.add(registro_user)

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

    session.commit()
    session.close()