def mostrar_menu():

    print('Asignacion de espacio de almacenamiento. Asignacion indexada')

    print('1) Ingresar archivo')
    print('2) Eliminar archivo')
    print('3) Mostrar FAT')
    print('4) Desfragmentar')
    print('5) Salir')


    opc = input("Elegir opcion: ")

    while not opc.isdigit() or int(opc)>5 or int(opc)<1:
        opc = input("Elegir opcion: ")


    return int(opc)


def memoria():

    tam = ['MB', 'GB']
    max_mb = 4096
    min_mb = 15
    max_gb = 4
    min_gb = 0.014648
    print('Teclear la cantidad de memoria total')
    print('Ejemplo: 250 MB')
    print('MAX: ', max_gb,' GB = ', max_mb, ' MB')
    print('MIN: ', min_mb, ' MB')
    print('Tamaños disponibles: ', tam)
    cant_mem = input('--> ').strip()
    cant_mem = " ".join(cant_mem.split())
    cant_mem = cant_mem.split(' ')
        
    while (len(cant_mem) != 2 ) or not cant_mem[0].isdigit() or (cant_mem[1].upper() not in tam) or (((float(cant_mem[0]) > max_mb or float(cant_mem[0]) < min_mb) and cant_mem[1].upper() == 'MB') or ((float(cant_mem[0]) > max_gb or float(cant_mem[0]) < min_gb) and cant_mem[1].upper() == 'GB')):
        print('MAX: ', max_gb,' GB = ', max_mb, ' MB')
        print('MIN: ', min_mb, ' MB')
        cant_mem = input('Ingresar cantidad valida: ')
        cant_mem = " ".join(cant_mem.split())
        cant_mem = cant_mem.split(' ')

    return mem_kb(cant_mem)

def mem_kb(mem):

    tam = int(mem[0])
    unidad = mem[1].upper()

    if unidad == 'MB':
        tam = tam * 1024
    elif unidad == 'KB':
        return tam 
    else:
        tam = tam * 1048576

    return tam
