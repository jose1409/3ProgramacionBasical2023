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
    usuarios = []
    cantidad_carpetas = os.listdir()
    for carpeta in cantidad_carpetas:
        if os.path.isdir(carpeta) and carpeta != 'codigo_fuente':
            usuarios.append(carpeta)
    if len(usuarios) != 0:
        verificacion_2()
    else:
        print('No existe ni un solo usuario activo, vaya a Registro de Usuario nuevo')

#Returna una lista con todos los usuarios y contraseñas para poder verificar si son correctas
def obtener_datos():
    verificar = []
    archivo = open('usuarios_pines.txt', 'r')
    usuarios = archivo.read().splitlines()
    for i in range(1,len(usuarios),2):
        usuario = usuarios[i]
        pin = usuarios[i+1]
        verificar.append((usuario,pin))
    archivo.close()
    return verificar

#Verifica si el usuario es correcto
def verificar_id(id):
    temp = False
    verificar = obtener_datos()
    for usuario,pin in verificar:
        if usuario == id:
            temp = True
    return temp

#Verifica si el Pin es correcto
def verificar_pin(contra):
    temp = False
    verificar = obtener_datos()
    for usuario,pin in verificar:
        if pin == contra:
            temp = True
    return temp

#Si pasa la primer verificacion, se verificara que ingrese un ID y usuario correcto con 3 intentos
def verificacion_2():
        i = 0
        j = 0
        while i < 3:
            id_pin = input('Ingrese su ID:')
            i += 1
            if verificar_id(id_pin) == True:
                while j < 3:
                    pin_id = getpass('Ingrese la contraseña:')
                    if verificar_pin(pin_id) == True:
                        j = 3
                        i = 3
                        limpiar_pantalla()
                        print(f'Bienvenido al sistema señor(a) {id_pin}')
                        menu_inicio(id_pin,pin_id)
                    j += 1

#Funcion que mostrara el saldo del usuario registrado
def ver_saldo(ID,opcion):
    archivo = open(os.path.join(ID, 'saldos.txt'), 'r')
    saldo = archivo.read()
    archivo.close()
    limpiar_pantalla()
    if opcion == 0:
        print(f'Tu saldo actualmente es de ${saldo}, Volviendo al Submenu')
    else:
        return saldo

#Aqui se realizara las verificaciones y depositos de dinero correspondientes
def deposito(usuario):
    while True:
        try:
            dinero = int(input('1. Colones\n2. Dolares\n3. Bitcoin\nEn que moneda desea depositar:'))
            if dinero == 1:
                print('Trabajando, aun no disponible')
                break
            elif dinero == 2:
                limpiar_pantalla()
                monto = int(input('Digite el monto a depositar\n>>>'))
                if monto <= 0:
                    print('Error: no puede depositar montos menores a 0, volviendo al Submenu')
                    break
                else:
                    archivo = open(os.path.join(usuario, 'saldos.txt'), 'r+')
                    monto_viejo = archivo.read()
                    monto_viejo = int(monto_viejo)
                    total = monto_viejo + monto
                    archivo.seek(0)
                    archivo.write(str(total) + '\n')
                    archivo.close()
                    limpiar_pantalla()
                    print(f'Transaccion realizada, deposito exitoso de ${monto}, tu saldo actual es de ${total}')
                    break
            elif dinero == 3:
                print('Trabajando, aun no disponible')
                break
            else:
                print('Error, digite una de las opciones anteriores')
        except ValueError:
            limpiar_pantalla()
            print('Error, seleccione una de las monedas anteriores')

#Este es el Submenu de Juegos, aqui se podra decidir que puede jugar.
def menu_juegos(usuario):
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

#Aqui estara un usuario registrado, disponible todas las opciones que desee hacer o incluso jugar
def menu_inicio(usuario,pin):
    dato = 0
    while True:
        try:
            opcion = int(input('1. Retirar Dinero\n2. Depositar Dinero\n3. Ver Saldo Actual\n4. Juegos en Linea\n5. Eliminar Usuario\n6. Salir\n>>>'))
            if opcion == 1:
                retiro(usuario)
            elif opcion == 2:
                deposito(usuario)
            elif opcion == 3:
                ver_saldo(usuario,dato)
            elif opcion == 4:
                menu_juegos(usuario)
            elif opcion == 5:
                print('Trabajando')
            elif opcion == 6:
                limpiar_pantalla()
                print('Gracias por acompañarnos, volviendo al Menu Principal')
                break
            else:
                limpiar_pantalla()
                print('Error: Seleccione un numero de las opciones anteriores')
        except ValueError:
            limpiar_pantalla()
            print('Error: Digite un numero')

#Es posible retirar el dinero que el usuario decida sacar
def retiro(ID):
    dato = 1
    intentos = 3
    while intentos > 0:
        try:
            retiro = int(input(f'Bienvenido a retiro, tu saldo actual actual es de {ver_saldo(ID,dato)}\n¿cuanto desea retirar?:'))
            saldo = int(ver_saldo(ID, dato))
            if retiro == 0:
                print('Error, no puede retirar montos menores o iguales a 0')
            elif retiro <= saldo:
                    archivo = open(os.path.join(ID, 'saldos.txt'), 'r+')
                    monto_viejo = archivo.read()
                    monto_viejo = int(monto_viejo)
                    monto_viejo -= retiro
                    archivo.seek(0)
                    archivo.write(str(monto_viejo) + '\n')
                    archivo.close()
                    limpiar_pantalla()
                    print(f'Transaccion realizada, retiro exitoso de ${retiro}, tu saldo actual es de ${monto_viejo}')
                    break
            elif intentos == 0:
                print('Error, supero el numero de intentos posibles, regresando al Menu principal')
                
            else:
                intentos -= 1
                print(f'Error, el saldo no es suficiente para retirar ${retiro}, le quedan {intentos} intentos')
        except ValueError:
            print(f'Tiene que digitar un monto correcto, le quedan {intentos} intentos')



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