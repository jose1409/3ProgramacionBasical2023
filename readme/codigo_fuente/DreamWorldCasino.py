import os
import time
from getpass import getpass

from configuracion_avanzada import menu_configuracion_avanzada
def limpiar_pantalla():
    if os.name == 'nt':  # Windows    #Toda la variable se refiese al sistema operativo windows(memorizable)
        os.system('cls')
# Menu Principal
os.chdir('/Users/Usuario/OneDrive/Documentos/GitHub/3ProgramacionBasical2023/readme/')
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
            '''Verificacion de usuario '''
        elif opcion == 3:
            menu_configuracion_avanzada()
            numero1 = int(input('Digite el primer numero:'))
        elif opcion == 4:
            print('Gracias por visitar DreamWorld Casino, vuelva pronto')
            break

        else:
            print('*Error: Debes ingresar un número entre 1 y 4. Intente nuevamente*')  
    except ValueError:
        print('*Error: Debes ingresar un número entero. Intente nuevamente*')
