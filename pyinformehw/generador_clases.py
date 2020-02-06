import glob
from os import chdir
import codecs


def generarClase(seccion, mapa_campos):
    file = open(seccion.lower()+'.py','w')

    parte1 = ['from sqlalchemy import Column, Integer, String\n', 
              'from pyinformehw.dao.base import Base\n','\n']
    file.writelines(parte1)
    file.write('class ' + seccion.capitalize() + '(Base):\n')
    file.write("    __tablename__ = '" + seccion.lower() + "'\n\n")

    parte2 = ['    mapa_campos = {}\n','    \n', 
              '    id = Column(Integer, primary_key=True)\n',
              '    computer = Column(String(20))\n']
    file.writelines(parte2)

    pos_anterior = 0
    for campo,pos in map_campo.items():
        tamanyo = (pos-pos_anterior+5)
        file.write('    ' + campo.lower() + ' = Column(String(' + str(tamanyo) +'))\n')
        pos_anterior = pos

    parte3 = ['    \n','    def __init__(self, computer, columns):\n', 
              '        self.computer = computer\n',
              '        self.mapa_campos = columns\n','    \n',
              '    def leer_linea(self, linea):\n',
              '        pos_anterior = 0\n',
              '        for campo,pos in self.mapa_campos.items():\n',
              '            #print(campo, linea[pos_anterior:pos])\n',
              '            valor = linea[pos_anterior:pos].strip()\n',
              '            pos_anterior = pos\n']
    file.writelines(parte3)

    i = 0
    for campo in map_campo:
        if i==0:
            file.write("            if campo == '" + campo + "':\n")
        else: 
            file.write("            elif campo == '" + campo + "':\n")
        file.write('                self.' + campo.lower() + ' = valor\n')
        i = i + 1

    file.close()
    

chdir('./ficherosEntrada')
#Recorremos todos los ficheros de la carpeta que cumplen el patron
for file_name in glob.glob('info_*.txt'):
    print(file_name)
    
    #dividimos el nombre para saber usuario y maquina
    file_name_parts = file_name.split('_')
    user = file_name_parts[1]
    computer = file_name_parts[2]

    #leemos el fichero linea a linea, procesando la cabecera de seccion, la linea de titulos y los datos
    seccion = ''
    primera_linea = False

    fichero = codecs.open(file_name,'r','utf_16_le')
    
    lineas = fichero.readlines()
    for linea in lineas:
        #Cabecera de seccion
        if linea[0] == '#':
            seccion = linea.strip()[1:-1]
            print('Seccion', seccion)
            primera_linea = True

        #titulos de la linea
        elif primera_linea:
            primera_linea = False
            lista_campos = linea.split()
            map_campo = {}
            for i in range(0,len(lista_campos)):
                if i == len(lista_campos)-1:
                    map_campo[lista_campos[i]] = len(linea)
                else:
                    map_campo[lista_campos[i]] = linea.find(lista_campos[i+1])
            print(map_campo)
            generarClase(seccion,map_campo)

        #lineas de datos
        else:
            pass
            #pos_anterior = 0
            #for campo,pos in map_campo.items():
            #    print(campo, linea[pos_anterior:pos])
            #    pos_anterior = pos
    print('fin')
        
            