import time
import random
import os
apuesta = 0
apuesta_dividir = 0
apuesta_minima_temporal = 0
dinero_temporal = 0
baraja = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
usuario = []   
crupier = []
usuario_dividir = []
#Funcion que se llamara para limpiar la terminal para que no se llene de tanta informacion
def limpiar():
    os.system('cls')

#Funcion que hara verificaciones de dinero y requisitos de dinero minimo
def requisito_dinero_temporal(): 
        #Ingresar a la carpeta archivos avanzados y leer el minimo de apuesta disponible. (Modificaciones)
    global apuesta
    global dinero_temporal
    num = 0
    while num <=0:
        try:
            vaciar_lista()
            print(f'Tu saldo es de ${dinero_temporal}')
            apuesta = int(input('¿Cuanto desea apostar?'))
            if apuesta > dinero_temporal:
                limpiar()
                print('Dinero insuficiente, intente nuevamente')
            elif apuesta < apuesta_minima_temporal:
                limpiar()
                print(f'Apuesta minima de ${apuesta_minima_temporal}')
            else:
                num += 1
                dinero_temporal -= apuesta
                limpiar()
                juego()
        except ValueError:
            limpiar()
            print('Digite un monto con digitos numericos -_-')

#Funcion que se llamara para que despues de finalizar un juego las listas se limpien y queden para usar de nuevo
def vaciar_lista():
    usuario.clear()
    crupier.clear()
    usuario_dividir.clear()

#Funcion que se llamara unicamente si el usuario las solicita
def instrucciones():
    print('INSTRUCCIONES\n'
        'El objetivo de cualquier mano de blackjack es derrotar a la banca\n'
        'Puedes ganar con una puntuación igual o menor a 21 cuando la mano de la banca supera los 21 puntos o este mas alejado\n'
        'Cuando el valor total de tu mano es de 22 o más, esto se conoce comúnmente como "bancarrota", y automáticamente perderás cualquier dinero apostado\n'
        '\n'
        'LIGAR:\n' 
        '      Puedes solicitar cartas extra para mejorar tu mano. Las cartas se pueden pedir de a una hasta que el valor total de la mano sea 21 o superior\n'
        'PLANTARSE:\n' 
        '          Cuando el valor total de tu mano sea 21 o inferior, puedes elegir plantarte y no arriesgar las posibilidades de que tu mano supere los 21 en valor total\n'
        'DIVIDIR:\n'
        '        Cuando tus primeras dos cartas tienen el mismo valor (ocho-ocho, jota-diez, etc.), puedes realizar apuestas adicionales\n' 
        '        (igual a la apuesta inicial) y crear una segunda mano con la que jugar contra la banca\n'
        'DOBLAR:\n' 
        '       Puedes colocar una apuesta extra, igual a la apuesta inicial, a cambio de una sola carta más para tu mano, después de la cual te plantarás automáticamente\n')

#Aqui se hara el llamado inicial y reparticion de dos cartas para iniciar el juego
def mezclar(repartir_cartas):
    numero = 0
    while numero <2:
            #Recorre la lista para el lado
        j=random.randint(0,12)
            #Recorre la lista para abajo
        i=random.randint(0,3)
        if baraja[i][j] != 0:
            temporal = []
                #Primero se recorre vertical y luego horizontal (abajo y derecha)
            temporal.append(baraja[i][j])
            temporal.append(i)
            repartir_cartas.append(temporal)
            baraja[i][j] = 0
            numero +=1

#Esta se llamara para que cuando exista una A sea enviada al final de la lista y haga su conversion a numero correctamente
def acomodar_letras(carta):
        #Leera toda la lista y si encuentra una A, la tomara, la eliminara y trasladara al final de la lista
    for i in range(len(carta)):
        if carta[i][0] == 'A':
            temp = carta[i]
            carta[i]=carta[len(carta)-1]
            carta[len(carta)-1]=temp
    
#Esta funcion se llamara para hacer la suma respectiva de crupier y usuario cada vez que sea necesario, tanto condicionales como resultados
def suma_total(carta):
    acomodar_letras(carta)
    suma=0
    for i in range(len(carta)):
        if carta[i][0] == 'J' or carta[i][0] =='Q' or carta[i][0] == 'K':
            suma+=10
        elif carta[i][0] == 'A':
            if suma <=10:
                suma += 11
            else:
                suma+=1
        else:
            suma += carta[i][0]    
    return suma

