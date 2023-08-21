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
        limpiar_pantalla()
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
                    i = 3
                    pin_id = getpass('Ingrese la contraseña:')
                    if verificar_pin(pin_id) == True:
                        j = 3
                        limpiar_pantalla()
                        print(f'Bienvenido al sistema señor(a) {id_pin}')
                        menu_inicio(id_pin,pin_id)
                    elif j == 2:
                        limpiar_pantalla()
                        print('Se excedió el máximo de intentos para ingresar su PIN, volviendo al menú principal')
                    j += 1
            elif i == 3:
                limpiar_pantalla()
                print('Se excedió el máximo de intentos para ingresar su ID, volviendo al menú principal')

#Funcion que mostrara el saldo del usuario registrado
def ver_saldo(ID,opcion):
    archivo = open(os.path.join(ID, 'saldos.txt'), 'r')
    saldo = archivo.read()
    archivo.close()
    if opcion == 0:
        limpiar_pantalla()
        print(f'Tu saldo actualmente es de ${saldo}, Volviendo al Submenu')
    else:
        return saldo

#Aqui se abrira el archivo y se sacara el valor para la conversion del colon
def conversion_colon():
    archivo = open('configuraciones_avanzadas.txt', 'r')
    contenido = archivo.read()
    lineas = contenido.split('\n')
    linea_colon = lineas[0]
    dato, valor = linea_colon.split(':')
    archivo.close()
    valor = int(valor)
    return valor

#Aqui se abrira el archivo y se sacara el valor para la conversion del Bitcoin
def conversion_bitcoin():
    archivo = open('configuraciones_avanzadas.txt', 'r')
    contenido = archivo.read()
    lineas = contenido.split('\n')
    linea_colon = lineas[1]
    dato, valor = linea_colon.split(':')
    archivo.close()
    valor = int(valor)
    return valor

#A la hora de depositar en colon, entrara esta funcion que llamara a la conversion y hara la escritura para tener el dinero correspondiente
def deposito_colon(usuario):
    colon = conversion_colon()
    monto = float(input('Digite el monto en colones a depositar\n>>>'))
    if monto <= 0:
        print('Error: no puede depositar montos menores a 0, volviendo al Submenu')
    else:
        convertido = monto / colon
        convertido = round(convertido,2)
        archivo = open(os.path.join(usuario, 'saldos.txt'), 'r+')
        monto_viejo = archivo.read()
        monto_viejo = float(monto_viejo)
        total = monto_viejo + convertido
        archivo.seek(0)
        archivo.write("{:.2f}\n".format(total)) #Bibliografia, del codigo usado
        archivo.close()
        limpiar_pantalla()
        print(f'Transaccion realizada, deposito exitoso de ₡{monto}, con un tipo de cambio de {colon} x 1 dolar, tu saldo actual es de ${total}')

#Aqui se almacena la funcion para hacer deposito en dolares.
def deposito_dolar(usuario):
    limpiar_pantalla()
    monto = float(input('Digite el monto en dolares a depositar\n>>>'))
    if monto <= 0:
        print('Error: no puede depositar montos menores a 0, volviendo al Submenu')
    else:
        archivo = open(os.path.join(usuario, 'saldos.txt'), 'r+')
        monto_viejo = archivo.read()
        monto_viejo = float(monto_viejo)
        total = monto_viejo + monto
        archivo.seek(0)
        archivo.write("{:.2f}\n".format(total)) #Bibliografia, del codigo usado
        archivo.close()
        limpiar_pantalla()
        print(f'Transaccion realizada, deposito exitoso de ${monto}, tu saldo actual es de ${total}')

#A la hora de depositar en bitcoin, entrara esta funcion que llamara a la conversion y hara la escritura para tener el dinero correspondiente
def deposito_bitcoin(usuario):
    bitcoin = conversion_bitcoin()
    monto = float(input('Digite el monto en Bitcoins a depositar\n>>>'))
    convertido = monto * bitcoin
    convertido = round(convertido,2)
    archivo = open(os.path.join(usuario, 'saldos.txt'), 'r+')
    monto_viejo = archivo.read()
    monto_viejo = float(monto_viejo)
    total = monto_viejo + convertido
    archivo.seek(0)
    archivo.write("{:.2f}\n".format(total)) #Bibliografia, del codigo usado
    archivo.close()
    limpiar_pantalla()
    print(f'Transaccion realizada, deposito exitoso de BTC{monto}, con un tipo de cambio de {bitcoin}, tu saldo actual es de ${total}')

