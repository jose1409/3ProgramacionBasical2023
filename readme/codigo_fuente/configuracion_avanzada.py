import getpass
import os

# PIN especial definido por el equipo para permitir acceso al menú
specialPIN = "2023"
usuarios_pines_file = "usuarios_pines.txt"

def getUserInput(prompt):
    return input(prompt).strip()

def getHiddenInput(prompt): # ocultar el PIN de la pantalla
    return getpass.getpass(prompt)

def authenticateUser():
    attempts = 3
    while attempts > 0:
        enteredPIN = getHiddenInput("Bienvenido, Ingrese su PIN especial: ")
        if enteredPIN == specialPIN:
            return True
        attempts -= 1
        print("El PIN es incorrecto. Sus intentos restantes son:", attempts)
    return False

def cargar_usuarios_pines(file_path):
    usuarios_pines = {}
    try:
        with open(file_path, 'r') as file: 

            
            lines = file.readlines()
            lines = lines[1:]
            for index in range(0, len(lines), 2):
                
                usuario = lines[index]
                pin =  lines[index+1]
                # quitar \n de cada
                usuario = usuario[:len(usuario)-1]
                pin = pin[:len(pin)-1]

                usuarios_pines[usuario] = pin

    except FileNotFoundError:
        pass
    return usuarios_pines

def guardar_usuarios_pines(file_path, usuarios_pines):
    with open(file_path, 'w') as file:
        file.write(f"{specialPIN}\n")
        for usuario, pin in usuarios_pines.items():
            file.write(f"{usuario}\n")
            file.write(f"{pin}\n")

def deleteUser(userID):
    usuarios_pines = cargar_usuarios_pines(usuarios_pines_file)
    

    if userID in usuarios_pines:
        del usuarios_pines[userID]
        guardar_usuarios_pines(usuarios_pines_file, usuarios_pines)
        print(f"El usuario con el siguiente ID {userID} ha sido eliminado.")
    else:
        print(f"El ID {userID} es incorrecto o no existe en la lista de usuarios. Intente nuevamente.")

def modifySystemValues():
    conversionOptions = [
        "Tipo de cambio: Compra de dólares usando colones",
        "Tipo de cambio: Compra de dólares usando bitcoins",
        "Valor acumulado Tragamonedas",
        "Apuesta mínima Tragamonedas",
        "Apuesta mínima Blackjack",
        "Inversión mínima para registrarse",
        "Salir"
    ]
    while True:
        print("¿Qué desea modificar el día de hoy?")
        for idx, option in enumerate(conversionOptions, start=1):
            print(f"{idx}. {option}")
        
        try:
            choice = int(getUserInput("Ingrese el número de la opción que desea modificar: "))
        
            if 1 <= choice <= len(conversionOptions) - 1:
                newValue = getUserInput("Ingrese el nuevo valor: ")
                # implementación para modificar los valores del sistema
                print(f"El siguiente Valor ha sido modificado para la opción {choice}: {newValue}")
            elif choice == len(conversionOptions):
                print("Volviendo al menú principal.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Error: Debes ingresar un número entero. Intente nuevamente.")

def mainMenu():
    while True:
        print("Bienvenido al menú principal.")
        print("1. Eliminación de usuario")
        print("2. Modificar valores del sistema")
        print("3. Salir")

        try:
            choice = int(getUserInput("Ingrese el número de la opción que desea elegir: "))
        
            if choice == 1:

                userID = getUserInput("Ingrese el ID del usuario que desea eliminar: ")
                deleteUser(userID)
            elif choice == 2:
                modifySystemValues()
            elif choice == 3:
                print("Saliendo del programa.")
                exit()
            else:
                print("Opción inválida. Vuelva a intentarlo.")
        except ValueError:
            print("Error: Debes ingresar un número entero. Intente nuevamente.")

def menu_configuracion_avanzada():
    print("Este es el menú de Configuración Avanzada. Autenticación es requerida.")
    if authenticateUser():
        mainMenu()
    else:
        print("Autenticación fallida. Saliendo del programa.")

if __name__ == "__main__":
    menu_configuracion_avanzada()




