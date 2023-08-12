'''
Instrucciones
Apuesta = Verificacion
Repartir Cartas/Mostrarlas
Ligar/Quedarse

'''
import time
import random
import os
apuesta = 0
apuesta_minima_temporal = 10
dinero_temporal = 1000
baraja = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A'],[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
usuario = []   
crupier = []

def limpiar():
    os.system('cls')


def requisito_dinero_temporal(): 
        #Ingresar a la carpeta archivos avanzados y leer el minimo de apuesta disponible.
    global apuesta
    global dinero_temporal
    num = 0
    while num <=0:
        try:
            vaciar_lista()
            print(f'Tu saldo es de {dinero_temporal}')
            apuesta = int(input('¿Cuanto desea apostar?'))
                #Entrar a la carpeta de usuario y saldos, verificar que posea el dinero suficiente
            if apuesta > dinero_temporal:
                limpiar()
                print('Dinero insuficiente, intente nuevamente')
            elif apuesta < apuesta_minima_temporal:
                limpiar()
                print('Apuesta minima de ₡10')
            else:
                num += 1
                dinero_temporal -= apuesta
                juego()
        except ValueError:
            limpiar()
            print('Digite un monto con digitos numericos -_-')


def vaciar_lista():
    usuario.clear()
    crupier.clear()
        #Instrucciones iniciales

        
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


def acomodar_letras(carta):
    for i in range(len(carta)):
        if carta[i][0] == 'A':
            temp = carta[i]
            carta[i]=carta[len(carta)-1]
            carta[len(carta)-1]=temp
    

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


def juego():
    mezclar(usuario), mezclar(crupier)
    print(f'---Baraja crupier---')
    mostrar_juego_dos(crupier)
    print()  
    time.sleep(1)
    print(f"---Baraja usuario---")
    mostrar_juego(usuario)
    time.sleep(1)
    print(f"-----suma total usuario-----\n{suma_total(usuario)}\n")
    opcion = input('Ligar, Plantarse:')
    if opcion.lower() == 'ligar':
        ligar(usuario)
    elif opcion.lower() == 'plantarse':
        plantarse()


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
def mostrar_juego_dos(figuras):
    time.sleep(0.5)
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
    print('Carta #2 Oculta')

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

  
def juego_despues_ligar():
    temp=True
    print(f'Tu saldo es de {dinero_temporal}')
    print(f'---Baraja crupier---')
    mostrar_juego_dos(crupier)
    print()
    print(f"---Baraja usuario---")
    mostrar_juego(usuario)
    print(f"-----suma total usuario-----\n{suma_total(usuario)}\n")
    
    if suma_total(usuario) > 21:
        opcion = input('Usted perdio, ¿Desea jugar de nuevo? (si/no):')
        if opcion.lower() == 'si':
            limpiar()
            requisito_dinero_temporal()
        elif opcion.lower() == 'no':
            print()         #Volver al Menu principal (Funcion de devolver el dinero al archivo txt saldos)
    elif suma_total(usuario) <=21:
        opcion = input('Ligar, Plantarse:')
        if opcion.lower() == 'ligar':
            ligar(usuario)
        elif opcion.lower() == 'plantarse':
            plantarse()
        
        
def plantarse():
    print()



def inicio():
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
        
inicio()



