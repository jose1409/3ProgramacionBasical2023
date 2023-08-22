"Este es el menu de configuraciones avanzadas el cual se despliega del menu principal y permite la eliminacion de usuarios y modificacion de valores"
import getpass
import os

# PIN especial definido por el equipo para permitir acceso al menú
specialPIN = "2023"
usuarios_pines_file = "./usuarios_pines.txt"  #path para archivo de usuarios pines
configuraciones_avanzadas_file = "./configuraciones_avanzadas.txt" #path para archivo de configuraciones avanzadas

#para poder obtener la entrada del usuario
def getUserInput(prompt):
    return input(prompt).strip()

#uso de getpass para ocultar la entrada del usuario
def getHiddenInput(prompt):
    return getpass.getpass(prompt)

#funcion que permita autenticar al usuario 
def authenticateUser():
    attempts = 3
    while attempts > 0:
        enteredPIN = getHiddenInput("Bienvenido, Ingrese su PIN especial: ")
        if enteredPIN == specialPIN:
            return True
        attempts -= 1
        print("El PIN es incorrecto. Sus intentos restantes son:", attempts)
    return False


def cargar_usuarios_pines(file_path): #cargar los usuarios desde el archivo
    usuarios_pines = {}
    try:
        with open(file_path, 'r') as file: #abrir el archivo para leer los datos que contiene

            
            lines = file.readlines() 
            lines = lines[1:] #se utiliza para omitir la primera linea que corresponde al pin especial
            for index in range(0, len(lines), 2): #rango de lineas 
                
                usuario = lines[index]
                pin =  lines[index+1]
                # quitar \n de cada linea
                usuario = usuario[:len(usuario)-1]
                pin = pin[:len(pin)-1]

                usuarios_pines[usuario] = pin

    except FileNotFoundError: #bloque para evitar que el programa se caiga si el archivo no existe
        pass
    return usuarios_pines #devolver el diccionario que contiene los datos cargados del archivo

#funcion para guardar usuarios 
def guardar_usuarios_pines(file_path, usuarios_pines):
    with open(file_path, 'w') as file:
        file.write(f"{specialPIN}\n") #escribe el pin especial en la primera linea
        for usuario, pin in usuarios_pines.items():
            file.write(f"{usuario}\n") #escribe el usuario en una linea
            file.write(f"{pin}\n") #escribe en pin del usuario en la siguiente linea correspondiente

def deleteUser(userID): 
    usuarios_pines = cargar_usuarios_pines(usuarios_pines_file) #permite cargar los usuarios y pines desde el archivo
    

    if userID in usuarios_pines:  #si el usuario existe lo  borra
        del usuarios_pines[userID]
        guardar_usuarios_pines(usuarios_pines_file, usuarios_pines)
        print(f"El usuario con el siguiente ID {userID} ha sido eliminado.")
    else:
        print(f"El ID {userID} es incorrecto o no existe en la lista de usuarios. Intente nuevamente.")

#funcion para cargar las configuraciones avanzadas
def cargar_configuraciones_avanzadas(file_path):
    configuraciones = {}
    try:
        with open(file_path, 'r') as file: #leer archivo en modo lectura
            lines = file.readlines()
            for line in lines: #recorrer cada linea
                key, value = line.strip().split(":") #eliminar espacios en blanco
                configuraciones[key] = value #key es la clave y  value el valor que se ingresara al diccionario para acceder y modificar valores
    except FileNotFoundError:
        pass
    return configuraciones

def guardar_configuraciones_avanzadas(file_path, configuraciones):
    with open(file_path, 'w') as file:
        for key, value in configuraciones.items():
            file.write(f"{key}:{value}\n")

#funcion para modifcar valores del sistema

def modifySystemValues():
    conversionOptions = [
        "tipocambiocolones",
        "tipocambiobitcoin",
        "acumuladotragamonedas",
        "minimotragamonedas",
        "minimoblackjack",
        "inversionminima",
        "Salir"
    ] #opciones disponibles

    configuraciones = cargar_configuraciones_avanzadas(configuraciones_avanzadas_file) #carga los valores actuales desde el archivo

    while True:
        print("¿Qué desea modificar el día de hoy?")
        for idx, option in enumerate(conversionOptions, start=1):
            print(f"{idx}. {option}")

        try:
            choice = int(getUserInput("Ingrese el número de la opción que desea modificar: ")) #obtener la eleccion del usuario

            if 1 <= choice <= len(conversionOptions)-1:
                option_to_modify = conversionOptions[choice - 1]
                current_value = configuraciones.get(option_to_modify, "No se encontró valor")
                print(f"Valor actual para {option_to_modify}: ${current_value}") #valor actual

                new_value = getUserInput("Ingrese el nuevo valor: ")
                configuraciones[option_to_modify] = new_value
                guardar_configuraciones_avanzadas(configuraciones_avanzadas_file, configuraciones)
                #guarda los nuevos valores en el archivo

                print(f"El valor para {option_to_modify} ha sido modificado exitosamente.")
            elif choice == len(conversionOptions) :
                return
            else:
                print("Opción inválida.")
        except Exception as e: #permite atrapar todas las excepciones
            print("Error: Debes ingresar un número entero. Intente nuevamente." + e)

def mainMenu(): #muestra el menu principal
    while True:
        print("Bienvenido al menú principal.")
        print("1. Eliminación de usuario")
        print("2. Modificar valores del sistema")
        print("3. Salir")

        try:
            choice = int(getUserInput("Ingrese el número de la opción que desea elegir: "))
        
            if choice == 1:

                userID = getUserInput("Ingrese el ID del usuario que desea eliminar: ")  #solicitar al usuario que ID desea eliminar
                deleteUser(userID)
            elif choice == 2:
                modifySystemValues() #llama a la funcion para modificar las configuraciones avanzadas
            elif choice == 3:
                print("Saliendo del programa.")
                return
            else:
                print("Opción inválida. Vuelva a intentarlo.")
        except Exception as e:
            print("Error: Debes ingresar un número entero. Intente nuevamente." + e)

def menu_configuracion_avanzada():
    print("Este es el menú de Configuración Avanzada. Autenticación es requerida.")
    if authenticateUser():
        mainMenu()
    else:
        print("Autenticación fallida. Saliendo del programa.")

if __name__ == "__main__": #ejecuta el menu de configuracion avanzada al llamar la funcion de configuracion avanzada
    menu_configuracion_avanzada()