#Juego inicial, aqui se llamara distintas funciones para mostrar el juego inicial e inidicar primeras opciones al usuario.
def juego():
    global apuesta
    global dinero_temporal
    global apuesta_dividir
    print(f'Saldo: ${dinero_temporal}\nApuesta: ${apuesta}')
    mezclar(usuario),mezclar(crupier)
    print(f'---Baraja crupier---')
    mostrar_juego_dos(crupier)
    print()  
    time.sleep(1)
    print(f"---Baraja usuario---")
    mostrar_juego(usuario)
    time.sleep(1)
    print(f"-----suma total usuario-----\n{suma_total(usuario)}\n")
    num=0
        #Aqui habran condicionales y opciones para jugar ademas de requisitos de dinero en dividir y duplicar
    while num <=0:
        opcion = input('Ligar, Plantarse, Duplicar, Dividir:')
        if opcion.lower() == 'ligar':
            ligar(usuario)
            num +=1
        elif opcion.lower() == 'plantarse':
            limpiar()
            plantarse()
            num +=1
        elif opcion.lower() == 'duplicar':
            if dinero_temporal < apuesta:
                print('Error: Dinero insuficiente, Digite otra opcion')
            else:
                dinero_temporal -= apuesta
                apuesta = apuesta*2
                ligar_dos(usuario)
                num +=1
        elif opcion.lower() == 'dividir':
            if dividir(usuario[0][0]) == dividir(usuario[1][0]): 
                if dinero_temporal > apuesta:
                #La lista usuario deja de tener dos valores, se elimina el segundo y este pasa a ser parte de la segunda lista
                    temp = usuario[1]
                    usuario.remove(temp)
                    usuario_dividir.append(temp)
                    apuesta_dividir += apuesta
                    dinero_temporal -= apuesta_dividir
                    num+=1
                    limpiar()
                    juego_dividido()
                else:
                    print('Error: Dinero insuficiente, Digite otra opcion')
            else:
                print('Error: Para dividir necesita dos cartas de igual valor. Digite otra opcion')
        else:
            print('Error: Digite una de las opciones anteriores')

#Aqui se mostrara unicamente la careta del juego a la hora de dividir
def mostrar_juego_dividido():
    print(f'Saldo: ${dinero_temporal}\nApuesta 1:${apuesta}\nApuesta 2:${apuesta_dividir}')
    print(f'---Baraja crupier---')
    mostrar_juego_dos(crupier)
    print()  
    time.sleep(1)
    print(f"---Baraja usuario 1---")
    mostrar_juego(usuario)
    print(f"-----suma total -----\n{suma_total(usuario)}\n")
    time.sleep(1)
    print(f"---Baraja usuario 2---")
    mostrar_juego(usuario_dividir)
    print(f"-----suma total -----\n{suma_total(usuario_dividir)}\n")

#Aqui se mostrara la careta del juego a la hora de dividir final, quiere decir que estara disponible con la suma del crupier y la carta a la vista del usuario
def mostrar_juego_dividido_final():
    print(f'Saldo: ${dinero_temporal}\nApuesta 1:${apuesta}\nApuesta 2:${apuesta_dividir}')
    print(f'---Baraja crupier---')
    mostrar_juego(crupier)
    print(f"-----suma total -----\n{suma_total(crupier)}\n")
    time.sleep(1)
    print(f"---Baraja usuario 1---")
    mostrar_juego(usuario)
    print(f"-----suma total -----\n{suma_total(usuario)}\n")
    time.sleep(1)
    print(f"---Baraja usuario 2---")
    mostrar_juego(usuario_dividir)
    print(f"-----suma total -----\n{suma_total(usuario_dividir)}\n")

