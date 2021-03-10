from helpers import mem_kb
import math
import random
from lista import *

def ingresar_arch(sectores, tam_sector, archivos,fat):
    try:
        tam = ['KB','MB', 'GB']
        nombre_arch = " ".join(input('Ingresar nombre del archivo: ').split())
        print(nombre_arch)
        if existe_archivo(archivos, nombre_arch):
            msg = 'Archivo existente'
            return False, archivos, fat, sectores, msg
        print('Tamaño')
        print('MIN: 1 KB')
        print('Ejemplo: 96 KB')
        tam_arch = " ".join(input('--> ').split())
        tam_arch = tam_arch.split(' ')
        sectores_requeridos = math.ceil(mem_kb(tam_arch)/ tam_sector)
            

        while (len(tam_arch) != 2) or not tam_arch[0].isdigit() or (tam_arch[1].upper() not in tam) or (float(tam_arch[0])<1 and tam_arch[1].upper()=='KB'):
            print('Ingrese tamaño valido. MIN: 1 KB')
            print('Ejemplo: 96 KB')
            tam_arch = " ".join(input('--> ').split())
            tam_arch = tam_arch.split(' ')
            sectores_requeridos = math.ceil(mem_kb(tam_arch) / tam_sector)


        if sectores_requeridos>sectores:
            msg = 'Espacio insuficiente'
            return False, archivos, fat, sectores, msg
            
        
        counter = 0
        archivos[nombre_arch] = Lista()
        while counter != sectores_requeridos:
            key = "S"+str(random.randrange(1,len(fat.keys())+1))
            print(key, end=' ')
            if fat[key] == None:
                fat[key] = nombre_arch
                archivos[nombre_arch].push(key)
                counter = counter + 1

        sectores = sectores - sectores_requeridos
        msg = 'Archivo insertado correctamente'
        return True, archivos, fat, sectores, msg

    except:
        msg = 'Ocurrio un error inesperado'
        return False, archivos, fat, sectores, msg


def generar_fat(n_sectores):

    fat = {"S"+str(i):None for i in range(1,int(n_sectores+1))}

    return fat



def existe_archivo(archivos, nombre):

    return nombre in archivos.keys()



def mostrar_fat(archivos, mem_disp):

    print('--- FAT ---')
    print('Memoria disponible: ', mem_disp, 'KB')
    sector = 64
    for key in archivos.keys():
        print(" --- --- --- ")
        print('Archivo: ', key)
        print('Espacio utilizado: ', str(archivos[key].length * sector), 'KB')
        print('Sectores utilizados: ', end='')
        archivos[key].print()
        print()

    print(" --- --- --- ")

    
def desfragmentar(fat, archivos):

    inicio = 1
    for key in archivos.keys():
        sec_requeridos = archivos[key].length
        claves = ["S"+str(x) for x in range(inicio, inicio+sec_requeridos)]
        
        index = 0
        for clave in claves:
            data_arch = archivos[key].get_data_by_index(index)
            if fat[clave] == None:
                fat[data_arch] = None    
            else:
                archivos[fat[clave]].editar_nodo(clave, data_arch)
                fat[data_arch] = fat[clave]

            fat[clave] = key
            archivos[key].editar_nodo(data_arch, clave)    
            index = index + 1
            

        inicio = inicio + sec_requeridos
        
    return fat, archivos
            