#Aqui se realizara las verificaciones y depositos de dinero correspondientes
def deposito(usuario):
    try:
        dinero = int(input('1. Colones\n2. Dolares\n3. Bitcoin\nEn que moneda desea depositar:'))
        if dinero == 1:
            deposito_colon(usuario)
        elif dinero == 2:
            deposito_dolar(usuario)
        elif dinero == 3:
            deposito_bitcoin(usuario)
        else:
            print('Error, digite una de las opciones anteriores, volviendo al submenu')
    except ValueError:
        limpiar_pantalla()
        print('Error, no selecciono correctamente, volviendo al Submenu')

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
                if retiro(usuario) == 1:
                    break 
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
    intentos = 0
    while intentos < 3:
        try:
            retiro = float(input(f'Tu saldo actual actual es de ${ver_saldo(ID,dato)}\n¿cuanto desea retirar?:'))
            if retiro == 0:
                print('Error, no puede retirar montos menores o iguales a 0')
            elif retiro <= float(ver_saldo(ID, dato)):
                    archivo = open(os.path.join(ID, 'saldos.txt'), 'r+')
                    monto_viejo = archivo.read()
                    monto_viejo = float(monto_viejo)
                    monto_viejo -= retiro
                    archivo.seek(0)
                    archivo.write("{:.2f}\n".format(monto_viejo))
                    archivo.close()
                    limpiar_pantalla()
                    intentos = 3
                    print(f'Transaccion realizada, retiro exitoso de ${retiro}, tu saldo actual es de ${monto_viejo}')  
                    break        
            else:
                intentos += 1
                if intentos == 3:
                    limpiar_pantalla()
                    print('Supero el numero de intentos maximo, regresando al Menu Principal')
                    return dato
                limpiar_pantalla()
                print(f'Error, el saldo no es suficiente para retirar ${retiro}, intente nuevamente')
        except ValueError:
            intentos += 1
            limpiar_pantalla()
            print(f'Tiene que digitar un monto correcto')


#Fin Funciones de DreamWorldCasino
#Inicio Funciones Deposito Obligatorio


#Aqui se hara una funcion para retornar el minimo del deposito cada vez que sea necesario, siguiendo el mismo principio siempre que sea necesario
def minimo_deposito():
    archivo = open('configuraciones_avanzadas.txt', 'r')
    contenido = archivo.read()
    lineas = contenido.split('\n')
    linea_colon = lineas[5]
    dato, valor = linea_colon.split(':')
    archivo.close()
    valor = int(valor)
    return valor

#Aqui sera el menu del deposito obligatorio, sera requisito fundamental pasar aqui y depositar += 15 dolares para terminar el registro de usuario
def deposito_obligatorio():
    min = minimo_deposito()
    print(f'Como ultimo paso, necesitamos un deposito minimo de ${minimo_deposito()}')
    intentos = 0
    while intentos < 3:
        try:
            opcion = int(input('1. Colones\n2. Dolares\n3. Bitcoin\nEn que moneda desea depositar:'))
            #Siempre el valor se compara con el minimo de deposito para asi no permitir depositar menos de lo permitido
            if opcion == 1:
                valor = depo_colon()
                if valor >= minimo_deposito():
                    return valor
                else:
                    intentos += 1
                    print(f'Error: no puede depositar montos menores a ${minimo_deposito()}, intentelo nuevamente')
            elif opcion == 2:
                valor = depo_dolar()
                if valor >= minimo_deposito():
                    return valor
                else:
                    intentos += 1
                    print(f'Error: no puede depositar montos menores a ${minimo_deposito()}, intentelo nuevamente')
            elif opcion == 3:
                valor = depo_bitcoin()
                if valor >= minimo_deposito():
                    return valor
                else:
                    intentos += 1
                    print(f'Error: no puede depositar montos menores a ${minimo_deposito()}, intentelo nuevamente')
            else:
                print('Error, digite una de las opciones anteriores, volviendo al submenu')
            if intentos == 3:
                print('Se excedió el máximo de intentos para depositar el mínimo de dinero requerido, volviendo al menú principal')

            
            
        except ValueError:
            intentos += 1
            limpiar_pantalla()
            print('Error, no selecciono correctamente')

#Aqui simplemente se tomara el monto y lo retornara, para que se vea mas bonito
def depo_dolar():
    limpiar_pantalla()
    monto = float(input('Digite el monto en dolares a depositar\n>>>'))
    return monto

#Aqui se hara la conversion del colon y el retorno del valor en dolares
def depo_colon():
    limpiar_pantalla()
    monto = float(input(f'Digite el monto en colones a depositar, con un tipo de cambio de {conversion_colon()}\n>>>'))
    monto /= conversion_colon()
    monto = round(monto,2)
    return monto

#Aqui se hara la conversion del bitcoin y el retorno del valor en dolares
def depo_bitcoin():
    limpiar_pantalla()
    monto = float(input(f'Digite el monto en BTC a depositar, con un tipo de cambio de {conversion_bitcoin()}\n>>>'))
    monto *= conversion_bitcoin()
    monto = round(monto,2)
    return monto
    

#Fin Funciones Deposito Obligatorio


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
                                    limpiar_pantalla()
                                    monto = deposito_obligatorio()
                                    if monto == None:
                                        usuario_creado = True
                                        break
                                    elif monto >= minimo_deposito():
                                        time.sleep(0.5)
                                        limpiar_pantalla()
                                        print('El PIN ha sido creado exitosamente')
                                        os.mkdir(ID)
                                        print(f"el ID {ID} ha sido creado, volviendo al Menu Principal")
                                        archivo = open(os.path.join(ID, 'saldos.txt'), 'w')
                                        archivo.write("{:.2f}\n".format(monto))
                                        archivo.close()
                                        #Modos de lectura en BibliotecaOS.py
                                        archivo = open('usuarios_pines.txt', 'a')
                                        archivo.write(f'{ID}\n')
                                        archivo.write(f'{PIN}\n')
                                        archivo.close()
                                        usuario_creado = True
                                        break
                                    else:
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
        limpiar_pantalla()
        print('*Error: Debes ingresar un número entero. Intente nuevamente*')