import glob
from os import chdir
import codecs

chdir('./ficherosEntrada')
for file_name in glob.glob('info_*.txt'):
    print(file_name)
    seccion = ''
    primera_linea = False
    #file = open(file_name,'r',encoding='utf_16_be')
    fichero = codecs.open(file_name,'r','utf_16_le')
    lineas = fichero.readlines()
    for linea in lineas:
        if linea[0] == '#':
            seccion = linea.strip()[1:-1]
            print('Seccion', seccion)
            primera_linea = True
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
        else:
            pos_anterior = 0
            for campo,pos in map_campo.items():
                print(campo, linea[pos_anterior:pos])
                pos_anterior = pos
    print('fin')
        
            