#Aqui sera las opciones despues de dividir para jugar
def juego_dividido():
    mostrar_juego_dividido()
    ciclo = 1
    if suma_total(usuario) > 21:
        print('Usted perdio con la baraja 1: Siguiendo a Baraja 2')
        ciclo = 2
    if suma_total(usuario_dividir) > 21:
        print('Usted perdio con la baraja 2.')
    if suma_total(usuario) > 21 and suma_total(usuario_dividir) > 21:
        opcion = input('Usted perdio ambos juegos, ¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)
    opcion_dividir(ciclo)

#Aqui sera las opciones despues de dividir para jugar con la baraja 2
def juego_dividido_dos():
    mostrar_juego_dividido()
    ciclo = 2
    if suma_total(usuario_dividir) > 21:
        print('Usted perdio con la baraja 2: Plantandose Automaticamente')
        juego_dividido_plantado()
    if suma_total(usuario) > 21 and suma_total(usuario_dividir) > 21:
        opcion = input('Usted perdio ambos juegos, ¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)
    if suma_total(usuario_dividir) <= 21:
        opcion_dividir(ciclo)

#Todas las opciones, no se muestra, unicamente esta programado para ligar y plantarse, ademas de sus respectivas señales de error
def opcion_dividir(num):
    while num <= 2:
        opcion = input(f'Baraja {num}: Ligar, Plantarse:')
        if opcion.lower() == 'ligar':
            if num == 1:
                ligar_tres(usuario,num)
                num += 2
            elif num == 2:
                ligar_tres(usuario_dividir,num)
                num += 1
        elif opcion.lower() == 'plantarse':
            if num == 1:
                limpiar()
                juego_dividido_dos()
                num += 2
            elif num == 2:
                limpiar()
                juego_dividido_plantado()
                num += 1
        elif opcion.lower() == 'dividir':
            print('Dividir esta disponible solamente en la primer mano')
        elif opcion.lower() == 'duplicar':
            print('Duplicar esta disponible solamente en la primer mano')
        else:
            print('Error: Digite una de las opciones anteriores')

#Aqui se mostrara todos los resultados, si perdio, empato o gano, con ambos juegos a la hora de dividir.
def juego_dividido_plantado():
    mostrar_juego_dividido_final()
    global apuesta
    global apuesta_dividir
    global dinero_temporal
    if suma_total(usuario) > 21 and suma_total(usuario_dividir) > 21:
        opcion = input('Usted perdio ambos juegos, ¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)
    elif suma_total(crupier) < 15:
        ligar_cuatro(crupier)
    else:
        if suma_total(usuario) <= 21 and suma_total(usuario) > suma_total(crupier):
            print(f'Felicidades, usted gano, tu apuesta de ${apuesta} te hizo ganar ${apuesta*2}')
            dinero_temporal += apuesta*2
        elif suma_total(usuario) == suma_total(crupier):
            print(f'Empate, recuperas tu apuesta de {apuesta} del juego 1')
            dinero_temporal += apuesta
        else:
            print('Usted perdio el juego 1:')

        if suma_total(usuario_dividir) <= 21 and suma_total(usuario_dividir) > suma_total(crupier):
            print(f'Felicidades, usted gano el juego 2, tu apuesta de ${apuesta_dividir} te hizo ganar ${apuesta_dividir*2}')
            dinero_temporal += apuesta_dividir*2
        elif suma_total(usuario_dividir) == suma_total(crupier):
            print(f'Empate en el juego 2, recuperas tu apuesta de ${apuesta_dividir}')
            dinero_temporal += apuesta_dividir
        else:
            print('Usted perdio el juego 2:')

        opcion = input('¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)

#Otra funcion de ligado
def ligar_cuatro(repartir_cartas):
    numero = 0
    while numero <=0:
            #Recorre la lista para el lado
        j=random.randint(0,12)
            #Recorre la lista para abajo
        i=random.randint(0,3)
        if baraja[i][j] != 0:
            temporal = []
                #Primero se recorre vertical y luego horizontal (abajo y derecha)
            temporal.append(baraja[i][j])
            temporal.append(i)
            repartir_cartas.append(temporal)
            baraja[i][j] = 0
            numero +=1
    limpiar()
    juego_dividido_plantado()

#Me ayuda a retornar un valor a los numeros y asi poder saber si es posible dividir
def dividir(valor):
    temp = 0
    if valor == 'A':
        temp = 11
    elif valor == 'K':
        temp = 10
    elif valor == 'Q':
        temp = 10
    elif valor == 'J':
        temp = 10
    else:
        temp = valor
    return temp

#Esta funcion me mostrara el juego del ususario, juego completo
def mostrar_juego(figuras):
    for i in range(len(figuras)):
        time.sleep(0.5)
        if figuras[i][1] == 0:
            print(f'{figuras[i][0]} de Bastos')
        elif figuras[i][1] == 1:
            print(f'{figuras[i][0]} de Picas')
        elif figuras[i][1] == 2:
            print(f'{figuras[i][0]} de Treboles')
        elif figuras[i][1] == 3:
            print(f'{figuras[i][0]} de Corazones')

#Este funcion me mostrara el juego del crupier, ocultando la primer carta y mostrando unicamente la Carta numero 2.
def mostrar_juego_dos(figuras):
    time.sleep(0.5)
    print('Carta #1 Oculta')
    for i in range(1,len(figuras)):
        if figuras[i][1] == 0:
            print(f'{figuras[i][0]} de Bastos')
        elif figuras[i][1] == 1:
            print(f'{figuras[i][0]} de Picas')
        elif figuras[i][1] == 2:
            print(f'{figuras[i][0]} de Treboles')
        elif figuras[i][1] == 3:
            print(f'{figuras[i][0]} de Corazones') 
    time.sleep(0.5) 

#Otra funcion de ligar con dos diferentes posibles juegos de acuerdo del temp
def ligar_tres(repartir_cartas, temp):
    numero = 0
    while numero <=0:
            #Recorre la lista para el lado
        j=random.randint(0,12)
            #Recorre la lista para abajo
        i=random.randint(0,3)
        if baraja[i][j] != 0:
            temporal = []
                #Primero se recorre vertical y luego horizontal (abajo y derecha)
            temporal.append(baraja[i][j])
            temporal.append(i)
            repartir_cartas.append(temporal)
            baraja[i][j] = 0
            numero +=1
    limpiar()
    if temp == 1:
        juego_dividido()
    elif temp == 2:
        juego_dividido_dos()

#Esta funcion sera llamada cada vez que el usuario desee pedir una carta y redirigiendolo a juego_despues_ligar()
def ligar(repartir_cartas):
    numero = 0
    while numero <=0:
            #Recorre la lista para el lado
        j=random.randint(0,12)
            #Recorre la lista para abajo
        i=random.randint(0,3)
        if baraja[i][j] != 0:
            temporal = []
                #Primero se recorre vertical y luego horizontal (abajo y derecha)
            temporal.append(baraja[i][j])
            temporal.append(i)
            repartir_cartas.append(temporal)
            baraja[i][j] = 0
            numero +=1
    limpiar()
    juego_despues_ligar()

#Esta funcion sera llamada por el crupier para solicitar cartas cada vez que lo necesite
def ligar_dos(repartir_cartas):
    numero = 0
    while numero <=0:
            #Recorre la lista para el lado
        j=random.randint(0,12)
            #Recorre la lista para abajo
        i=random.randint(0,3)
        if baraja[i][j] != 0:
            temporal = []
                #Primero se recorre vertical y luego horizontal (abajo y derecha)
            temporal.append(baraja[i][j])
            temporal.append(i)
            repartir_cartas.append(temporal)
            baraja[i][j] = 0
            numero +=1
    limpiar()
    plantarse()

#Segunda pestaña de juego, sera mejorada con condicionales por si se pasa de 21
def juego_despues_ligar():
    print(f'Saldo: ${dinero_temporal}\nApuesta: ${apuesta}')
    print(f'---Baraja crupier---')
    mostrar_juego_dos(crupier)
    print()
    print(f"---Baraja usuario---")
    mostrar_juego(usuario)
    print(f"-----suma total usuario-----\n{suma_total(usuario)}\n")
    if suma_total(usuario) > 21:
        opcion = input('Usted perdio, ¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)
    elif suma_total(usuario) <=21:
        num = 0
        while num <= 0:
            opcion = input('Ligar, Plantarse:')
            if opcion.lower() == 'ligar':
                num += 1
                ligar(usuario)
            elif opcion.lower() == 'plantarse':
                num += 1
                limpiar()
                plantarse()
            elif opcion.lower() == 'duplicar':
                print('Error: Duplicar esta disponible solo en ronda 1, Digite otra opcion')
            elif opcion.lower() == 'dividir':
                print('Error: Dividir esta disponible solo en ronda 1, Digite otra opcion')
            else:
                print('Error: Digite (ligar/plantarse)')

#Una vez que el usuario se plante, correra esta funcion y jugara automaticamente hasta que alcance 15 o supere los 21 y pierda   
def plantarse():
    global dinero_temporal
    print(f'Saldo: ${dinero_temporal}\nApuesta: ${apuesta}')
    print(f'---Baraja crupier---')
    mostrar_juego(crupier)
    print(f"-----suma total crupier-----\n{suma_total(crupier)}\n")
    print()
    print(f"---Baraja usuario---")
    mostrar_juego(usuario)
    print(f"-----suma total usuario-----\n{suma_total(usuario)}\n")
    time.sleep(1)
    if suma_total(usuario) > 21:
        opcion = input('Usted perdio, ¿Desea jugar de nuevo? (si/no):')
        jugar_nuevamente(opcion)
    elif suma_total(crupier) < 15:
        ligar_dos(crupier)
    else:
        if suma_total(usuario) <= 21 and suma_total(usuario) > suma_total(crupier) or suma_total(crupier) > 21:
            print(f'Felicidades, usted gano, tu apuesta de ${apuesta} te hizo ganar ${apuesta*2}')
            dinero_temporal += apuesta*2
            opcion = input('¿Desea jugar de nuevo? (si/no):')
            jugar_nuevamente(opcion)
        elif suma_total(usuario) == suma_total(crupier):
            print(f'Empate, recuperas tu apuesta de ${apuesta}')
            dinero_temporal += apuesta
            opcion = input('¿Desea jugar de nuevo? (si/no):')
            jugar_nuevamente(opcion)
        else:
            opcion = input('Usted perdio, ¿Desea jugar de nuevo? (si/no):')
            jugar_nuevamente(opcion)
            
#Inicio del juego, con opcion de ver las instrucciones y dirigiendose a la funcion de las apuestas,
def inicio(dato):
    apuesta_min()
    saldo_usuario(dato)
    num = 0
    while num <=0:
        opcion = input('Desea ver las Instrucciones? (si/no):')
        if opcion.lower() == 'si':
            instrucciones()
            num +=1
            requisito_dinero_temporal()
        elif opcion.lower() == 'no':
            num +=1
            requisito_dinero_temporal()
        else:
            limpiar()
            print('Digite "si" o "no", no otra estupidez')
    saldo_recuperar(dato)

#Esta funcion sera usada cada vez que finaliza el juego, no importa si pierde, gana o empata, y su funcion sera volver al submenu de juegos o jugar nuevamente
def jugar_nuevamente(opcion):
    num = 0
    while num <= 0:
        if opcion.lower() == 'si':
            limpiar()
            num += 1
            requisito_dinero_temporal()
        elif opcion.lower() == 'no':
            print('Volviendo al Submenu de Juegos')         #Volver al Menu principal (Funcion de devolver el dinero al archivo txt saldos)
            time.sleep(1)
            limpiar()
            num += 1
        else:
            opcion = input('Error: Digite (si/no)')
    
#Aqui se accedera al saldo del usuario registrado y se trasladara al dinero temporal    
def saldo_usuario(dato):
    global dinero_temporal
    archivo = open(os.path.join(dato, 'saldos.txt'), 'r')
    saldo = archivo.read()
    archivo.close()
    saldo = int(saldo)
    dinero_temporal += saldo

#Aqui se hara la verificacion de apuesta minima de acuerdo a lo que el archivo ajustes avanzados diga
def apuesta_min():
    global apuesta_minima_temporal
    archivo = open('configuraciones_avanzadas.txt', 'r')
    contenido = archivo.read()
    lineas = contenido.split('\n')
    linea_black = lineas[4]
    dato, valor = linea_black.split(':')
    apuesta_minima_temporal = int(valor)
    archivo.close()

#A la hora de que el usuario salga del juego, se actualizara su saldo desde este archivo automaticamente
def saldo_recuperar(usuario):
    dinero_temporal
    archivo = open(os.path.join(usuario, 'saldos.txt'), 'w')
    archivo.write(str(dinero_temporal) + '\n')
    archivo.close()