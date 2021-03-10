from helpers import *
import math
from operaciones import *

def main():

    mem_total = memoria()
    print(mem_total, 'KB')
    sector = 64
    sectores = math.floor(mem_total / sector)
    print('Sectores Iniciales: ', sectores)
    archivos = {}
    fat = generar_fat(sectores)

    opc = mostrar_menu()


    while opc != 5:
        if opc==1:
            ingresado, archivos, fat, sectores, msg = ingresar_arch(sectores, sector, archivos, fat)
            if ingresado:
                print(msg)
            else:
                print(msg)
        
        if opc == 2:
            nombre_arch = " ".join(input('Ingresar nombre del archivo a eliminar: ').split())
            if existe_archivo(archivos, nombre_arch):
                archivos[nombre_arch].print()
                eliminado, fat, sec_liberados = archivos[nombre_arch].eliminar_del_fat(fat)
                if eliminado:
                    sectores = sectores + sec_liberados
                    del archivos[nombre_arch]
                    print('Archivo eliminado exitosamente')

            else:
                print('El archivo no existe')

        if opc == 3:
            mostrar_fat(archivos, mem_total)

        if opc == 4:
            fat, archivos = desfragmentar(fat, archivos)

        mem_total = sectores * sector
        #print('Memoria disponible: ', mem_total, ' KB')
        #print('Sectores disponibles: ', sectores)
        opc = mostrar_menu()
            
main()

