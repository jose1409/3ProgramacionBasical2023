import os
import time
from getpass import getpass
from configuracion_avanzada import menu_configuracion_avanzada
import Blackjack

#Funcion usada para limpiar la terminal cuando se sobre cargue mucho de inforamcion
def limpiar_pantalla():
    os.system('cls')

#De aqui hacia abajo hay funciones de DreamWorldCasino hasta nuevo comentario avisando de finalizacion

#Si se selecciona DreamWorldCasino, si no existiese ningun tipo de usuario, sera devuelto al Menu
def verificacion_existencia():
    dato = 'ID'
    usuarios = []
    cantidad_carpetas = os.listdir()
    for carpeta in cantidad_carpetas:
        if os.path.isdir(carpeta) and carpeta != 'codigo_fuente':
            usuarios.append(carpeta)
    if len(usuarios) != 0:
        verificacion_2(dato)
    else:
        print('No existe ni un solo usuario activo, vaya a Registro de Usuario nuevo')

#Aqui se sacaran los usuarios y contraseñas para ser guardadas y verificadas.
def lectura_usuarios(opcion,dato):
    verificar = []
    archivo = open('usuarios_pines.txt', 'r')
    usuarios = archivo.read().splitlines()
    for i in range(0,len(usuarios),2):
        usuario = usuarios[i]
        pin = usuarios[i+1]
        verificar.append((usuario,pin))
    archivo.close()
    print(verificar)
    if dato == 'ID':
        for usuario,pin in verificar:
            if usuario == opcion:
                dato = 'PIN'
                verificacion_2(dato)
            elif usuario != opcion:
                limpiar_pantalla()
                print('Error: ID no valido, intente nuevamente')
    else:
        for usuario,pin in verificar:
            if pin == opcion:
                limpiar_pantalla()
                print(f'Bienvenido al sistema señor {usuario}')
                menu_inicio(usuario,pin)
            else:
                limpiar_pantalla()
                print('Error: PIN no valido, intente nuevamente')
  
#Si pasa la primer verificacion, se verificara que ingrese un ID y usuario correcto con 3 intentos
def verificacion_2(dato):
    global cierre
    if dato == 'ID':
        for i in range(3):
            id_pin = input(f'Ingrese su {dato}:')
            lectura_usuarios(id_pin,dato)
            if i == 2 and dato == 'ID':
                print('Se excedió el máximo de intentos para ingresar su ID, volviendo al menú principal')

    else:
        for i in range(3):
            id_pin = getpass(f'Ingrese su {dato}:')
            lectura_usuarios(id_pin,dato)
            if i == 2:
                print('Se excedió el máximo de intentos para ingresar su ID, volviendo al menú principal')

#Funcion que mostrara el saldo del usuario registrado
def ver_saldo(ID):
    archivo = open(os.path.join(ID, 'saldos.txt'), 'r')
    saldo = archivo.read()
    archivo.close()
    limpiar_pantalla()
    return print(f'Tu saldo actualmente es de ${saldo}, Volviendo al Submenu')

#Aqui estara un usuario registrado, disponible todas las opciones que desee hacer o incluso jugar
def menu_inicio(usuario,pin):
    print(usuario,pin)
    while True:
        try:
            opcion = int(input('1. Retirar Dinero\n2. Depositar Dinero\n3. Ver Saldo Actual\n4. Juegos en Linea\n5. Eliminar Usuario\n6. Salir\n>>>'))
            if opcion == 1:
                print('Trabajando')
            elif opcion == 2:
                print('Trabajando')
            elif opcion == 3:
                ver_saldo(usuario)
            elif opcion == 4:
                limpiar_pantalla()
                while True:
                    juego = int(input('1- Blackjack\n2- Tragamonedas\n3- Salir\n>>>'))
                    if juego == 1:
                        Blackjack.inicio(usuario)
                    elif juego == 2:
                        print('Trabajando')
                    elif juego == 3:
                        limpiar_pantalla()
                        print('Volviendo al Submenu')
                        break
                    else:
                        limpiar_pantalla()
                        print('Error: Digite una de las opciones anteriores, volviendo al menu de juegos')
            elif opcion == 5:
                print('Trabajando')
            elif opcion == 6:
                print('Gracias por acompañarnos, volviendo al Menu Principal')
                break
            else:
                limpiar_pantalla()
                print('Error: Seleccione un numero de las opciones anteriores')
        except ValueError:
            limpiar_pantalla()
            print('Error: Digite un numero')

#Fin Funciones de DreamWorldCasino


# Menu Principal
os.chdir('./readme/')
while True:
    try:
        print('---Bienvenido a DreamWorld Casino---\n1. Registro de usuario nuevo\n2. DreamWorld Casino\n3. Configuracion avanzada\n''4. Salir')
        opcion = int(input('Digite la opción que desea realizar:'))
        if opcion == 1:
            limpiar_pantalla()
            print('Bienvenido al registro de Usuario Nuevo, por favor digite su ID (Nombre de Usuario)\n'
                  'Tiene que ser Alfanumerico / Minimo 5 caracteres')
            usuario_creado = False
            for i in range(3):
                ID = input('Ingrese su ID:')
                # Verificacion de que se cumpla el minimo de digitos para el usuario
                if len(ID) < 5:
                    print('Error: El ID debe tener al menos 5 digitos, intente nuevamente')
                # Verificacion para saber si el Usuario ya existe y creacion de carpeta en el caso que no
                else:                     
                    if(os.path.exists(ID)):
                        print(f"El usuario {ID} ya existe, intente con otro ID")
                    else:
                        time.sleep(0.5)
                        nombre = input('Ingrese su Nombre Completo:')
                        #Ciclo que no terminara hasta que digite bien la contraseña, y creada los archivos cuando se verifique
                        while True:         
                            PIN = getpass('Digite su PIN')
                            if len(PIN) < 6:
                                print('Error: Tu PIN debe tener al menos 6 digitos, intente nuevamente')
                            else:
                                PIN_confirmacion = getpass('Ingrese nuevamente su PIN para confirmacion')
                                if PIN == PIN_confirmacion:
                                    time.sleep(0.5)
                                    limpiar_pantalla()
                                    print('El PIN ha sido creado exitosamente')
                                    os.mkdir(ID)
                                    print(f"el ID {ID} ha sido creado, volviendo al Menu Principal")
                                    archivo = open(os.path.join(ID, 'saldos.txt'), 'w')
                                    archivo.write(str(0) + '\n')
                                    archivo.close()
                                    #Modos de lectura en BibliotecaOS.py
                                    archivo = open('usuarios_pines.txt', 'a')
                                    archivo.write(f'{ID}\n')
                                    archivo.write(f'{PIN}\n')
                                    archivo.close()
                                    usuario_creado = True
                                    break
                                else:
                                    print('Error: El PIN de confirmacion no coincide, intente nuevamente')
                #Si el usuario supera los intentos, se devuelve al menu principal                                               
                if i == 2:                 
                    time.sleep(2)
                    limpiar_pantalla()
                    print('Se excedio el maximo de intentos para ingresar un ID valido, volviendo al Menu principal')
                if usuario_creado:
                    break









        elif opcion == 2:
            verificacion_existencia()
        elif opcion == 3:
            menu_configuracion_avanzada()
        elif opcion == 4:
            print('Gracias por visitar DreamWorld Casino, vuelva pronto')
            break

        else:
            print('*Error: Debes ingresar un número entre 1 y 4. Intente nuevamente*')  
    except ValueError:
        print('*Error: Debes ingresar un número entero. Intente nuevamente*')