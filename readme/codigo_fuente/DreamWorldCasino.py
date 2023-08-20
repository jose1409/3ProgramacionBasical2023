import os



def verificacion_1():
    os.chdir('./readme/')
    usuarios = []
    cantidad_carpetas = os.listdir()
    for carpeta in cantidad_carpetas:
        if os.path.isdir(carpeta) and carpeta != 'codigo_fuente':
            usuarios.append(carpeta)
    if len(usuarios) != 0:
        verificacion_2
    else:
        print('No existe ni un solo usuario activo, vaya a Creacion de Usuario')

verificacion_1()


def verificacion_2():
    print