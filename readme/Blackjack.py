import random
import time
dinero_temporal = 500
numero_crupier = []
palo_crupier = []
numero_usuario = []
palo_usuario = []
suma_usuario = 0
suma_crupier = 0
def obtener_valor_carta(numero, mano):
    if numero in ['J', 'Q', 'K']:
        return 10
    elif numero == 'A':
        # Si sumar 11 no lleva a una bancarrota (más de 21 puntos), se considera 11, en caso contrario, se considera 1.
        return 11 if sum(mano) + 11 <= 21 else 1
    return numero

def baraja():
    palos = ['Corazon', 'Trebol', 'Picas', 'Diamante']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    palo = random.randint(0, 3)
    numero_baraja = random.randint(0, 12)

    return numeros[numero_baraja], palos[palo]

def repartir_cartas():
    # Primera carta para el usuario
    numero, palo = baraja()
    valor_carta = obtener_valor_carta(numero, numero_usuario)
    numero_usuario.append(valor_carta)
    palo_usuario.append(palo)

    # Segunda carta para el crupier
    numero, palo = baraja()
    valor_carta = obtener_valor_carta(numero, numero_crupier)
    numero_crupier.append(valor_carta)
    palo_crupier.append(palo)

    # Tercera carta para el usuario
    numero, palo = baraja()
    valor_carta = obtener_valor_carta(numero, numero_usuario)
    numero_usuario.append(valor_carta)
    palo_usuario.append(palo)

    # Cuarta carta para el Crupier (Oculta)
    numero, palo = baraja()
    valor_carta = obtener_valor_carta(numero, numero_crupier)
    numero_crupier.append(valor_carta)
    palo_crupier.append(palo)

    #Instrucciones del juego/Menu
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
apuesta_minima = int(input('¿Cuanto desea apostar?'))
    #Dinero temporal para probar el juego
if dinero_temporal < apuesta_minima:
    print('Dinero insuficiente, ingrese otro monto')
    
    #Reparticion de cartas
else:
    repartir_cartas()
    #Cartas del usuario
    for i in range(len(numero_usuario)):
        print(f"{numero_usuario[i]} de {palo_usuario[i]}")
        time.sleep(1.2)

    #Cartas del Crupier
    print('\nCarta Oculta')
    time.sleep(1.2)
    for i in range(1, len(numero_crupier)):
        print(f"{numero_crupier[i]} de {palo_crupier[i]}")



